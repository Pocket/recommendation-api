from locust import HttpUser, task, between, tag

home_query = '''
query HomelateLineup {
  homeSlateLineup {
    slates {
      headline
      subheadline
      moreLink { url text }
      recommendationReasonType
      recommendations {
        corpusItem {
          id
        }
        reason {
          name
          type
        }
      }
    }
  }
}

'''

class RecommendUser(HttpUser):
    wait_time = between(3, 5)

    @tag('cf')
    @task
    def recommend_hybrid_cf(self):
        res = self.client.post("/", json={'query': home_query}, headers={
            "userId": "123456",
            "encodedId": "587Aag53d47e2Tb263p3e0GpF8TTd821e51e8ak8fna444A9emI9fc50Hb6umd2c",
            "Content-Type": "application/json"
        })

        response = res.json()
        assert not response.get('errors')
        slates = response['data']['homeSlateLineup']['slates']
        assert slates[0]['headline'] == 'For You'
        assert slates[0]['recommendationReasonType'] == 'HYBRID_CF_RECOMMENDER'
        assert len(slates[0]['recommendations']) == 10

    @tag('default')
    @task
    def recommend_default(self):
        res = self.client.post("/", json={'query': home_query}, headers={
            "userId": "123456",
            "encodedId": "xxasd123",
            "Content-Type": "application/json"
        })

        response = res.json()
        assert not response.get('errors')
        slates = response['data']['homeSlateLineup']['slates']
        assert slates[0]['headline'] == 'Recommended Reads'
        assert slates[0]['recommendationReasonType'] == None
        assert len(slates[0]['recommendations']) == 10
