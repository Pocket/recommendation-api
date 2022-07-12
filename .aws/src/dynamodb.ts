import {Resource} from "cdktf";
import {Construct} from "constructs";
import {config} from "./config";
import {ApplicationDynamoDBTable} from "@pocket-tools/terraform-modules";
import {dynamodb} from "@cdktf/provider-aws";

export class DynamoDB extends Resource {

  public readonly candidatesTable: ApplicationDynamoDBTable
  public readonly metadataTable: ApplicationDynamoDBTable
  public readonly recommendationMetricsTable: dynamodb.DataAwsDynamodbTable
  public readonly slateMetricsTable: dynamodb.DataAwsDynamodbTable
  public readonly candidateSetsTable: ApplicationDynamoDBTable;

  constructor(scope: Construct, name: string) {
    super(scope, name);
    this.candidatesTable = this.setupCandidatesTable();
    this.metadataTable = this.setupTopicsMetadataTable();
    this.recommendationMetricsTable = this.getRecommendationMetricsTable();
    this.slateMetricsTable = this.getSlateMetricsTable();
    this.candidateSetsTable = this.setupCandidateSetsTable();
  }

  /**
   * @deprecated Delete this table if PR #409 is deployed without issues for a week:
   * https://github.com/Pocket/recommendation-api/pull/409
   *
   * Sets up the dynamodb table where the candidates will live
   * @private
   */
  private setupCandidatesTable() {
    return new ApplicationDynamoDBTable(this, `candidates`, {
      tags: config.tags,
      prefix: `${config.shortName}-${config.environment}-Candidates`,
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
      },
      preventDestroyTable: false,
    });
  }


  /**
   * Sets up the dynamodb table where the topics will live
   * @private
   */
  private setupTopicsMetadataTable() {
    return new ApplicationDynamoDBTable(this, `topic_metadata`, {
      tags: config.tags,
      prefix: `${config.shortName}-${config.environment}-TopicMetadata`,
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


  /**
   * Sets up the dynamodb table where the candidate sets will live
   * @private
   */
  private setupCandidateSetsTable() {
    return new ApplicationDynamoDBTable(this, `candidate_sets`, {
      tags: config.tags,
      prefix: `${config.shortName}-${config.environment}-CandidateSets`,
      tableConfig: {
        hashKey: 'id',
        writeCapacity: 5,
        readCapacity: 5,
        attribute: [
          {
            name: 'id',
            type: 'S'
          }
        ],
        ttl: {
          attributeName: 'expires_at',
          enabled: true
        },
        globalSecondaryIndex: [],
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

  private getRecommendationMetricsTable() {
    return new dynamodb.DataAwsDynamodbTable(this, `rec_metrics`, {
      name: config.recommendationMetricsDynamodbName,
    });
  }

  private getSlateMetricsTable() {
    return new dynamodb.DataAwsDynamodbTable(this, `slate_metrics`, {
      name: config.slateMetricsDynamodbName,
    });
  }
}
