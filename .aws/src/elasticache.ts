import { Construct } from 'constructs';
import { config } from './config';
import {
  ApplicationMemcache,
  PocketVPC,
} from '@pocket-tools/terraform-modules';

export class Elasticache extends Construct {
  public readonly nodeList: string[];

  constructor(scope: Construct, name: string) {
    super(scope, name);

    this.nodeList = Elasticache.createElasticache(scope);
  }

  /**
   * Creates the elasticache and returns the node address list
   * @param scope
   * @private
   */
  private static createElasticache(scope: Construct): string[] {
    const pocketVPC = new PocketVPC(scope, 'pocket-shared-vpc');

    const elasticache = new ApplicationMemcache(scope, 'memcached', {
      //Usually we would set the security group ids of the service that needs to hit this.
      //However we don't have the necessary security group because it gets created in PocketALBApplication
      //So instead we set it to null and allow anything within the vpc to access it.
      //This is not ideal..
      //Ideally we need to be able to add security groups to the ALB application.
      allowedIngressSecurityGroupIds: undefined,
      node: {
        count: config.cacheNodes,
        size: config.cacheSize,
      },
      subnetIds: pocketVPC.privateSubnetIds,
      tags: config.tags,
      vpcId: pocketVPC.vpc.id,
      prefix: config.prefix,
    });

    let nodeList: string[] = [];
    for (let i = 0; i < config.cacheNodes; i++) {
      // ${elasticache.elasticacheClister.cacheNodes(i.toString()).port} has a bug and is not rendering the proper terraform address
      // its rendering -1.8881545897087503e+289 for some weird reason...
      // For now we just hardcode to 11211 which is the default memcache port.
      nodeList.push(
        `${
          // elasticache.elasticacheCluster.cacheNodes(i.toString()).address
          elasticache.elasticacheCluster.cacheNodes.get(i).address
        }:11211`
      );
    }
    return nodeList;
  }
}
