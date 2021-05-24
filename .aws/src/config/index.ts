const name = 'RecommendationAPI';
let environment;
let domain;
let cacheNodes;
let cacheSize;

if (process.env.NODE_ENV === 'development') {
  environment = 'Dev';
  domain = 'recommendation-api.getpocket.dev';
  cacheNodes = 1;
  cacheSize = 'cache.t3.micro';
} else {
  environment = 'Prod';
  domain = 'recommendation-api.readitlater.com';
  // aiocache currently does not support data partitioning, so there's little benefit to having more than 1 node.
  cacheNodes = 1;
  cacheSize = 'cache.t3.medium';
}

export const config = {
  name,
  prefix: `${name}-${environment}`,
  circleCIPrefix: `/${name}/CircleCI/${environment}`,
  shortName: 'RECAPI',
  environment,
  domain,
  recommendationMetricsDynamodbName: `MODELD-${environment}-RecMetrics`,
  slateClickdataDynamodbName: `MODELD-${environment}-SlateMetrics`,
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
