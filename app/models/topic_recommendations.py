import asyncio

from pydantic import BaseModel
from typing import List
from scipy.stats import beta
from operator import itemgetter
from app.models.recommendation import RecommendationModel, RecommendationType
from app.models.topic import TopicModel, PageType
from aws_xray_sdk.core import xray_recorder
from app.models.clickdata import ClickdataModel, RecommendationModules


class TopicRecommendationsModel(BaseModel):
    curated_recommendations: List[RecommendationModel] = []
    algorithmic_recommendations: List[RecommendationModel] = []

    @staticmethod
    @xray_recorder.capture_async('models_topic_get_recommendations')
    async def get_recommendations(
            slug: str,
            algorithmic_count: int,
            curated_count: int,
            publisher_spread: int = 3) -> ['TopicRecommendationsModel']:

        # Pull in the topic so we can split what we do based on the page type.
        topic = await TopicModel.get_topic(slug=slug)

        topic_recommendations = TopicRecommendationsModel()

        if topic.page_type == PageType.editorial_collection:
            # Editorial collections just use the curated_recommendation responses but are saved in dynamodb as a
            # "collection"
            topic_recommendations.curated_recommendations = await RecommendationModel.get_recommendations(
                topic_id=topic.id,
                recommendation_type=RecommendationType.COLLECTION
            )
        else:
            algorithmic_results, curated_results = await asyncio.gather(RecommendationModel.get_recommendations(
                topic_id=topic.id,
                recommendation_type=RecommendationType.ALGORITHMIC,
            ), RecommendationModel.get_recommendations(
                topic_id=topic.id,
                recommendation_type=RecommendationType.CURATED
            ))
            topic_recommendations.algorithmic_recommendations = algorithmic_results
            topic_recommendations.curated_recommendations = curated_results

        # dedupe items in the algorithmic recommendations
        topic_recommendations = TopicRecommendationsModelUtils.dedupe(topic_recommendations)

        # topic_recommendations.curated_recommendations = TopicRecommendationsModelUtils.thompson_sampling(
        #     topic_recommendations.curated_recommendations, RecommendationModules.TOPIC)

        topic_recommendations.algorithmic_recommendations = await TopicRecommendationsModelUtils.thompson_sampling(
            topic_recommendations.algorithmic_recommendations, RecommendationModules.TOPIC)

        # spread out publishers in algorithmic recommendations so articles from the same publisher are not right next
        # to each other. (curated recommendations are expected to be intentionally ordered.)
        topic_recommendations.algorithmic_recommendations = TopicRecommendationsModelUtils.spread_publishers(
            topic_recommendations.algorithmic_recommendations, publisher_spread)

        # lets limit the result set to what was requested.
        topic_recommendations = TopicRecommendationsModelUtils.limit_results(topic_recommendations,
                                                                             algorithmic_count,
                                                                             curated_count)

        return topic_recommendations


class TopicRecommendationsModelUtils:
    @staticmethod
    @xray_recorder.capture('models_topic_dedupe')
    def dedupe(topic_recs_model: TopicRecommendationsModel) -> TopicRecommendationsModel:
        """
        If a recommendation exists in both the curated and algorithmic lists, removes that recommendation from the
        algorithmic list (favoring the curated list).

        :param topic_recs_model: an object containing collections of curated and algorithmic recommendations
        :return: the same object, with entries in the curated collection removed from the algorithmic collection
        """

        # are there dupes?
        curated_item_ids = {x.item_id for x in topic_recs_model.curated_recommendations}
        algorithmic_item_ids = {x.item_id for x in topic_recs_model.algorithmic_recommendations}

        dupes = set(curated_item_ids) & set(algorithmic_item_ids)

        if dupes:
            # if there are dupes, remove the duplicates from the algorithmic recs
            topic_recs_model.algorithmic_recommendations = list(filter(lambda rec: rec.item_id not in curated_item_ids,
                                                                       topic_recs_model.algorithmic_recommendations))

        return topic_recs_model

    @staticmethod
    def limit_results(topic_recommendations: TopicRecommendationsModel,
                      algorithmic_count: int,
                      curated_count: int
                      ) -> TopicRecommendationsModel:
        # The requester wants us to limit our results, so lets truncate the arrays
        topic_recommendations.algorithmic_recommendations = topic_recommendations.algorithmic_recommendations[
                                                            0: algorithmic_count]
        topic_recommendations.curated_recommendations = topic_recommendations.curated_recommendations[
                                                        0: curated_count]

        return topic_recommendations

    @staticmethod
    @xray_recorder.capture('models_topic_spread_publishers')
    def spread_publishers(recs: List[RecommendationModel], spread: int = 3) -> List[RecommendationModel]:
        """
        Makes sure stories from the same publisher/domain are not listed sequentially, and have a configurable number
        of stories in-between them.

        :param recs: a list of recommendations in the desired order (pre-publisher spread)
        :param spread: the minimum number of items before we can repeat a publisher/domain
        :return: a re-ordered version of recs satisfying the spread as best as possible
        """

        # if there are no recommendations, we done
        if not len(recs):
            return recs

        # move first item in list to first item in re-ordered list
        reordered = [recs.pop(0)]

        # iterator to keep track of spread between domains
        iterator = 0

        # iterate over remaining items in recs
        while len(recs):
            # if there aren't enough items left in recs to satisfy the desired domain spread,
            # or if the iterator reaches the end of recs, then we cannot spread any further.
            # just add the rest of the recs as-is to the end of the re-ordered list.

            # note that this is a simplistic take - we could write more logic here to decrease the spread value by
            # one each time if iterator reaches or exceeds the length of recs
            if (len(recs) <= spread) or (iterator >= len(recs)):
                reordered.extend(recs)
                break

            # get a list of domains that are currently invalid in the sequence
            if len(reordered) > spread:
                # if we have enough items in the reordered list, the invalid domains are the last spread number
                domains_to_check = [x.publisher for x in reordered[-spread:]]
            else:
                # if we don't have more than spread items reordered, just get all the domains in reordered
                domains_to_check = [x.publisher for x in reordered]

            # we can add the rec at iterator position to the re-ordered list if.the rec at iterator has a different
            # domain than the invalid list retrieved above
            if recs[iterator].publisher not in domains_to_check:
                reordered.append(recs.pop(iterator))
                iterator = 0
            else:
                # if we cannot add the rec at position iterator to the re-ordered list, increment the iterator and try
                # the next item in recs
                iterator += 1

        return reordered

    @staticmethod
    @xray_recorder.capture('models_topic_thompson_sample')
    async def thompson_sampling(recs: List[RecommendationModel],
                                module: RecommendationModules) -> List[RecommendationModel]:
        """
        Re-rank items using Thompson sampling which combines exploitation of known item CTR
        with exploration of new items with unknown CTR modeled by a prior

        :param recs: a list of recommendations in the desired order (pre-publisher spread)
        :param module: the name of the module (rec surface) for which we are re-ranking
        :return: a re-ordered version of recs satisfying the spread as best as possible
        """

        # if there are no recommendations, we done
        if not recs:
            return recs

        item_list = [item.item_id for item in recs]
        try:
            # returns a dict with item_id as key and dynamodb row modeled as ClickDataModel
            clk_data = await ClickdataModel.get_clickdata(module, item_list)
            # 'default' is a special key we can use for anything that is missing.
            # The values here aren't actually clicks or impressions,
            # but instead direct alpha and beta parameters for the module CTR prior
            alpha_prior, beta_prior = clk_data['default'].clicks, clk_data['default'].impressions
        except ValueError:
            # indicates no results were returned
            clk_data = {}
            alpha_prior, beta_prior = 0.02, 1.0
        except KeyError:
            # indicates no default was found indicating MLE for module prior failed to converge
            alpha_prior, beta_prior = 0.02, 1.0

        scores = []
        prior = beta(alpha_prior, beta_prior)
        for rec in recs:
            resolved_id = rec.item_id
            d = clk_data.get(resolved_id)
            if d:
                clicks = max(d.clicks + alpha_prior, 1e-18)
                no_clicks = max(d.impressions - d.clicks + beta_prior, 1e-18)
                # sample from posterior for CTR given click data
                score = beta.rvs(clicks, no_clicks)
                scores.append((rec, score))
            else:  # no click data, sample from module prior
                scores.append((rec, prior.rvs()))

        scores.sort(key=itemgetter(1), reverse=True)
        return [x[0] for x in scores]
