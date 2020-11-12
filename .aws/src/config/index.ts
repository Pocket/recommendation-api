const name = 'ExploreTopics';
let environment;
let domain;

if (process.env.NODE_ENV === 'development') {
  environment = 'Dev';
  domain = 'explore-topics.getpocket.dev';
} else {
  environment = 'Prod';
  domain = 'explore-topics.readitlater.com';
}

export const config = {
  name,
  prefix: `${name}-${environment}`,
  circleCIPrefix: `/${name}/CircleCI/${environment}`,
  shortName: 'EXTOP',
  environment,
  domain,
  stateMachines: [
    'CuratedCandidatesFlow',
    'AlgorithmicCandidatesFlow',
    'CollectionCandidatesFlow'
  ],
  tags: {
    service: name,
    environment
  }
};
