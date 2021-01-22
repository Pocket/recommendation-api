import {Construct} from 'constructs';
import {App, DataTerraformRemoteState, RemoteBackend, TerraformStack} from 'cdktf';
import {
  AwsProvider,
  DataAwsCallerIdentity,
  DataAwsKmsAlias,
  DataAwsRegion,
  DataAwsSnsTopic
} from '../.gen/providers/aws';
import {config} from './config';
import {DynamoDB} from "./dynamodb";
import {PocketALBApplication} from "@pocket/terraform-modules";
import {EventBridgeLambda} from "./eventBridgeLambda";
import {PocketPagerDuty} from "@pocket/terraform-modules/dist/src/pocket/PocketPagerDuty";
import {PagerdutyProvider} from "../.gen/providers/pagerduty";

class RecommendationAPI extends TerraformStack {
  constructor(scope: Construct, name: string) {
    super(scope, name);

    new AwsProvider(this, 'aws', {
      region: 'us-east-1',
    });

    new PagerdutyProvider(this, 'pagerduty_provider', {
      token: undefined
    });

    new RemoteBackend(this, {
      hostname: 'app.terraform.io',
      organization: 'Pocket',
      workspaces: [
        {
          prefix: `${config.name}-`,
        },
      ],
    });

    const incidentManagement = new DataTerraformRemoteState(this, 'incident_management', {
      organization: 'Pocket',
      workspaces: {
        name: 'incident-management'
      }
    });

    const pagerDuty = new PocketPagerDuty(this, 'pagerduty', {
      prefix: config.prefix,
      service: {
        criticalEscalationPolicyId: incidentManagement.get('policy_backend_critical_id'),
        nonCriticalEscalationPolicyId: incidentManagement.get('policy_backend_non_critical_id')
      }
    })

    const region = new DataAwsRegion(this, 'region');
    const caller = new DataAwsCallerIdentity(this, 'caller');
    const secretsManager = new DataAwsKmsAlias(this, 'kms_alias', {
      name: 'alias/aws/secretsmanager'
    });

    const snsTopic = new DataAwsSnsTopic(this, 'backend_notifications', {
      name: `Backend-${config.environment}-ChatBot`
    })

    const dynamodb = new DynamoDB(this, 'dynamodb');

    new PocketALBApplication(this, 'application', {
      internal: true,
      prefix: config.prefix,
      alb6CharacterPrefix: config.shortName,
      tags: config.tags,
      cdn: false,
      domain: config.domain,
      containerConfigs: [
        {
          name: 'app',
          hostPort: 8000,
          containerPort: 8000,
          envVars: [
            {
              name: 'ENVIRONMENT',
              value: process.env.NODE_ENV, // this gives us a nice lowercase production and development
            },
            {
              name: 'AWS_DYNAMODB_ENDPOINT_URL',
              value: `https://dynamodb.${region.name}.amazonaws.com`
            },
            {
              name: 'RECOMMENDATION_API_METADATA_TABLE',
              value: dynamodb.metadataTable.dynamodb.name
            },
            {
              name: 'RECOMMENDATION_API_CANDIDATES_TABLE',
              value: dynamodb.candidatesTable.dynamodb.name
            }
          ]
        },
        {
          name: 'xray-daemon',
          containerImage: 'amazon/aws-xray-daemon',
          hostPort: 2000,
          containerPort: 2000,
          protocol: 'udp',
          command: ['--region', 'us-east-1', '--local-mode'],
        }
      ],
      codeDeploy: {
        useCodeDeploy: true,
        snsNotificationTopicArn: snsTopic.arn,
      },
      exposedContainer: {
        name: 'app',
        port: 8000,
        healthCheckPath: '/health-check'
      },
      ecsIamConfig: {
        prefix: config.prefix,
        taskExecutionRolePolicyStatements: [
          //This policy could probably go in the shared module in the future.
          {
            actions: [
              'secretsmanager:GetSecretValue',
              'kms:Decrypt'
            ],
            resources: [
              `arn:aws:secretsmanager:${region.name}:${caller.accountId}:secret:Shared`,
              `arn:aws:secretsmanager:${region.name}:${caller.accountId}:secret:Shared/*`,
              secretsManager.targetKeyArn
            ],
            effect: 'Allow'
          }
        ],
        taskRolePolicyStatements: [
          {
            actions: [
              'dynamodb:BatchGet*',
              'dynamodb:DescribeTable',
              'dynamodb:Get*',
              'dynamodb:Query',
              'dynamodb:Scan',
            ],
            resources: [
              dynamodb.candidatesTable.dynamodb.arn,
              dynamodb.metadataTable.dynamodb.arn,
              `${dynamodb.candidatesTable.dynamodb.arn}/*`,
              `${dynamodb.metadataTable.dynamodb.arn}/*`,
            ],
            effect: 'Allow'
          },
          {
            actions: [
              'xray:PutTraceSegments',
              'xray:PutTelemetryRecords',
              'xray:GetSamplingRules',
              'xray:GetSamplingTargets',
              'xray:GetSamplingStatisticSummaries'
            ],
            resources: ['*'],
            effect: 'Allow'
          }


        ],
        taskExecutionDefaultAttachmentArn: 'arn:aws:iam::aws:policy/service-role/AmazonECSTaskExecutionRolePolicy',
      },

      autoscalingConfig: {
        targetMinCapacity: 2,
        targetMaxCapacity: 10
      },
      alarms: {
        http5xxError: {
          threshold: 10,
          evaluationPeriods: 2,
          period: 600,
          actions: [pagerDuty.snsCriticalAlarmTopic.arn]
        },
        httpLatency: {
          evaluationPeriods: 2,
          threshold: 500,
          actions: [pagerDuty.snsCriticalAlarmTopic.arn]
        },
        httpRequestCount: {
          threshold: 5000,
          evaluationPeriods: 2,
          actions: [pagerDuty.snsCriticalAlarmTopic.arn]
        }
      }
    });

    new EventBridgeLambda(this, 'event-bridge-lambda', dynamodb.candidatesTable, pagerDuty);
  }
}

const app = new App();
new RecommendationAPI(app, 'recommendation-api');
app.synth();
