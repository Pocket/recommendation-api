event = {
    'version': '0',
    'id': '4d940b9c-f64d-6550-a816-e5d8b081ec18',
    'detail-type': 'Step Functions Execution Status Change',
    'source': 'aws.states',
    'account': '996905175585',
    'time': '2020-11-10T16:13:32Z',
    'region': 'us-east-1',
    'resources': [
        'arn:resource'
    ],
    'detail': {
        'executionArn': 'arn:execution',
        'stateMachineArn': 'arn:aws:states:us-east-1:996905175585:stateMachine:CuratedCandidatesFlow',
        'name': 'd3f71c11-26d3-bbbc-6a7f-4efafc51f9d2_283eaaf0-5b60-f4fb-8cf7-9e629d1f9de1', 'status': 'SUCCEEDED',
        'startDate': 1605024016678, 'stopDate': 1605024812793, 'input': '{"Parameters": "{}"}',
        'inputDetails': {'included': True},
        'output': '{"JobId":"e0bb55c3-bf95-49cf-a108-2c7e21d27d44","Parameters":{"metaflow.step_name":"end","metaflow.flow_name":"CuratedCandidatesFlow","metaflow.run_id":"d3f71c11-26d3-bbbc-6a7f-4efafc51f9d2_283eaaf0-5b60-f4fb-8cf7-9e629d1f9de1","step_name":"end","metaflow.version":"2.2.4","metaflow.owner":"codebuild","metaflow.user":"SFN"}}',
        'outputDetails': {'included': True}
    }
}

metaflow_data = [
    {
        "topic_id": 1,
        "items": [
            {
                "item_id": 1,
                "feed_id": 1
            }
        ]
    },
    {
        "topic_id": 2,
        "items": [
            {
                "item_id": 2,
                "feed_id": 2
            }
        ]
    }
]