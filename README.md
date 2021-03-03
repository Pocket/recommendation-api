# Welcome to the Recommendations API App!

We use this app for serving customers recommendations of topics they might like.

## Development Setup & Running Tests

For complete instructions, see [docs/development.md](/docs/development.md).

TL;DR: 
1. `docker-compose build`
2. `docker-compose up`
3. Visit http://localhost:8000

## GraphQL API

To get a list of topics:
```
query list {
    listTopics {
        slug
    }
}
```

To get topic recommendations: 
```
query recs {
  getTopicRecommendations(slug: "business") {
    algorithmicRecommendations {feedItemId itemId feedId}
    curatedRecommendations {feedItemId itemId feedId}
	}
}
```
