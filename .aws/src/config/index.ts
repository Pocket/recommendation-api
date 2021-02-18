const name = 'RecommendationAPI';
let environment;
let domain;
let clickdataDynamodbName

if (process.env.NODE_ENV === 'development') {
  environment = 'Dev';
  domain = 'recommendation-api.getpocket.dev';
  clickdataDynamodbName = 'ExploreClickData-ClickData';
} else {
  environment = 'Prod';
  domain = 'recommendation-api.readitlater.com';
  clickdataDynamodbName = 'explore-clickdata-update-prod-ClickData';
}

export const config = {
  name,
  prefix: `${name}-${environment}`,
  circleCIPrefix: `/${name}/CircleCI/${environment}`,
  shortName: 'RECAPI',
  environment,
  domain,
  clickdataDynamodbName,
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
