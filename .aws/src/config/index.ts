const name = 'RecommendationAPI';
const domainPrefix = 'recommendation-api';
const isDev = process.env.NODE_ENV === 'development';
const environment = isDev ? 'Dev' : 'Prod';
const isProd : boolean = environment === "Prod";
const domain = isDev
  ? `${domainPrefix}.getpocket.dev`
  : `${domainPrefix}.readitlater.com`;

// aiocache currently does not support data partitioning, so there's little benefit to having more than 1 node.
const cacheNodes = isDev ? 1 : 1;
const cacheSize = isDev ? 'cache.t2.micro' : 'cache.t3.medium';

export const config = {
  name,
  prefix: `${name}-${environment}`,
  circleCIPrefix: `/${name}/CircleCI/${environment}`,
  shortName: 'RECAPI',
  isProd,
  isDev,
  environment,
  domain,
  recommendationMetricsDynamodbName: `MODELD-${environment}-RecMetrics`,
  slateMetricsDynamodbName: `MODELD-${environment}-SlateMetrics`,
  cacheNodes,
  cacheSize,
  stateMachines: [
    'CuratedCandidatesFlow',
    'AlgorithmicCandidatesFlow',
    'CoronavirusPageFlow'
  ],
  tags: {
    service: name,
    environment
  }
};
