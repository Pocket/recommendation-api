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
import {SqsLambda} from "./sqsLambda";
import {Elasticache} from "./elasticache";

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

    const isProd : boolean = config.environment === "Prod";

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
      },
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

    const elasticache = new Elasticache(this, 'elasticache')

    new PocketALBApplication(this, 'application', {
      internal: true,
      prefix: config.prefix,
      alb6CharacterPrefix: config.shortName,
      tags: config.tags,
      cdn: false,
      domain: config.domain,
      taskSize: {
        cpu: 2048,
        memory: 4096,
      },
      containerConfigs: [
        {
          name: 'app',
          portMappings: [
            {
              hostPort: 8000,
              containerPort: 8000,
            }
          ],
          healthCheck: {
            command: ["CMD-SHELL", "curl -f http://localhost:8000/health-check || exit 1" ],
            interval: 15,
            retries: 3,
            timeout: 5,
            startPeriod: 0,
          },
          envVars: [
            {
              name: 'ENVIRONMENT',
              value: process.env.NODE_ENV, // this gives us a nice lowercase production and development
            },
            {
              name: 'AWS_DYNAMODB_ENDPOINT_URL',
              value: `https://dynamodb.${region.name}.amazonaws.com`,
            },
            {
              name: 'RECOMMENDATION_API_METADATA_TABLE',
              value: dynamodb.metadataTable.dynamodb.name,
            },
            {
              name: 'RECOMMENDATION_API_CANDIDATES_TABLE',
              value: dynamodb.candidatesTable.dynamodb.name,
            },
            {
              name: 'MODELD_RECOMMENDATION_METRICS_TABLE',
              value: dynamodb.recommendationMetricsTable.name,
            },
            {
              name: 'MODELD_RECOMMENDATION_METRICS_PK',
              value: dynamodb.recommendationMetricsTable.hashKey,
            },
            {
              name: 'MODELD_SLATE_METRICS_TABLE',
              value: dynamodb.slateMetricsTable.name,
            },
            {
              name: 'MODELD_SLATE_METRICS_PK',
              value: dynamodb.slateMetricsTable.hashKey,
            },
            {
              name: 'RECOMMENDATION_API_CANDIDATE_SETS_TABLE',
              value: dynamodb.candidateSetsTable.dynamodb.name,
            },
            {
              name: 'MEMCACHED_SERVERS',
              value: elasticache.nodeList.join(','),
            },
          ],
          secretEnvVars: [
            {
              name: 'SENTRY_DSN',
              valueFrom: `arn:aws:ssm:${region.name}:${caller.accountId}:parameter/${config.name}/${config.environment}/SENTRY_DSN`
            },
          ],
        },
        {
          name: 'xray-daemon',
          containerImage: 'amazon/aws-xray-daemon',
          portMappings: [
            {
              hostPort: 2000,
              containerPort: 2000,
              protocol: 'udp',
            },
          ],
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
          },
          {
            actions: [
              "ssm:GetParameter*"
            ],
            resources: [
              `arn:aws:ssm:${region.name}:${caller.accountId}:parameter/${config.name}/${config.environment}`,
              `arn:aws:ssm:${region.name}:${caller.accountId}:parameter/${config.name}/${config.environment}/*`,
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
              dynamodb.recommendationMetricsTable.arn,
              dynamodb.slateMetricsTable.arn,
              dynamodb.candidateSetsTable.dynamodb.arn,
              `${dynamodb.candidatesTable.dynamodb.arn}/*`,
              `${dynamodb.metadataTable.dynamodb.arn}/*`,
              `${dynamodb.recommendationMetricsTable.arn}/*`,
              `${dynamodb.slateMetricsTable.arn}/*`,
              `${dynamodb.candidateSetsTable.dynamodb.arn}/*`
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
       http5xxErrorPercentage: {
          // This will go off if the 5xx errors exceed 25% of the total request over
          // a period of 20 minutes after 4 evaluation periods of 5 mins each.
          threshold: 25, // This is a percentage
          evaluationPeriods: 4,
          period: 300, // 5 mins
          actions: isProd ? [pagerDuty.snsCriticalAlarmTopic.arn] : [],
        },
        httpLatency: {
          // If the latency is greater than 150 ms for 1 hour continuously i.e
          // breaches the threshold 4 times every 15 minutes,
          // this will go off
          period: 900,
          evaluationPeriods: 4,
          threshold: 0.15, // 150ms
          actions: isProd ? [pagerDuty.snsNonCriticalAlarmTopic.arn] : [],
        },
      }
    });

    new EventBridgeLambda(this, 'event-bridge-lambda', dynamodb.candidatesTable, pagerDuty);
    new SqsLambda(this, 'sqs-lambda', dynamodb.candidateSetsTable, pagerDuty);
  }
}

const app = new App();
new RecommendationAPI(app, 'recommendation-api');
app.synth();
