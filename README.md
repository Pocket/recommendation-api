# Welcome to the Recommendations API App!

We use this app for serving customers recommendations of topics they might like.

## Development Setup & Running Tests

For complete instructions, see [docs/development.md](/docs/development.md).

TL;DR: 
1. `docker-compose build`
2. `docker-compose up`
3. Visit http://localhost:8000

## Example queries
To list all slates:
```graphql
query list_slates{ 
  listSlates {
    id
  }
}
```
 
To get self-improvement slates with recommendations: 
```graphql
query test_query {
  getSlateLineup(slateLineupId: "63f24663-0e80-4c08-82aa-3fb0e06c4979") {
      experimentId
      slates {
        displayName
        recommendations {
          itemId
        }
      }
   }         
}
```
