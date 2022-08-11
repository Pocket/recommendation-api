
# Unfortunately boto3 doesn't use types for feature store records at the moment, so we define one ourselves.
from typing import List, Dict

FeatureStoreRecordType = List[Dict[str, str]]


BATCH_GET_RECORD_MAX_ITEMS = 10


def feature_store_record_to_dict(
    record: FeatureStoreRecordType,
    lowercase_names: bool = True,
) -> Dict[str, str]:
    """
    Converts a feature group record to a dict
    :param lowercase_names: If true, feature names will be returned as lowercase, otherwise they are returned unchanged.
    :param record: List of dicts, each with a 'FeatureName' and 'ValueAsString'
    :return: Dict keyed on feature name
    """
    return {
        feature['FeatureName'].lower() if lowercase_names else feature['FeatureName']:
        feature['ValueAsString']
        for feature in record
    }
