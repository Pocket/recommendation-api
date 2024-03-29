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
