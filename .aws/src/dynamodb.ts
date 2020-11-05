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
                hashKey: 'id',
                writeCapacity: 5,
                readCapacity: 5,
                attribute: [
                    {
                        name: 'id',
                        type: 'S'
                    },
                    {
                        name: 'created_at',
                        type: 'S'
                    },
                    {
                        name: 'topic_id-type',
                        type: 'S'
                    }
                ],
                globalSecondaryIndex: [
                    {
                        name: 'topic_id-type',
                        hashKey: 'topic_id-type',
                        rangeKey: 'created_at',
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


    /**
     * Sets up the dynamodb table where the topics will live
     * @private
     */
    private setupTopicsMetadataTable() {
        new ApplicationDynamoDBTable(this, `topic_metadata`, {
            tags: config.tags,
            prefix: `${config.prefix}-TopicMetadata`,
            tableConfig: {
                hashKey: 'id',
                writeCapacity: 5,
                readCapacity: 5,
                attribute: [
                    {
                        name: 'id',
                        type: 'S'
                    },
                    {
                        name: 'slug',
                        type: 'S'
                    }
                ],
                globalSecondaryIndex: [
                    {
                        name: 'slug',
                        hashKey: 'slug',
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
