
# Unfortunately boto3 doesn't use types for feature store records at the moment, so we define one ourselves.
FeatureStoreRecordType = List[Dict[str, str]]


BATCH_GET_RECORD_MAX_ITEMS = 10
