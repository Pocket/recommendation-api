import { config } from './config';
import { Construct } from 'constructs';
import { AssetType, TerraformAsset } from 'cdktf';
import * as path from 'path';
import { DataArchiveFile } from '@cdktf/provider-archive';
import {
  cloudwatch,
  DataAwsDefaultTags,
  datasources,
  iam,
  synthetics,
  s3,
} from '@cdktf/provider-aws';
import { PocketVPC } from '@pocket-tools/terraform-modules';

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

    new DataAwsDefaultTags(this, 'monitoring_default_tags', {
      tags: config.tags,
    });
  }

  createSyntheticCheck(snsCriticalAlarmTopicARN: string) {
    const caller = new datasources.DataAwsCallerIdentity(this, 'caller');
    const region = new datasources.DataAwsRegion(this, 'region');
    const pocketVPC = new PocketVPC(this, 'pocket-shared-vpc');

    const syncheckArtifactsS3 = new s3.S3Bucket(
      this,
      'synthetic_check_artifacts',
      {
        bucket: `pocket-${config.prefix.toLowerCase()}-synthetic-check`,
      }
    );

    const syntheticCode = new TerraformAsset(this, 'synthetic_check_asset', {
      path: path.resolve(`${__dirname}`, 'files/synthetic/synthetic.py'),
      type: AssetType.FILE,
    });

    const syncheckZipFile = new DataArchiveFile(this, 'synthetic_check_zip', {
      outputPath: `generated-archives/synthetic-${syntheticCode.assetHash}.zip`,
      sourceDir: syntheticCode.path,
      type: 'zip',
    });

    // behind the scenes, Cloudwatch Synthetics are AWS-managed Lambdas
    const dataSyncheckAssume = new iam.DataAwsIamPolicyDocument(
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

    const syncheckRole = new iam.IamRole(this, 'synthetic_check_role', {
      name: `pocket-${config.prefix.toLowerCase()}-synthetic-check`,

      assumeRolePolicy: dataSyncheckAssume.json,
      tags: config.tags,
    });

    // puts artifacts into s3, stores logs, pushes metrics to Cloudwatch
    const dataSynCheckAccess = new iam.DataAwsIamPolicyDocument(
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

    const synCheckAccessPolicy = new iam.IamPolicy(
      this,
      'synthetic_check_access_policy',
      {
        name: `pocket-${config.prefix.toLowerCase()}-synthetic-check-access`,
        policy: dataSynCheckAccess.json,
      }
    );

    new iam.IamRolePolicyAttachment(this, 'synthetic_check_access_attach', {
      role: syncheckRole.id,
      policyArn: synCheckAccessPolicy.arn,
    });
    
    const synCheckCanary = new synthetics.SyntheticsCanary(
      this,
      'synthetic_check',
      {
        name: `${config.prefix.toLowerCase()}`, // limit of 21 characters

        artifactS3Location: `s3://${syncheckArtifactsS3.bucket}/`,
        executionRoleArn: syncheckRole.arn,
        handler: 'synthetic.handler',
        runConfig: {
          timeoutInSeconds: 180, // 3 minute timeout
        },
        runtimeVersion: 'sync-python-selenium-1.3',
        schedule: {
          expression: 'rate(5 minutes)', // run every 5 minutes
        },
        startCanary: true,
        zipFile: syncheckZipFile.outputPath,
        vpcConfig: {
          subnetIds: pocketVPC.privateSubnetIds,
          securityGroupIds: [pocketVPC.defaultSecurityGroups.id],
        }, 
      }
    );

    new cloudwatch.CloudwatchMetricAlarm(this, 'synthetic_check_alarm', {
      alarmDescription: `Alert when ${synCheckCanary.name} canary success percentage has decreased below 66% in the last 15 minutes`,
      alarmName: `pocket-${config.prefix.toLowerCase()}-synthetic-check-access`,

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

      alarmActions: [snsCriticalAlarmTopicARN],
      insufficientDataActions: [],
      okActions: [snsCriticalAlarmTopicARN],
    });
  }
}