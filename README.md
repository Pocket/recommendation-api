# Welcome to the Explore Topics API App!

We use this app for serving customers recommendations of topics they might like. 

## Development Setup

### Requirements:

- pip
- pipenv
- docker (and, if you're on Windows or Linux, separately install docker-compose. It comes with the docker Mac installation)
- An IDE (we like PyCharm)

1. To install dependencies for development and run a virtual environment, run `pipenv install --dev`
1. After this, preface all command line calls with `pipenv run <command>`
2. Create a `.env` file in the project root:
```
SENTRY_DSN=<local Sentry DSN>
```

### Running the Tests

1. Run with `pipenv run pytest tests`

### Running the App

1. To run the app, run `docker-compose up`
2. The app should then be available at localhost:8000

### Using the App

1. This is an API on the GraphQL protocol. When you visit localhost:8000, you will have:
 - a panel (left) where you can enter a query
 - a panel (center) where results of queries will appear when you write a query and click the "play" button on the top bar
 - a panel (right) for clicking around to explore our GraphQL query model

Example queries: 

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
