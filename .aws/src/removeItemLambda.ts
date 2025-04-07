import {Construct} from 'constructs';
import {config} from './config';
import {
  LAMBDA_RUNTIMES,
  PocketSQSWithLambdaTarget,
  PocketVPC
} from '@pocket-tools/terraform-modules';
import {CloudwatchEventRule} from '@cdktf/provider-aws/lib/cloudwatch-event-rule';
import {CloudwatchEventTarget} from '@cdktf/provider-aws/lib/cloudwatch-event-target';
import {DataAwsSsmParameter} from '@cdktf/provider-aws/lib/data-aws-ssm-parameter';
import {Elasticache} from './elasticache';
import {SqsQueuePolicy} from '@cdktf/provider-aws/lib/sqs-queue-policy';

export class RemoveItemLambda extends Construct {
  constructor(scope: Construct, name: string, elasticache: Elasticache) {
    super(scope, name);

    const vpc = new PocketVPC(this, 'pocket-shared-vpc');

    const { sentryDsn, gitSha } = this.getEnvVariableValues();

    const sqsWithLambda = new PocketSQSWithLambdaTarget(this, 'remove-sqs-lambda', {
      name: `${config.prefix}-Sqs-RemoveEventHandler`,
      batchSize: 1,
      sqsQueue: {
        maxReceiveCount: 3, // 2 retries
        visibilityTimeoutSeconds: 300,
      },
      lambda: {
        runtime: 'python3.9' as LAMBDA_RUNTIMES,
        handler: 'remove_item_lambda.sqs_handler.handler',
        timeout: 120,
        executionPolicyStatements: [
          {
            effect: 'Allow',
            actions: ['elasticache:ModifyCacheCluster', 'elasticache:DescribeCacheClusters'],
            resources: [elasticache.clusterArn],
          },
        ],
        environment: {
          SENTRY_DSN: sentryDsn,
          GIT_SHA: gitSha,
          ENVIRONMENT: config.environment === 'Prod' ? 'production' : 'development',
          ELASTICACHE_SERVERS: elasticache.nodeList.join(','), // Pass node list to Lambda
        },
        vpcConfig: {
          securityGroupIds: vpc.internalSecurityGroups.ids,
          subnetIds: vpc.privateSubnetIds,
        },
        codeDeploy: {
          region: 'us-east-1',
          accountId: '410318598490',
        },
      },
    });

    const eventRule = new CloudwatchEventRule(this, 'remove-event-rule', {
      name: `${config.prefix}-RemoveEventRule`,
      description: 'Event rule for REMOVE_ITEM events to SQS',
      // source and detail-type are defined in:
      // https://github.com/Pocket/content-monorepo/blob/main/servers/curated-corpus-api/src/config/index.ts
      eventPattern: JSON.stringify({
        source: ['curation-migration-datasync'],
        'detail-type': ['remove-approved-item'],
      }),
      eventBusName: 'default',
    });

    new CloudwatchEventTarget(this, 'remove-event-target', {
      rule: eventRule.name,
      arn: sqsWithLambda.sqsQueueResource.arn,
    });

    // Allow the EventRule to invoke the SQS Queue
    new SqsQueuePolicy(this, 'sqs-queue-policy', {
      queueUrl: sqsWithLambda.sqsQueueResource.url,
      policy: JSON.stringify({
        Version: '2012-10-17',
        Statement: [
          {
            Effect: 'Allow',
            Principal: { Service: 'events.amazonaws.com' },
            Action: 'sqs:SendMessage',
            Resource: sqsWithLambda.sqsQueueResource.arn,
            Condition: { ArnEquals: { 'aws:SourceArn': eventRule.arn } },
          },
        ],
      }),
    });
  }

  private getEnvVariableValues() {
    const sentryDsn = new DataAwsSsmParameter(this, 'sentry-dsn', {
      name: `/${config.name}/${config.environment}/SENTRY_DSN`,
    });

    const serviceHash = new DataAwsSsmParameter(this, 'service-hash', {
      name: `${config.circleCIPrefix}/SERVICE_HASH`,
    });

    return { sentryDsn: sentryDsn.value, gitSha: serviceHash.value };
  }
}
