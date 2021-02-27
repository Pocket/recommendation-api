const name = 'RecommendationAPI';
let environment;
let domain;
let clickdataDynamodbName;
let cacheNodes;
let cacheSize;

if (process.env.NODE_ENV === 'development') {
  environment = 'Dev';
  domain = 'recommendation-api.getpocket.dev';
  clickdataDynamodbName = 'ExploreClickData-ClickData';
  cacheNodes = 1;
  cacheSize = 'cache.t3.micro';
} else {
  environment = 'Prod';
  domain = 'recommendation-api.readitlater.com';
  clickdataDynamodbName = 'explore-clickdata-update-prod-ClickData';
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
  clickdataDynamodbName,
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
