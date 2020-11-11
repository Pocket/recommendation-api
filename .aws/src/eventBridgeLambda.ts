import {TerraformStack} from "cdktf";
import {Construct} from "constructs";
import {config as defaultConfig} from "./config";
import {ApplicationDynamoDBTable, PocketVPC} from "@pocket/terraform-modules";
import {PocketEventBridgeWithLambdaTarget} from "@pocket/terraform-modules/dist/src/pocket/PocketEventBridgeWithLambdaTarget";
import {LAMBDA_RUNTIMES} from "@pocket/terraform-modules/dist/src/base/ApplicationVersionedLambda";
import {DataAwsSsmParameter} from "../.gen/providers/aws";

interface EventBridgeLambdaProps {
  candidatesTable: ApplicationDynamoDBTable
}

export class EventBridgeLambda extends TerraformStack {
  constructor(private scope: Construct, private name: string, config: EventBridgeLambdaProps) {
    super(scope, name);

    const vpc = new PocketVPC(this, 'pocket-shared-vpc');

    const {sentryDsn, gitSha} = this.getEnvVariableValues();

    new PocketEventBridgeWithLambdaTarget(this, 'translation-event-bridge-lambda', {
      name: `${defaultConfig.prefix}-Translation`,
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
          "stateMachineArn": defaultConfig.stateMachines.map(name => {
            return `arn:aws:states:${vpc.region}:${vpc.accountId}:stateMachine:${name}`
          })
        }
      },
      ruleDescription: 'Capture Metaflow Step Functions SUCCEEDED status',
      runtime: LAMBDA_RUNTIMES.PYTHON38,
      handler: 'index.handler',
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
            config.candidatesTable.dynamodb.arn,
            `${config.candidatesTable.dynamodb.arn}/*`
          ]
        }
      ],
      environment: {
        EXPLORE_TOPICS_CANDIDATES_TABLE: config.candidatesTable.dynamodb.name,
        SENTRY_DSN: sentryDsn,
        GIT_SHA: gitSha,
        ENVIRONMENT: defaultConfig.environment === 'Prod' ? 'production' : 'development'
      },
      vpcConfig: {
        securityGroupIds: vpc.defaultSecurityGroups.ids,
        subnetIds: vpc.privateSubnetIds
      },
      tags: defaultConfig.tags,
      codeDeploy: {
        region: vpc.region,
        accountId: vpc.accountId,
      }
    });
  }

  private getEnvVariableValues() {
    const sentryDsn = new DataAwsSsmParameter(this, 'sentry-dsn', {
      name: `/${defaultConfig.name}/${defaultConfig.environment}/SENTRY_DSN`
    });

    const serviceHash = new DataAwsSsmParameter(this, 'service-hash', {
      name: `${defaultConfig.circleCIPrefix}/SERVICE_HASH`
    });

    return {sentryDsn: sentryDsn.value, gitSha: serviceHash.value};
  }
}
