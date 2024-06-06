const name = 'RecommendationAPI';
const domainPrefix = 'recommendation-api';
const isDev = process.env.NODE_ENV === 'development';
const environment = isDev ? 'Dev' : 'Prod';
const githubConnectionArn = isDev
  ? 'arn:aws:codestar-connections:us-east-1:410318598490:connection/7426c139-1aa0-49e2-aabc-5aef11092032'
  : 'arn:aws:codestar-connections:us-east-1:996905175585:connection/5fa5aa2b-a2d2-43e3-ab5a-72ececfc1870';
const branch = isDev ? 'dev' : 'main';
const domain = isDev
  ? `${domainPrefix}.getpocket.dev`
  : `${domainPrefix}.readitlater.com`;

// aiocache currently does not support data partitioning, so there's little benefit to having more than 1 node.
const cacheNodes = isDev ? 1 : 1;
const cacheSize = isDev ? 'cache.t3.micro' : 'cache.t3.medium';

export const config = {
  name,
  prefix: `${name}-${environment}`,
  circleCIPrefix: `/${name}/CircleCI/${environment}`,
  shortName: 'RECAPI',
  isDev,
  codePipeline: {
    githubConnectionArn,
    repository: 'pocket/recommendation-api',
    branch,
  },
  environment,
  domain,
  recommendationMetricsDynamodbName: `MODELD-${environment}-RecMetrics`,
  slateMetricsDynamodbName: `MODELD-${environment}-SlateMetrics`,
  cacheNodes,
  cacheSize,
  stateMachines: [
    'CuratedCandidatesFlow',
    'AlgorithmicCandidatesFlow',
    'CoronavirusPageFlow',
  ],
  tags: {
    service: name,
    environment,
    app_code: 'pocket-content-shared',
    component_code: `pocket-content-shared-${name.toLowerCase()}`,
    env_code: isDev ? 'dev' : 'prod',
  },
};
