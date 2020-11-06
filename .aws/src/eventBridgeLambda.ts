import {TerraformStack} from "cdktf";
import {Construct} from "constructs";
import {config} from "./config";
import {PocketVPC} from "@pocket/terraform-modules";
import {PocketEventBridgeWithLambdaTarget} from "@pocket/terraform-modules/dist/src/pocket/PocketEventBridgeWithLambdaTarget";
import {LAMBDA_RUNTIMES} from "@pocket/terraform-modules/dist/src/base/ApplicationVersionedLambda";

export class EventBridgeLambda extends TerraformStack {
    constructor(private scope: Construct, private name: string) {
        super(scope, name);

        const vpc = new PocketVPC(this, 'pocket-shared-vpc');

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
            handler: 'index.handler',
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
}
