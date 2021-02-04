import {Resource} from "cdktf";
import {Construct} from "constructs";
import {config} from "./config";
import {ApplicationDynamoDBTable, PocketVPC} from "@pocket/terraform-modules";
import {PocketSQSWithLambdaTarget} from "@pocket/terraform-modules/dist/src/pocket/PocketSQSWithLambdaTarget";
import {LAMBDA_RUNTIMES} from "@pocket/terraform-modules/dist/src/base/ApplicationVersionedLambda";
import {DataAwsSecretsmanagerSecretVersion, DataAwsSsmParameter} from "../.gen/providers/aws";
import {PocketPagerDuty} from "@pocket/terraform-modules/dist/src/pocket/PocketPagerDuty";


export class SqsLambda extends Resource {
  constructor(
    scope: Construct,
    private name: string,
    candidatesTable: ApplicationDynamoDBTable,
    pagerDuty: PocketPagerDuty
  ) {
    super(scope, name);

    const vpc = new PocketVPC(this, 'pocket-shared-vpc');

    const {sentryDsn, gitSha} = this.getEnvVariableValues();

    new PocketSQSWithLambdaTarget(this, 'translation-sqs-lambda', {
      name: `${config.prefix}-Sqs-Translation`,
      batchSize: 100,
      batchWindow: 60,
      sqsQueue: {
        maxReceiveCount: 3,
        visibilityTimeoutSeconds: 300,
      },
      lambda: {
        runtime: LAMBDA_RUNTIMES.PYTHON38,
        handler: 'aws_lambda.index.handler_v2',
        timeout: 30,
        executionPolicyStatements: [
          {
            effect: 'Allow',
            actions: [
              'dynamodb:BatchWriteItem',
              'dynamodb:PutItem',
              'dynamodb:DescribeTable',
              'dynamodb:UpdateItem'
            ],
            /* TODO: Change this to candidate set dynamodb resource once ready. */
            resources: [
              candidatesTable.dynamodb.arn,
              `${candidatesTable.dynamodb.arn}/*`
            ]
          }
        ],
        environment: {
          RECOMMENDATION_API_CANDIDATES_TABLE: candidatesTable.dynamodb.name,
          SENTRY_DSN: sentryDsn,
          GIT_SHA: gitSha,
          ENVIRONMENT: config.environment === 'Prod' ? 'production' : 'development',
        },
        vpcConfig: {
          securityGroupIds: vpc.defaultSecurityGroups.ids,
          subnetIds: vpc.privateSubnetIds
        },
        codeDeploy: {
          region: vpc.region,
          accountId: vpc.accountId,
        },
        alarms: {
          invocations: {
            period: 10800, // 3 hours
            threshold: 1,
            comparisonOperator: 'LessThanThreshold',
            actions: [pagerDuty.snsNonCriticalAlarmTopic.arn],
            treatMissingData: 'breaching'
          },
          errors: {
            period: 10800, // 3 hours
            threshold: 2,
            actions: [pagerDuty.snsNonCriticalAlarmTopic.arn]
          }
        }
      },
      tags: config.tags,
    });
  }

  private getEnvVariableValues() {
    const sentryDsn = new DataAwsSsmParameter(this, 'sentry-dsn', {
      name: `/${config.name}/${config.environment}/SENTRY_DSN`
    });

    const serviceHash = new DataAwsSsmParameter(this, 'service-hash', {
      name: `${config.circleCIPrefix}/SERVICE_HASH`
    });

    return {sentryDsn: sentryDsn.value, gitSha: serviceHash.value};
  }
}
