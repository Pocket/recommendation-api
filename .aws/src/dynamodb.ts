import {TerraformStack} from "cdktf";
import {Construct} from "constructs";
import {config} from "./config";
import {ApplicationDynamoDBTable} from "@pocket/terraform-modules";

export class DynamoDB extends TerraformStack {
    constructor(scope: Construct, name: string) {
        super(scope, name);
        this.setupCandidatesTable();
        this.setupTopicsMetadataTable();
    }

    /**
     * Sets up the dynamodb table where the candidates will live
     * @private
     */
    private setupCandidatesTable() {
        new ApplicationDynamoDBTable(this, `candidates`, {
            tags: config.tags,
            prefix: `${config.prefix}-Candidates`,
            tableConfig: {
                hashKey: 'item_id',
                writeCapacity: 5,
                readCapacity: 5,
                attribute: [{
                    name: 'item_id',
                    type: 'S'
                }]
            },
            readCapacity: {
                tracking: 70,
                max: 100,
                min: 5
            },
            writeCapacity: {
                tracking: 70,
                max: 100,
                min: 5
            }
        });
    }


    /**
     * Sets up the dynamodb table where the topics will live
     * @private
     */
    private setupTopicsMetadataTable() {
        new ApplicationDynamoDBTable(this, `topic_metadata`, {
            tags: config.tags,
            prefix: `${config.prefix}-TopicMetadata`,
            tableConfig: {
                hashKey: 'slug',
                writeCapacity: 5,
                readCapacity: 5,
                attribute: [{
                    name: 'slug',
                    type: 'S'
                }],
                globalSecondaryIndex: [
                    {
                        hashKey: 'curator_label',
                        name: 'curator_label-index',
                        projectionType: 'ALL',
                        readCapacity: 5,
                        writeCapacity: 5,
                    }
                ]
            },
            readCapacity: {
                tracking: 70,
                max: 100,
                min: 5
            },
            writeCapacity: {
                tracking: 70,
                max: 100,
                min: 5
            }
        });
    }
}