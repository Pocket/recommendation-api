import {Resource} from "cdktf";
import {Construct} from "constructs";
import {config} from "./config";
import {ApplicationDynamoDBTable, PocketVPC} from "@pocket-tools/terraform-modules";
import {PocketEventBridgeWithLambdaTarget} from "@pocket-tools/terraform-modules";
import {LAMBDA_RUNTIMES} from "@pocket-tools/terraform-modules";
import {DataAwsSecretsmanagerSecretVersion, DataAwsSsmParameter} from "@cdktf/provider-aws";
import {PocketPagerDuty} from "@pocket-tools/terraform-modules";


export class EventBridgeLambda extends Resource {
  constructor(
    scope: Construct,
    private name: string,
    candidatesTable: ApplicationDynamoDBTable,
    pagerDuty?: PocketPagerDuty
  ) {
    super(scope, name);

    const vpc = new PocketVPC(this, 'pocket-shared-vpc');

    const {sentryDsn, gitSha, metaflowSecretFqn} = this.getEnvVariableValues();

    new PocketEventBridgeWithLambdaTarget(this, 'translation-event-bridge-lambda', {
      name: `${config.prefix}-Translation`,
      lambda: {
        runtime: LAMBDA_RUNTIMES.PYTHON38,
        handler: 'aws_lambda.index.handler',
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
            resources: [
              candidatesTable.dynamodb.arn,
              `${candidatesTable.dynamodb.arn}/*`
            ]
          },
          {
            effect: 'Allow',
            actions: [
              'secretsmanager:DescribeSecret',
              'secretsmanager:GetSecretValue'
            ],
            resources: [
              'arn:aws:secretsmanager:*:*:secret:CodeBuild/Metaflow*'
            ]
          },
          {
            effect: 'Allow',
            actions: [
              's3:List*',
              's3:Get*',
            ],
            resources: [
              'arn:aws:s3:::metaflow*',
              'arn:aws:s3:::metaflow*/*'
            ]
          }
        ],
        environment: {
          RECOMMENDATION_API_CANDIDATES_TABLE: candidatesTable.dynamodb.name,
          SENTRY_DSN: sentryDsn,
          GIT_SHA: gitSha,
          ENVIRONMENT: config.environment === 'Prod' ? 'production' : 'development',
          // We are adding these metaflow required env variables here because metaflow client will not let us set these as
          // configuration/options at runtime and lambd will not let is set env vars at runtime either. So here we are...
          METAFLOW_DATASTORE_SYSROOT_S3: `\${jsondecode(${metaflowSecretFqn}.secret_string).METAFLOW_DATASTORE_SYSROOT_S3}`,
          METAFLOW_SERVICE_INTERNAL_URL: `\${jsondecode(${metaflowSecretFqn}.secret_string).METAFLOW_SERVICE_INTERNAL_URL}`
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
            actions: config.isProd ? [pagerDuty!.snsNonCriticalAlarmTopic.arn] : [],
            treatMissingData: 'breaching'
          },
          errors: {
            period: 10800, // 3 hours
            threshold: 2,
            actions: config.isProd ? [pagerDuty!.snsNonCriticalAlarmTopic.arn] : []
          }
        }
      },
      eventRule: {
        pattern: {
          "source": [
            "aws.states"
          ],
          "detail-type": [
            "Step Functions Execution Status Change"
          ],
          "detail": {
            "status": [
              "SUCCEEDED"
            ],
            "stateMachineArn": config.stateMachines.map(name => {
              return `arn:aws:states:${vpc.region}:${vpc.accountId}:stateMachine:${name}`
            })
          }
        },
        description: 'Capture Metaflow Step Functions SUCCEEDED status',
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

    // IT'S OK, don't panic!!! There's nothing SENSITIVE in this secret
    const metaflowSecret = new DataAwsSecretsmanagerSecretVersion(this, 'metaflow-secret', {
      secretId: 'CodeBuild/Metaflow'
    });

    return {sentryDsn: sentryDsn.value, gitSha: serviceHash.value, metaflowSecretFqn: metaflowSecret.fqn};
  }
}
