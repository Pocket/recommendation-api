from locust import HttpUser, task, between, tag

syndicated_query = '''
  query Syndicated  {
    _entities(representations: [{
          __typename: "SyndicatedArticle",
          itemId: 3772386356,
        publisherUrl: "https://www.eater.com/21324222/moldy-food-safety-whats-safe-to-eat"
      
    }]) {
        ... on SyndicatedArticle {
            itemId
            publisherUrl
            relatedEndOfArticle(count: 3) {
                id
                corpusItem {
                  id
                }
            }
            relatedRightRail(count: 3) {
                id
                corpusItem {
                  id
                }
            }
      }
    }
  }
'''

item_after_article_query = '''
  query ItemAfterArticle  {
    _entities(representations: [{
          __typename: "Item",
          itemId: 481684109
    }]) {
      ... on Item {
          itemId
          relatedAfterArticle(count: 3) {
              id
              corpusItem {
                id
              }
          }
      }
    }
	}
'''

item_after_create_query = '''
  query ItemAfterArticle  {
    _entities(representations: [{
          __typename: "Item",
          itemId: 481684109
    }]) {
      ... on Item {
          itemId
          relatedAfterCreate(count: 3) {
              id
              corpusItem {
                id
              }
          }
      }
    }
	}
'''


class RecommendUser(HttpUser):
    wait_time = between(3, 5)

    @tag('syndicated')
    @task
    def recommend_syndicated(self):
        res = self.client.post("/", json={'query': syndicated_query})

        response = res.json()
        assert not response.get('errors')
        entity = response['data']['_entities'][0]
        recs1 = entity['relatedEndOfArticle']
        recs2 = entity['relatedRightRail']
        assert len(recs1) == 3
        assert len(recs2) == 3

    @tag('after-article')
    @task
    def recommend_after_article(self):
        res = self.client.post("/", json={'query': item_after_article_query})

        response = res.json()
        assert not response.get('errors')
        entity = response['data']['_entities'][0]
        recs = entity['relatedAfterArticle']
        assert len(recs) == 3

    @tag('after-create')
    @task
    def recommend_after_create(self):
        res = self.client.post("/", json={'query': item_after_create_query})

        response = res.json()
        assert not response.get('errors')
        entity = response['data']['_entities'][0]
        recs = entity['relatedAfterCreate']
        assert len(recs) == 3
