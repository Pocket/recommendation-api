import {config} from './config';
import {Construct} from 'constructs';
import {AssetType, TerraformAsset} from 'cdktf';
import * as path from 'path';
import {DataArchiveFile} from '@cdktf/provider-archive/lib/data-archive-file';
import {PocketVPC} from '@pocket-tools/terraform-modules';

import {CloudwatchMetricAlarm} from '@cdktf/provider-aws/lib/cloudwatch-metric-alarm';
import {DataAwsCallerIdentity} from '@cdktf/provider-aws/lib/data-aws-caller-identity';
import {DataAwsIamPolicyDocument} from '@cdktf/provider-aws/lib/data-aws-iam-policy-document';
import {DataAwsRegion} from '@cdktf/provider-aws/lib/data-aws-region';
import {IamPolicy} from '@cdktf/provider-aws/lib/iam-policy';
import {IamRolePolicyAttachment} from '@cdktf/provider-aws/lib/iam-role-policy-attachment';
import {IamRole} from '@cdktf/provider-aws/lib/iam-role';
import {S3Bucket} from '@cdktf/provider-aws/lib/s3-bucket';
import {SyntheticsCanary} from '@cdktf/provider-aws/lib/synthetics-canary';

/**
 * Create additional monitoring
 * @param app
 * @param provider
 */
export class RecommendationApiSynthetics extends Construct {
  public readonly scope: Construct;
  public readonly name: string;

  constructor(scope: Construct, name: string) {
    super(scope, name);
  }

  createSyntheticCheck(snsAlarmTopicARNs: string[]) {
    const caller = new DataAwsCallerIdentity(this, 'caller');
    const region = new DataAwsRegion(this, 'region');
    const pocketVPC = new PocketVPC(this, 'pocket-shared-vpc');

    const syncheckArtifactsS3 = new S3Bucket(
      this,
      'synthetic_check_artifacts',
      {
        bucket: `pocket-${config.prefix.toLowerCase()}-synthetic-check`,
      }
    );

    const syntheticCode = new TerraformAsset(this, 'synthetic_check_asset', {
      path: path.resolve(`${__dirname}`, '../src/files'),
      type: AssetType.DIRECTORY,
    });

    const syncheckZipFile = new DataArchiveFile(this, 'synthetic_check_zip', {
      outputPath: `generated-archives/synthetic-${syntheticCode.assetHash}.zip`,
      sourceDir: syntheticCode.path,
      type: 'zip',
    });

    // behind the scenes, Cloudwatch Synthetics are AWS-managed Lambdas
    const dataSyncheckAssume = new DataAwsIamPolicyDocument(
      this,
      'synthetic_check_assume',
      {
        version: '2012-10-17',
        statement: [
          {
            effect: 'Allow',
            actions: ['sts:AssumeRole'],

            principals: [
              {
                identifiers: ['lambda.amazonaws.com'],
                type: 'Service',
              },
            ],
          },
        ],
      }
    );

    const syncheckRole = new IamRole(this, 'synthetic_check_role', {
      name: `pocket-${config.prefix.toLowerCase()}-synthetic-check`,

      assumeRolePolicy: dataSyncheckAssume.json,
    });

    // puts artifacts into s3, stores logs, pushes metrics to Cloudwatch
    const dataSynCheckAccess = new DataAwsIamPolicyDocument(
      this,
      'synthetic_check_access',
      {
        version: '2012-10-17',
        statement: [
          {
            effect: 'Allow',
            actions: [
              'logs:CreateLogGroup',
              'logs:CreateLogStream',
              'logs:PutLogEvents',
            ],
            resources: [
              `arn:aws:logs:${region.id}:${
                caller.accountId
              }:log-group:/aws/lambda/cwsyn-${config.prefix.toLowerCase()}-*`,
            ],
          },
          {
            effect: 'Allow',
            actions: [
                'ec2:CreateNetworkInterface',
                'ec2:DescribeNetworkInterfaces',
                'ec2:DeleteNetworkInterface',
            ],
            resources: [
                '*'
            ],
          },
          {
            actions: ['s3:PutObject', 's3:GetObject'],
            resources: [`${syncheckArtifactsS3.arn}/*`],
          },
          {
            actions: ['s3:GetBucketLocation'],
            resources: [syncheckArtifactsS3.arn],
          },
          {
            actions: ['s3:ListAllMyBuckets'],
            resources: ['*'],
          },
          {
            actions: ['cloudwatch:PutMetricData'],
            resources: ['*'],
            condition: [
              {
                test: 'StringEquals',
                values: ['CloudWatchSynthetics'],
                variable: 'cloudwatch:namespace',
              },
            ],
          },
        ],
      }
    );

    const synCheckAccessPolicy = new IamPolicy(
      this,
      'synthetic_check_access_policy',
      {
        name: `pocket-${config.prefix.toLowerCase()}-synthetic-check-access`,
        policy: dataSynCheckAccess.json,
      }
    );

    new IamRolePolicyAttachment(this, 'synthetic_check_access_attach', {
      role: syncheckRole.id,
      policyArn: synCheckAccessPolicy.arn,
    });
    
    const synCheckCanary = new SyntheticsCanary(
      this,
      'synthetic_check',
      {
        // name canary recapi-prod-new-tab to indicate only newTabSlate is covered. Name is limited to 21 characters.
        name: `${config.shortName}-new-tab-${config.environment}`.toLowerCase().substring(0, 21),
        artifactS3Location: `s3://${syncheckArtifactsS3.bucket}/`,
        executionRoleArn: syncheckRole.arn,
        handler: 'new_tab_synthetic.handler',  // Must be located in a directory named 'python'.
        runConfig: {
          timeoutInSeconds: 180, // 3 minute timeout
          environmentVariables: {
              'RECOMMENDATION_API_DOMAIN': config.domain,
          }
        },
        runtimeVersion: 'syn-python-selenium-1.3',
        schedule: {
          expression: 'rate(5 minutes)', // run every 5 minutes
        },
        startCanary: !config.isDev,
        zipFile: syncheckZipFile.outputPath,
        vpcConfig: {
          subnetIds: pocketVPC.privateSubnetIds,
          securityGroupIds: pocketVPC.defaultSecurityGroups.ids,
        }, 
      }
    );

    new CloudwatchMetricAlarm(this, 'synthetic_check_alarm', {
      alarmDescription: `Runbook: https://getpocket.atlassian.net/l/cp/5wQMswfT`,
      alarmName: `pocket-${synCheckCanary.name}-synthetic-check-access`,

      comparisonOperator: 'LessThanThreshold',
      dimensions: {
        CanaryName: synCheckCanary.name,
      },
      evaluationPeriods: 3,
      metricName: 'SuccessPercent',
      namespace: 'CloudWatchSynthetics',
      period: 300, // 15 minutes
      statistic: 'Average',
      threshold: 66,
      treatMissingData: 'breaching',

      alarmActions: snsAlarmTopicARNs,
      insufficientDataActions: [],
      okActions: snsAlarmTopicARNs,
    });
  }
}
