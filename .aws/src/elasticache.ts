import { Construct } from 'constructs';
import { config } from './config';
import {
  ApplicationMemcache,
  PocketVPC,
} from '@pocket-tools/terraform-modules';

export class Elasticache extends Construct {
  public readonly nodeList: string[];
  public readonly clusterArn: string;

  constructor(scope: Construct, name: string) {
    super(scope, name);

    const { nodeList, clusterArn } = Elasticache.createElasticache(scope);
    this.nodeList = nodeList;
    this.clusterArn = clusterArn;
  }

  /**
   * Creates the Elasticache cluster and returns the node list and cluster ARN.
   * @param scope
   * @private
   */
  private static createElasticache(scope: Construct): { nodeList: string[]; clusterArn: string } {
    const pocketVPC = new PocketVPC(scope, 'pocket-shared-vpc');

    const elasticache = new ApplicationMemcache(scope, 'memcached', {
      allowedIngressSecurityGroupIds: undefined,
      node: {
        count: config.cacheNodes,
        size: config.cacheSize,
      },
      subnetIds: pocketVPC.privateSubnetIds,
      vpcId: pocketVPC.vpc.id,
      prefix: config.prefix,
    });

    const nodeList: string[] = [];
    for (let i = 0; i < config.cacheNodes; i++) {
      nodeList.push(`${elasticache.elasticacheCluster.cacheNodes.get(i).address}:11211`);
    }

    const clusterArn = elasticache.elasticacheCluster.arn;

    return { nodeList, clusterArn };
  }
}
