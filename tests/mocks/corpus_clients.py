import os

import pytest

from app.config import ROOT_DIR
from app.data_providers.corpus.corpus_feature_group_client import CorpusFeatureGroupClient
from tests.mocks.feature_store_mock import FeatureStoreMock
