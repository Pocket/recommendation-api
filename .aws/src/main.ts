import {Construct} from 'constructs';
import {App, RemoteBackend, TerraformStack} from 'cdktf';
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

class ExploreTopics extends TerraformStack {
    constructor(scope: Construct, name: string) {
        super(scope, name);

        new AwsProvider(this, 'aws', {
            region: 'us-east-1',
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
                            name: 'EXPLORE_TOPICS_METADATA_TABLE',
                            value: dynamodb.metadataTable.dynamodb.name
                        },
                        {
                            name: 'EXPLORE_TOPICS_CANDIDATES_TABLE',
                            value: dynamodb.candidatesTable.dynamodb.name
                        }
                    ]
                }
            ],
            codeDeploy: {
                useCodeDeploy: true,
                // Disabling because of module bug atm.. and unique names..
                //snsNotificationTopicArn: snsTopic.arn,
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
                    }
                ],
                taskExecutionDefaultAttachmentArn: 'arn:aws:iam::aws:policy/service-role/AmazonECSTaskExecutionRolePolicy',
            }
        })
    }
}

const app = new App();
new ExploreTopics(app, 'explore-topics');
app.synth();
