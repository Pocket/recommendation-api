import {TerraformStack} from "cdktf";
import {Construct} from "constructs";
import {config} from "./config";
import {
    CloudwatchEventRule,
    CloudwatchEventTarget, CloudwatchLogGroup,
    CodedeployApp,
    CodedeployDeploymentGroup,
    CodestarnotificationsNotificationRule,
    DataAwsCallerIdentity,
    DataAwsIamPolicyDocument,
    DataAwsRegion, DataAwsSnsTopic,
    IamRole,
    IamRolePolicy,
    IamRolePolicyAttachment,
    LambdaAlias,
    LambdaFunction,
    LambdaPermission,
    S3Bucket,
    S3BucketPublicAccessBlock
} from "../.gen/providers/aws";
import {PocketVPC} from "@pocket/terraform-modules";
import {DataArchiveFile} from "@pocket/terraform-modules/dist/.gen/providers/archive";

export class EventBridgeLambda extends TerraformStack {
    private region: DataAwsRegion;
    private callerIdentity: DataAwsCallerIdentity;

    constructor(private scope: Construct, private name: string) {
        super(scope, name);

        this.region = new DataAwsRegion(this, 'current-region');
        this.callerIdentity = new DataAwsCallerIdentity(this, 'current-identity');

        const lambda = this.createLambdaFunction();
        this.setupLambdaResourcePermission(lambda, this.createCloudwatchEventRule(lambda));
        this.setupLambdaCodeDeploy();
    }

    private setupLambdaResourcePermission(lambda: LambdaAlias, rule: CloudwatchEventRule) {
        new LambdaPermission(this, 'lambda-permission', {
            action: 'lambda:InvokeFunction',
            functionName: lambda.functionName,
            principal: 'events.amazonaws.com',
            sourceArn: rule.arn,
            dependsOn: [lambda, rule]
        });
    }

    private setupLambdaCodeDeploy() {
        const lambdaCodeDeployApp = new CodedeployApp(this, 'lambda-translation-code-deploy-app', {
            name: `${config.prefix}-Translation`,
            computePlatform: 'Lambda'
        });

        this.createCodeDeploymentGroup(lambdaCodeDeployApp);
        this.setupCodeDeployNotifications(lambdaCodeDeployApp);
        this.createLambdaCodeBucket();
    }

    private createCodeDeploymentGroup(lambdaCodeDeployApp: CodedeployApp) {
        new CodedeployDeploymentGroup(this, 'lambda-code-deployment-group', {
            appName: lambdaCodeDeployApp.name,
            deploymentConfigName: 'CodeDeployDefault.LambdaAllAtOnce',
            deploymentGroupName: `${config.prefix}-Translation`,
            serviceRoleArn: this.getCodeDeployRole().arn,
            deploymentStyle: [
                {
                    deploymentType: 'BLUE_GREEN',
                    deploymentOption: 'WITH_TRAFFIC_CONTROL'
                }
            ],
            autoRollbackConfiguration: [
                {
                    enabled: true,
                    events: ['DEPLOYMENT_FAILURE']
                }
            ]
        });
    }

    private getCodeDeployRole() {
        const codeDeployRole = new IamRole(this, 'lambda-code-deploy-role', {
            name: `${config.prefix}-LambdaCodeDeployRole`,
            assumeRolePolicy: this.getCodeDeployAssumePolicyDocument().json
        });

        new IamRolePolicyAttachment(this, 'lambda-code-deploy-policy-attachment', {
            policyArn: 'arn:aws:iam::aws:policy/service-role/AWSCodeDeployRoleForLambda',
            role: codeDeployRole.name
        });

        return codeDeployRole;
    }

    private getCodeDeployAssumePolicyDocument() {
        return new DataAwsIamPolicyDocument(this, 'code-deploy-assume-role-policy-document', {
            statement: [
                {
                    effect: 'Allow',
                    actions: ['sts:AssumeRole'],
                    principals: [
                        {
                            identifiers: ['codedeploy.amazonaws.com'],
                            type: 'Service'
                        }
                    ]
                }
            ]
        });
    }

    private setupCodeDeployNotifications(lambdaCodeDeployApp: CodedeployApp) {
        const backendDeployTopic = new DataAwsSnsTopic(this, 'backend-deploy-topic', {
            name: `Backend-${config.environment}-ChatBot`
        });

        new CodestarnotificationsNotificationRule(this, 'lambda-metaflow-notifications', {
            detailType: 'BASIC',
            eventTypeIds: ['codedeploy-application-deployment-failed'],
            name: lambdaCodeDeployApp.name,
            resource: `arn:aws:codedeploy:${this.region.name}:${this.callerIdentity.accountId}:application:${lambdaCodeDeployApp.name}`,
            target: [
                {
                    address: backendDeployTopic.arn
                }
            ]
        });
    }

    private createLambdaCodeBucket() {
        const codeBucket = new S3Bucket(this, 'lambda-translation-code-bucket', {
            bucket: `pocket-${config.prefix.toLowerCase()}-translation`,
            acl: 'private',
            tags: config.tags
        });

        new S3BucketPublicAccessBlock(this, 'lambda-translation-code-bucket-public-access-block', {
            bucket: codeBucket.id,
            blockPublicAcls: true,
            blockPublicPolicy: true
        });
    }

    private createLambdaFunction() {
        const lambdaExecutionRole = new IamRole(this, 'lambda-execution-role', {
            name: `${config.prefix}-TranslationLambdaExecutionRole`,
            assumeRolePolicy: this.getLambdaAssumePolicyDocument().json,
        });

        new IamRolePolicy(this, 'lambda-execution-role-policy', {
            name: `${config.prefix}-TranslationLambdaExecutionRolePolicy`,
            policy: this.getLambdaExecutionPolicyDocument().json,
            role: lambdaExecutionRole.name
        })

        const vpc = new PocketVPC(this, 'pocket-shared-vpc');

        const defaultLambda = this.getLambdaDefault();
        const lambda = new LambdaFunction(this, 'lambda-translation', {
            functionName: `${config.prefix}-Translation`,
            filename: defaultLambda.outputPath,
            handler: 'index.lambda_handler',
            runtime: 'python3.8',
            sourceCodeHash: defaultLambda.outputBase64Sha256,
            role: lambdaExecutionRole.arn,
            vpcConfig: [{
                securityGroupIds: vpc.defaultSecurityGroups.ids,
                subnetIds: vpc.privateSubnetIds
            }],
            publish: true,
            lifecycle: {
                ignoreChanges: [
                    'filename',
                    'source_code_hash'
                ]
            },
            tags: config.tags
        });

        new CloudwatchLogGroup(this, 'lambda-log-group', {
            name: `/aws/lambda/${lambda.functionName}`,
            retentionInDays: 14,
            dependsOn: [lambda]
        });

        const lambdaAlias = new LambdaAlias(this, 'lambda-alias', {
            functionName: lambda.functionName,
            functionVersion: lambda.version,
            name: 'DEPLOYED',
            lifecycle: {
                ignoreChanges: ['function_version']
            },
            dependsOn: [lambda]
        });

        lambdaAlias.addOverride('function_version', `split(":", ${lambda.qualifiedArn})[7]`);

        return lambdaAlias;
    }

    private getLambdaAssumePolicyDocument() {
        return new DataAwsIamPolicyDocument(this, 'lambda-assume-policy-document', {
            version: '2012-10-17',
            statement: [{
                effect: 'Allow',
                actions: ['sts:AssumeRole'],
                principals: [
                    {
                        identifiers: ['lambda.amazonaws.com'],
                        type: 'Service'
                    }
                ]
            }]
        });
    }

    private getLambdaExecutionPolicyDocument() {
        return new DataAwsIamPolicyDocument(this, 'lambda-execution-policy-document', {
            version: '2012-10-17',
            statement: [
                {
                    effect: 'Allow',
                    actions: [
                        'logs:CreateLogGroup',
                        'logs:CreateLogStream',
                        'logs:PutLogEvents',
                        'logs:DescribeLogStreams'
                    ],
                    resources: [
                        'arn:aws:logs:*:*:*'
                    ]
                },
                {
                    effect: "Allow",
                    actions: [
                        'ec2:DescribeNetworkInterfaces',
                        'ec2:CreateNetworkInterface',
                        'ec2:DeleteNetworkInterface',
                        'ec2:DescribeInstances',
                        'ec2:AttachNetworkInterface'
                    ],
                    resources: ['*']
                }
            ]
        });
    }

    private createCloudwatchEventRule(lambda: LambdaAlias) {
        const rule = new CloudwatchEventRule(this, 'step-function-event-bridge-rule', {
            name: `${config.prefix}-StepFunctionRule`,
            description: 'Capture Metaflow Step Functions SUCCEEDED status',
            eventPattern: JSON.stringify({
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
                        return `arn:aws:states:${this.region.name}:${this.callerIdentity.accountId}:stateMachine:${name}`
                    })
                }
            })
        });

        new CloudwatchEventTarget(this, 'step-function-event-bridge-target', {
            rule: rule.name,
            targetId: 'lambda',
            arn: lambda.arn,
            dependsOn: [lambda, rule]
        });

        return rule;
    }

    private getLambdaDefault() {
        return new DataArchiveFile(this, 'lambda-default-file', {
            type: 'zip',
            source: [
                {
                    content: 'lambda_handler(event, context):\n\treturn',
                    filename: 'index.py'
                }
            ],
            outputPath: 'index.py.zip'
        })
    }
}
