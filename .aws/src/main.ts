import {Construct} from 'constructs';
import {App, RemoteBackend, TerraformStack} from 'cdktf';
import {AwsProvider} from '../.gen/providers/aws';
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

        new DynamoDB(this, 'dynamodb');

        new PocketALBApplication(this, 'application', {
            internal: true,
            prefix: config.name,
            alb6CharacterPrefix: config.shortName,
            tags: config.tags,
            cdn: false,
            domain: config.domain
        })
    }
}

const app = new App();
new ExploreTopics(app, 'explore-topics');
app.synth();
