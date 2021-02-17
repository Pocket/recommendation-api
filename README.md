# Welcome to the Explore Topics API App!

We use this app for serving customers recommendations of topics they might like. 

## Development Setup

### Requirements

- pip
- pipenv
- docker (and, if you're on Windows or Linux, separately install docker-compose. It comes with the docker Mac installation)
- An IDE (we like PyCharm)
- Create a `.env` file in the project root:
```
SENTRY_DSN=<local Sentry DSN>
```

### Adding interpreters to PyCharm

Remote application interpreter:
1. Open PyCharm > Preferences > Project: recommendation-api > Python Interpreter
2. Click the cog in the top-right, and choose 'add interpreter'
3. Choose 'Docker Compose'.

aws_lambda pipenv interpreter:
1. In PyCharm, choose File > Open, and open recommandation-api/aws_lambda
2. Open PyCharm > Preferences > Project: aws_lambda > Python Interpreter
2. Click the cog in the top-right, and choose 'add interpreter'
3. Choose 'PipEnv', and click 'OK'
4. Close the aws_lambda PyCharm project

### Adding Run/Debug configurations

Add a configuration for the app:
1. Click Run > Edit configurations
2. Click the + icon in the top-left, choose Python
3. Enter the settings from the screenshot below.

Add a configuration for aws_lambda tests:
1. Click Run > Edit configurations
2. Click the + icon in the top-left, choose Python tests > pytest
3. Enter the settings from the screenshot below
4. Run the tests by clicking the green play button. Contact #team-backend if the following error shows up:
```
botocore.exceptions.NoRegionError: You must specify a region.
```

## Running the Tests

1. Run with `pipenv run pytest tests`

#### App tests
1. Select Remote Python docker-compose interpreter as the project default. (See Adding interpreters to PyCharm)
2. Rightclick on 'tests' directory in the project root, and run 'pytest in tests'.

#### AWS Lambda test

Setup:
7. 

### Running the App

0. Whenever dependencies change, run `docker-compose build` to rebuild the container.
1. To run the app, run `docker-compose up`
2. The app should then be available at localhost:8000

### TEMP

1. To install dependencies for development and run a virtual environment, run `pipenv install --dev`
2. Run `docker-compose build` to build the 

### Adding Packages

`pipenv install <package>`. for dev packages, `pipenv install -d <package>`.

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
