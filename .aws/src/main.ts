import { Construct } from "constructs";
import { App, S3Backend, TerraformStack } from "cdktf";

import { config } from "./config";

import { ArchiveProvider } from "@cdktf/provider-archive/lib/provider";
import { AwsProvider } from "@cdktf/provider-aws/lib/provider";
import { LocalProvider } from "@cdktf/provider-local/lib/provider";
import { NullProvider } from "@cdktf/provider-null/lib/provider";

class RecommendationAPI extends TerraformStack {
  constructor(scope: Construct, name: string) {
    super(scope, name);

    // Create providers
    new AwsProvider(this, "aws", {
      region: "us-east-1",
      defaultTags: [{ tags: config.tags }],
    });
    new LocalProvider(this, "local_provider");
    new NullProvider(this, "null_provider");
    new ArchiveProvider(this, "archive_provider");

    new S3Backend(this, {
      bucket: `mozilla-content-team-${config.environment.toLowerCase()}-terraform-state`,
      dynamodbTable: `mozilla-content-team-${config.environment.toLowerCase()}-terraform-state`,
      key: config.name,
      region: "us-east-1",
    });
  }
}

const app = new App();
new RecommendationAPI(app, "recommendation-api");
app.synth();
