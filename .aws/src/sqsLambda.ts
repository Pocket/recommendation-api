import { Construct } from 'constructs';
import { config } from './config';
import {
  ApplicationDynamoDBTable,
  PocketVPC,
} from '@pocket-tools/terraform-modules';
import { PocketSQSWithLambdaTarget } from '@pocket-tools/terraform-modules';
import { LAMBDA_RUNTIMES } from '@pocket-tools/terraform-modules';
import { DataAwsSsmParameter } from '@cdktf/provider-aws/lib/data-aws-ssm-parameter';

export class SqsLambda extends Construct {
  constructor(
    scope: Construct,
    private name: string,
    candidateSetsTable: ApplicationDynamoDBTable,
  ) {
    super(scope, name);

    const vpc = new PocketVPC(this, 'pocket-shared-vpc');

    const { sentryDsn, gitSha } = this.getEnvVariableValues();

    new PocketSQSWithLambdaTarget(this, 'translation-sqs-lambda', {
      name: `${config.prefix}-Sqs-Translation`,
      /* batchSize is set to 25 because DynamoDB allows 25 put requests per BatchWriteItem. */
      batchSize: 25,
      batchWindow: 60,
      sqsQueue: {
        maxReceiveCount: 3,
        visibilityTimeoutSeconds: 300,
      },
      lambda: {
        runtime: 'python3.9' as LAMBDA_RUNTIMES,
        handler: 'aws_lambda.sqs_handler.handler',
        timeout: 120,
        executionPolicyStatements: [
          {
            effect: 'Allow',
            actions: [
              'dynamodb:BatchWriteItem',
              'dynamodb:PutItem',
              'dynamodb:DescribeTable',
              'dynamodb:UpdateItem',
            ],
            resources: [
              candidateSetsTable.dynamodb.arn,
              `${candidateSetsTable.dynamodb.arn}/*`,
            ],
          },
        ],
        environment: {
          RECOMMENDATION_API_CANDIDATE_SETS_TABLE:
            candidateSetsTable.dynamodb.name,
          SENTRY_DSN: sentryDsn,
          GIT_SHA: gitSha,
          ENVIRONMENT:
            config.environment === 'Prod' ? 'production' : 'development',
        },
        vpcConfig: {
          securityGroupIds: vpc.internalSecurityGroups.ids,
          subnetIds: vpc.privateSubnetIds,
        },
        codeDeploy: {
          region: vpc.region,
          accountId: vpc.accountId,
        },
      },
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
