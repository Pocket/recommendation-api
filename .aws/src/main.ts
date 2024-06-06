import {Construct} from 'constructs';
import {App, DataTerraformRemoteState, S3Backend, TerraformStack} from 'cdktf';

import {config} from './config';
import {DynamoDB} from "./dynamodb";
import {PocketALBApplication, PocketECSCodePipeline} from "@pocket-tools/terraform-modules";
import {SqsLambda} from "./sqsLambda";
import {Elasticache} from "./elasticache";
import {RecommendationApiSynthetics} from './monitoring';

import {ArchiveProvider} from '@cdktf/provider-archive/lib/provider';
import {AwsProvider} from '@cdktf/provider-aws/lib/provider';
import {DataAwsCallerIdentity} from '@cdktf/provider-aws/lib/data-aws-caller-identity';
import {DataAwsKmsAlias} from '@cdktf/provider-aws/lib/data-aws-kms-alias';
import {DataAwsRegion} from '@cdktf/provider-aws/lib/data-aws-region';
import {LocalProvider} from '@cdktf/provider-local/lib/provider';
import {NullProvider} from '@cdktf/provider-null/lib/provider';

class RecommendationAPI extends TerraformStack {
    constructor(scope: Construct, name: string) {
        super(scope, name);

        // Create providers
        new AwsProvider(this, 'aws', {
          region: 'us-east-1',
          defaultTags: [{ tags: config.tags }],
        });
        new LocalProvider(this, 'local_provider');
        new NullProvider(this, 'null_provider');
        new ArchiveProvider(this, 'archive_provider');

        new S3Backend(this, {
          bucket: `mozilla-content-team-${config.environment.toLowerCase()}-terraform-state`,
          dynamodbTable: `mozilla-content-team-${config.environment.toLowerCase()}-terraform-state`,
          key: config.name,
          region: 'us-east-1',
        });

        const region = new DataAwsRegion(this, 'region');
        const caller = new DataAwsCallerIdentity(this, 'caller');

        const dynamodb = new DynamoDB(this, 'dynamodb');

        const pocketApp = this.createPocketAlbApplication({
            secretsManagerKmsAlias: this.getSecretsManagerKmsAlias(),
            region,
            caller,
            elasticache: new Elasticache(this, 'elasticache'),
            dynamodb: dynamodb
        });

        this.createApplicationCodePipeline(pocketApp);

        const synthetic = new RecommendationApiSynthetics(this, 'synthetics');
        synthetic.createSyntheticCheck([]);

        new SqsLambda(this, 'sqs-lambda', dynamodb.candidateSetsTable);
    }


    /**
     * Get secrets manager kms alias
     * @private
     */
    private getSecretsManagerKmsAlias() {
        return new DataAwsKmsAlias(this, 'kms_alias', {
            name: 'alias/aws/secretsmanager'
        });
    }

    /**
     * Create CodePipeline to build and deploy terraform and ecs
     * @param app
     * @private
     */
    private createApplicationCodePipeline(app: PocketALBApplication) {
        new PocketECSCodePipeline(this, 'code-pipeline', {
            prefix: config.prefix,
            source: {
                codeStarConnectionArn: config.codePipeline.githubConnectionArn,
                repository: config.codePipeline.repository,
                branchName: config.codePipeline.branch
            }
        });
    }

    /**
     * Create ECS Application
     * @param dependencies
     * @private
     */
    private createPocketAlbApplication(dependencies: {
        region: DataAwsRegion;
        caller: DataAwsCallerIdentity;
        secretsManagerKmsAlias: DataAwsKmsAlias;
        dynamodb: DynamoDB;
        elasticache: Elasticache;
    }) {

        const {region, caller, secretsManagerKmsAlias, dynamodb, elasticache} =
            dependencies;
        return new PocketALBApplication(this, 'application', {
          internal: true,
          prefix: config.prefix,
          alb6CharacterPrefix: config.shortName,
          cdn: false,
          domain: config.domain,
          taskSize: {
            cpu: 4096,
            memory: 12288,
          },
          containerConfigs: [
            {
              name: 'app',
              portMappings: [
                {
                  hostPort: 8000,
                  containerPort: 8000,
                },
              ],
              healthCheck: {
                command: [
                  'CMD-SHELL',
                  'curl -f http://localhost:8000/health-check || exit 1',
                ],
                interval: 15,
                retries: 3,
                timeout: 5,
                startPeriod: 60,
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
                {
                  name: 'OTEL_INSTRUMENTATION_HTTP_CAPTURE_HEADERS_SERVER_REQUEST',
                  value: '.*',
                },
                {
                  name: 'OTEL_INSTRUMENTATION_HTTP_CAPTURE_HEADERS_SANITIZE_FIELDS',
                  value: 'Jwt,Authorization,.*session.*,set-cookie',
                },
              ],
              secretEnvVars: [
                {
                  name: 'SENTRY_DSN',
                  valueFrom: `arn:aws:ssm:${region.name}:${caller.accountId}:parameter/${config.name}/${config.environment}/SENTRY_DSN`,
                },
              ],
            },
            {
              name: 'aws-ot-collector',
              containerImage:
                'public.ecr.aws/aws-observability/aws-otel-collector:latest',
              portMappings: [
                {
                  hostPort: 4317, // grcp port for receiving spans
                  containerPort: 4317,
                },
                {
                  hostPort: 13133, // health_check
                  containerPort: 13133,
                },
              ],
              command: ['--config=/etc/ecs/ecs-default-config.yaml'],
            },
          ],
          codeDeploy: {
            useCodeDeploy: true,
            useCodePipeline: true,
          },
          exposedContainer: {
            name: 'app',
            port: 8000,
            healthCheckPath: '/health-check',
          },
          ecsIamConfig: {
            prefix: config.prefix,
            taskExecutionRolePolicyStatements: [
              //This policy could probably go in the shared module in the future.
              {
                actions: ['secretsmanager:GetSecretValue', 'kms:Decrypt'],
                resources: [
                  `arn:aws:secretsmanager:${region.name}:${caller.accountId}:secret:Shared`,
                  `arn:aws:secretsmanager:${region.name}:${caller.accountId}:secret:Shared/*`,
                  secretsManagerKmsAlias.targetKeyArn,
                ],
                effect: 'Allow',
              },
              {
                actions: ['ssm:GetParameter*'],
                resources: [
                  `arn:aws:ssm:${region.name}:${caller.accountId}:parameter/${config.name}/${config.environment}`,
                  `arn:aws:ssm:${region.name}:${caller.accountId}:parameter/${config.name}/${config.environment}/*`,
                ],
                effect: 'Allow',
              },
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
                  `${dynamodb.candidateSetsTable.dynamodb.arn}/*`,
                ],
                effect: 'Allow',
              },
              {
                actions: [
                  'sagemaker:PutRecord',
                  'sagemaker:BatchGetRecord',
                  'sagemaker:GetRecord',
                  'sagemaker:DescribeFeatureGroup',
                ],
                resources: ['*'],
                effect: 'Allow',
              },
              {
                actions: [
                  'xray:PutTraceSegments',
                  'xray:PutTelemetryRecords',
                  'xray:GetSamplingRules',
                  'xray:GetSamplingTargets',
                  'xray:GetSamplingStatisticSummaries',
                ],
                resources: ['*'],
                effect: 'Allow',
              },
            ],
            taskExecutionDefaultAttachmentArn:
              'arn:aws:iam::aws:policy/service-role/AmazonECSTaskExecutionRolePolicy',
          },

          autoscalingConfig: {
            targetMinCapacity: config.environment === 'Prod' ? 4 : 1,
            targetMaxCapacity: config.environment === 'Prod' ? 10 : 10,
          },
          alarms: {
            http5xxErrorPercentage: {
              // This will go off if the 5xx errors exceed 25% of the total request over
              // a period of 20 minutes after 4 evaluation periods of 5 mins each.
              threshold: 25, // This is a percentage
              evaluationPeriods: 4,
              period: 300, // 5 mins
              alarmDescription:
                'Runbook: https://getpocket.atlassian.net/l/c/sfMGntZ0',
            },
            httpLatency: {
              // If the latency is greater than 500 ms for 1 hour continuously i.e
              // breaches the threshold 4 times every 15 minutes,
              // this will go off
              period: 900,
              evaluationPeriods: 4,
              threshold: 0.5, // 500ms
              alarmDescription:
                'Runbook: https://getpocket.atlassian.net/l/c/dChZ24T1',
            },
          },
        });
    }

}

const app = new App();
new RecommendationAPI(app, 'recommendation-api');
app.synth();
