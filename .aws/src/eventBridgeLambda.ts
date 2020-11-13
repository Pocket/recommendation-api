import {TerraformStack} from "cdktf";
import {Construct} from "constructs";
import {config} from "./config";
import {ApplicationDynamoDBTable, PocketVPC} from "@pocket/terraform-modules";
import {PocketEventBridgeWithLambdaTarget} from "@pocket/terraform-modules/dist/src/pocket/PocketEventBridgeWithLambdaTarget";
import {LAMBDA_RUNTIMES} from "@pocket/terraform-modules/dist/src/base/ApplicationVersionedLambda";
import {DataAwsSsmParameter} from "../.gen/providers/aws";


export class EventBridgeLambda extends TerraformStack {
  constructor(private scope: Construct, private name: string, candidatesTable: ApplicationDynamoDBTable) {
    super(scope, name);

    const vpc = new PocketVPC(this, 'pocket-shared-vpc');

    const {sentryDsn, gitSha} = this.getEnvVariableValues();

    new PocketEventBridgeWithLambdaTarget(this, 'translation-event-bridge-lambda', {
      name: `${config.prefix}-Translation`,
      eventPattern: {
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
      ruleDescription: 'Capture Metaflow Step Functions SUCCEEDED status',
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
        EXPLORE_TOPICS_CANDIDATES_TABLE: candidatesTable.dynamodb.name,
        SENTRY_DSN: sentryDsn,
        GIT_SHA: gitSha,
        ENVIRONMENT: config.environment === 'Prod' ? 'production' : 'development'
      },
      vpcConfig: {
        securityGroupIds: vpc.defaultSecurityGroups.ids,
        subnetIds: vpc.privateSubnetIds
      },
      tags: config.tags,
      codeDeploy: {
        region: vpc.region,
        accountId: vpc.accountId,
      }
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
