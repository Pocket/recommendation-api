import logging
import time
from threading import Thread
from typing import List, Dict, Optional

import numpy as np

from app import config
from app.data_providers.model_loading import ModelLoader
from app.models.corpus_item_model import CorpusItemModel


class HybridCFModel:
    approved_subset_items: np.ndarray
    item_factors: np.ndarray
    user_factors: np.ndarray
    items_bias: np.ndarray
    users_bias: np.ndarray
    users2idx: Dict[str, int]
    idx2items: Dict[int, str]
    idx2users: Dict[int, str]
    content_to_corpus_items_lkp: Dict[str, str]

    def __init__(self, artifacts: Dict, past_engagements_lkp: Dict):
        self.past_engagements_lkp = past_engagements_lkp
        self.approved_subset_items = artifacts['approved_subset_items']
        self.item_factors = artifacts['item_factors_approved']
        self.user_factors = artifacts['user_factor']
        self.items_bias = artifacts['items_bias']
        self.users_bias = artifacts['users_bias']
        self.users2idx = artifacts['users2idx']
        self.idx2users = {idx: u for u, idx in self.users2idx.items()}
        self.idx2items = artifacts['idx2items']
        self.content_to_corpus_items_lkp = artifacts['content_to_corpus_items_lkp']


def reload_periodically(recommender, delay_sec: int):
    while True:
        try:
            time.sleep(delay_sec)
            recommender.load_model()
        except Exception as ex:
            logging.error(f'HybridCF: error while reloading the model: {ex}', exc_info=ex)


class HybridCFRecommender:
    """
    Hybrid Collaborative Filtering recommender
    """
    def __init__(self, model_loader: ModelLoader):
        self._model_loader = model_loader
        self._model = None

        self.load_model()
        self.thread = Thread(target=reload_periodically, daemon=True,
                             args=(self, config.hybrid_cf['reload_time_sec']))
        self.thread.start()

    def load_model(self):
        logging.info('HybridCF: loading models')
        model_artifacts = self._model_loader.load(config.hybrid_cf['model_artifacts'])
        past_engagements_lkp = self._model_loader.load(config.hybrid_cf['past_engagements'])

        model = HybridCFModel(artifacts=model_artifacts, past_engagements_lkp=past_engagements_lkp)
        logging.info('HybridCF: models are loaded')

        assert len(self.recommend(model.idx2users[0], 10, model=model)) == 10
        self._model = model

    def can_recommend(self, user_id: str) -> bool:
        return user_id in self._model.users2idx

    def recommend(self, user_id: str, k: int, model: HybridCFModel = None) -> Optional[List[CorpusItemModel]]:
        model = model or self._model

        user_idx = model.users2idx.get(user_id)
        if user_idx is None:
            logging.info(f'HybridCF: user not found {user_id}')
            return None

        # run inference
        dot_prod = np.dot(model.item_factors, model.user_factors[user_idx])
        scores = (dot_prod + model.items_bias + model.users_bias[user_idx])
        recs = model.approved_subset_items[np.argsort(-scores)][:k]

        # filter already engaged
        corpus_ids = []
        past_engagements = model.past_engagements_lkp[user_id]
        for i, rec in enumerate(recs):
            if model.idx2items[rec] not in past_engagements:
                corpus_ids.append(model.content_to_corpus_items_lkp[model.idx2items[rec]])

        return [CorpusItemModel(id=id) for id in corpus_ids]
