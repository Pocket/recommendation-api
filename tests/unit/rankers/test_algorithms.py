import unittest
import os
import json

import pytest

from tests.assets.engagement_metrics import generate_metrics, generate_firefox_metrics, generate_metrics_model_dict
from tests.unit.utils import generate_recommendations, generate_curated_configs, generate_nontopic_configs, generate_lineup_configs
from app.config import ROOT_DIR
from app.rankers.algorithms import spread_publishers, top5, top15, top30, thompson_sampling, rank_topics, \
    thompson_sampling_1day, thompson_sampling_7day, thompson_sampling_14day, blocklist, top1_topics, top3_topics, \
    firefox_thompson_sampling_1day, user_impression_filter
from app.models.personalized_topic_list import PersonalizedTopicList, PersonalizedTopicElement
from operator import itemgetter

ANDROID_DISCOVER_LINEUP_ID = "b50524d6-4df9-4f15-a0d0-13ccc8bdf4ed"
WEB_HOME_LINEUP_ID = "05027beb-0053-4020-8bdc-4da2fcc0cb68"


class TestAlgorithmsSpreadPublishers(unittest.TestCase):
    def test_spread_publishers_single_reorder(self):
        recs = generate_recommendations([1, 2, 3, 4, 5, 6, 7, 8])
        recs[0].publisher = 'thedude.com'
        recs[1].publisher = 'walter.com'
        recs[2].publisher = 'donnie.com'
        recs[3].publisher = 'thedude.com'
        recs[4].publisher = 'innout.com'
        recs[5].publisher = 'bowling.com'
        recs[6].publisher = 'walter.com'
        recs[7].publisher = 'abides.com'

        reordered = spread_publishers(recs, 3)

        # ensure the elements are re-ordered in the way we expect

        # this domain check is redundant, but it's kind of a nice illustration of what we expect and is easier
        # to read than the item ids, so i'm leaving it
        assert [x.publisher for x in reordered] == ['thedude.com', 'walter.com', 'donnie.com', 'innout.com',
                                                    'thedude.com', 'bowling.com', 'walter.com', 'abides.com']
        assert [x.item.item_id for x in reordered] == ['1', '2', '3', '5', '4', '6', '7', '8']

    def test_spread_publishers_multiple_reorder(self):
        recs = generate_recommendations([1, 2, 3, 4, 5, 6, 7, 8])
        recs[0].publisher = 'thedude.com'
        recs[1].publisher = 'walter.com'
        recs[2].publisher = 'walter.com'
        recs[3].publisher = 'thedude.com'
        recs[4].publisher = 'innout.com'
        recs[5].publisher = 'innout.com'
        recs[6].publisher = 'donnie.com'
        recs[7].publisher = 'abides.com'

        reordered = spread_publishers(recs, 3)

        # ensure the elements are re-ordered in the way we expect

        # this domain check is redundant, but it's kind of a nice illustration of what we expect and is easier
        # to read than the item ids, so i'm leaving it
        assert [x.publisher for x in reordered] == ['thedude.com', 'walter.com', 'innout.com', 'donnie.com',
                                                    'thedude.com', 'walter.com', 'innout.com', 'abides.com']
        assert [x.item.item_id for x in reordered] == ['1', '2', '5', '7', '4', '3', '6', '8']

    def test_spread_publishers_give_up_at_the_end(self):
        recs = generate_recommendations([1, 2, 3, 4, 5, 6, 7, 8])
        recs[0].publisher = 'thedude.com'
        recs[1].publisher = 'abides.com'
        recs[2].publisher = 'walter.com'
        recs[3].publisher = 'donnie.com'
        recs[4].publisher = 'donnie.com'
        recs[5].publisher = 'innout.com'
        recs[6].publisher = 'donnie.com'
        recs[7].publisher = 'innout.com'

        reordered = spread_publishers(recs, 3)

        # ensure the elements are re-ordered in the way we expect

        # if the number of elements at the end of the list cannot satisfy the spread, we give up and just append
        # the remainder
        assert [x.item.item_id for x in reordered] == ['1', '2', '3', '4', '6', '5', '7', '8']

    def test_spread_publishers_cannot_spread(self):
        """if we don't have enough variance in publishers, spread can't happen"""
        recs = generate_recommendations([1, 2, 3, 4, 5, 6, 7, 8])
        recs[0].publisher = 'thedude.com'
        recs[1].publisher = 'abides.com'
        recs[2].publisher = 'donnie.com'
        recs[3].publisher = 'donnie.com'
        recs[4].publisher = 'thedude.com'
        recs[5].publisher = 'thedude.com'
        recs[6].publisher = 'abides.com'
        recs[7].publisher = 'donnie.com'

        reordered = spread_publishers(recs, 3)

        # ensure the elements aren't reordered at all (as we don't have enough publisher variance)
        assert [x.item.item_id for x in reordered] == ['1', '2', '3', '4', '5', '6', '7', '8']


class TestAlgorithmsTop5(unittest.TestCase):
    def test_get_top_5_items(self):
        recs = generate_recommendations([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])
        top_5 = top5(recs)
        assert [x.item.item_id for x in top_5] == ['1', '2', '3', '4', '5']

    def test_get_all_items_when_less_than_5(self):
        recs = generate_recommendations([1, 2])
        top_5 = top5(recs)
        assert [x.item.item_id for x in top_5] == ['1', '2']


class TestAlgorithmsTop15(unittest.TestCase):
    def test_get_top_15_items(self):
        recs = generate_recommendations([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])
        top_15 = top15(recs)
        assert [x.item.item_id for x in top_15] == ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13',
                                                    '14', '15']

    def test_get_all_items_when_less_than_15(self):
        recs = generate_recommendations([1, 2])
        top_15 = top15(recs)
        assert [x.item.item_id for x in top_15] == ['1', '2']


class TestAlgorithmsTop30(unittest.TestCase):
    def test_get_top_30_items(self):
        recs = generate_recommendations(
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25,
             26, 27, 28, 29, 30, 31])
        top_30 = top30(recs)
        assert [x.item.item_id for x in top_30] == ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13',
                                                    '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24',
                                                    '25', '26', '27', '28', '29', '30']

    def test_get_all_items_when_less_than_30(self):
        recs = generate_recommendations([1, 2])
        top_30 = top30(recs)
        assert [x.item.item_id for x in top_30] == ['1', '2']


class TestAlgorithmsBlocklist(unittest.TestCase):
    def test_block_item_using_blocklist_file(self):
        recs = generate_recommendations([1, 2, 3203292423, 99, 999])
        filtered = blocklist(recs)
        assert [x.item.item_id for x in filtered] == ['1', '2', '99', '999']

    def test_block_item_using_blocklist_param(self):
        recs = generate_recommendations([1, 2, 33, 66, 99, 999])
        filtered = blocklist(recs, blocklist=['2', '99'])
        assert [x.item.item_id for x in filtered] == ['1', '33', '66', '999']


class TestAlgorithmsThompsonSampling:

    def test_it_can_rank_items_with_missing_metrics(self):
        recs = generate_recommendations(['333', '999'])

        metrics = generate_metrics_model_dict(
            id='home/999',
            trailing_28_day_opens=99,
            trailing_28_day_impressions=999,
        )

        sampled_recs = thompson_sampling(recs, metrics)
        # this needs to be a set since order isn't guaranteed in single trial
        assert {item.item_id for item in sampled_recs} == {"999", "333"}

    def test_invalid_prior(self):
        recs = generate_recommendations(['999'])
        metrics = generate_metrics_model_dict(
            id = 'home/default',
            trailing_28_day_opens=99,
            trailing_28_day_impressions=-14,
        )

        sampled_recs = thompson_sampling(recs, metrics)
        # this needs to be a set since order isn't guaranteed in single trial
        assert {item.item_id for item in sampled_recs} == {"999"}

    def test_invalid_trailing_period(self):
        """
        An exception should be raised is the trailing period does not exist on any metrics model
        :return:
        """
        # Invalid trailing_period
        with pytest.raises(ValueError):
            thompson_sampling(
                generate_recommendations(['999']),
                metrics=generate_metrics_model_dict(),
                trailing_period=123  # Model does not have 123 day trailing metrics
            )
        # Invalid trailing_period for Firefox New Tab metrics
        with pytest.raises(ValueError):
            thompson_sampling(
                generate_recommendations(['000-999']),
                metrics=generate_firefox_metrics(['000-999']),
                trailing_period=7  # MetricsModel has 7 day trailing period, but FirefoxNewTabMetricsModel does not.
            )

    @pytest.mark.parametrize("thompson_sampling_function,metrics", [
        (thompson_sampling, generate_metrics(28)),  # 28 day is the default
        (thompson_sampling_1day, generate_metrics(1)),
        (thompson_sampling_7day, generate_metrics(7)),
        (thompson_sampling_14day, generate_metrics(14)),
        (firefox_thompson_sampling_1day, generate_firefox_metrics(["333333", "666666", "999999"])),
    ])
    def test_rank_by_ctr_over_n_trials(self, thompson_sampling_function, metrics, ntrials = 99):
        """
        This routine tests the Thompson sampling ranker by
        aggregating results over multiple trials.  In a single run of the
        ranker results may not be ordered by CTR, but over multiple trials the
        ranks converge to descending by CTR
        :param ntrials is the number of trials for the aggregation
        """

        recs = generate_recommendations(["333333", "666666", "999999", "222222"])

        # goal of test is to rank by CTR over ntrials
        # order should be 999999, 666666, 333333
        ranks = {}
        for i in range(ntrials):
            sampled_recs = thompson_sampling_function(recs, metrics)
            c = 1
            for rec in sampled_recs:
                # compute average positional rank over the trials
                ranks[rec.item.item_id] = ranks.get(rec.item.item_id, 0) + (c / ntrials)
                c += 1

        final_ranks = sorted(ranks.items(), key=itemgetter(1))

        assert final_ranks[0][0] == '999999'
        assert final_ranks[1][0] == '666666'
        assert final_ranks[2][0] == '333333'
        # click data here should sample from default prior a = 0.02 b = 1, mean = 0.019
        assert final_ranks[3][0] == '222222'

        # ranks are not deterministic
        assert int(ranks['999999']) != ranks['999999']
        assert int(ranks['666666']) != ranks['666666']
        assert int(ranks['333333']) != ranks['333333']
        assert int(ranks['222222']) != ranks['222222']


class TestAlgorithmsPersonalizeTopics(unittest.TestCase):

    @staticmethod
    def _read_json_asset(filename: str):
        with open(os.path.join(ROOT_DIR, 'tests/assets/json/', filename)) as f:
            response = json.load(f)
        personalized_topics = [PersonalizedTopicElement(curator_topic_label=x[0], score=x[1])
                               for x in response["curator_topics"]]
        return PersonalizedTopicList(curator_topics=personalized_topics, user_id="3636")


    def test_personalize_topic_limit(self):
        full_topic_profile = self._read_json_asset("recit_full_user_profile.json")
        input_configs = generate_curated_configs()
        input_topics = [c.curator_topic_label for c in input_configs]
        # these are already sorted by RecIt
        personalized_topics = [t.curator_topic_label
                               for t in full_topic_profile.curator_topics
                               if t.curator_topic_label in input_topics]

        for test_limit, topic_ranker in zip([1, 3, None], [top1_topics, top3_topics, rank_topics]):
            if test_limit:
                num_pers_topics = test_limit
            else:
                num_pers_topics = len(personalized_topics)
            output_configs = topic_ranker(input_configs, full_topic_profile)
            ordered_output_topics = [c.curator_topic_label for c in output_configs]
            assert len(output_configs) == num_pers_topics
            assert ordered_output_topics == personalized_topics[:test_limit]

    def test_hybrid_lineups(self):
        ''' this test is the case where one topic slate is returned from a
        lineup with a mix of curated and uncurated slates
        '''
        full_topic_profile = self._read_json_asset("recit_full_user_profile.json")
        personalized_topics = [x.curator_topic_label for x in full_topic_profile.curator_topics]

        for lineup_id in [ANDROID_DISCOVER_LINEUP_ID, WEB_HOME_LINEUP_ID]:
            input_configs, description = generate_lineup_configs(lineup_id)
            non_topic_slots = [i for i, c in enumerate(input_configs) if c.curator_topic_label is None]
            topic_slates = [c.curator_topic_label for c in input_configs if c.curator_topic_label]
            num_topic_slates = len(topic_slates)
            # these are already sorted by RecIt
            first_personalizable_slot = min(set(range(len(input_configs))).difference(set(non_topic_slots)))
            other_slates_before = [t for i,t in enumerate(input_configs)
                                   if t.curator_topic_label is None and i < first_personalizable_slot]
            # this assumes topic slates are contiguous in lineup
            other_slates_after = [t for i,t in enumerate(input_configs)
                                  if t.curator_topic_label is None and i > first_personalizable_slot]

            print("Testing: ", description)

            for topic_limit, topic_ranker in zip([1, 3, None], [top1_topics, top3_topics, rank_topics]):
                print(f"first personalizable lineup slot is {first_personalizable_slot}, topic limit is {topic_limit}")
                if topic_limit:
                    num_pers_topics = topic_limit
                else:
                    num_pers_topics = num_topic_slates
                # one non-topic slate should be at start of lineup
                output_configs = topic_ranker(input_configs, full_topic_profile)
                ordered_output_topics = [c.curator_topic_label for c in output_configs]


                assert len(output_configs) == len(other_slates_before) + num_pers_topics + len(other_slates_after)
                # if non-personalizable slates are first they should preserve their positions
                assert output_configs[:len(other_slates_before)] == other_slates_before
                # returned topic slates should be highest ranked, but only include topics that are in the lineup
                assert ordered_output_topics[first_personalizable_slot:first_personalizable_slot+num_pers_topics] == [t for t in personalized_topics if t in topic_slates][:topic_limit]
                # check any trailing slates that are also not personalizable
                assert output_configs[(first_personalizable_slot + num_pers_topics):] == other_slates_after

    def test_no_topic_slates(self):
        full_topic_profile = self._read_json_asset("recit_full_user_profile.json")
        input_configs = generate_nontopic_configs()

        for topic_ranker in [top1_topics, top3_topics, rank_topics]:
            self.assertRaises(ValueError, topic_ranker, input_configs, full_topic_profile)


class TestAlgorithmsImpressionFilter(unittest.TestCase):

    def test_impression_filter_remove(self):
        item_ids = ["234", "345", "456"]
        recs = generate_recommendations(item_ids)
        impressed_items = [123, 456, 999]

        filtered_recs = user_impression_filter(recs, impressed_items)

        # check for filtering of impressed items
        filtered_item_ids = [r.item_id for r in filtered_recs]
        for i in impressed_items:
            assert i not in filtered_item_ids

        # check for presence of unfiltered items
        for i in recs:
            if int(i.item_id) not in impressed_items:
                assert i.item_id in filtered_item_ids

    def test_no_impressed_list(self):

        item_ids = ["234", "345", "456"]
        recs = generate_recommendations(item_ids)
        filtered_recs = user_impression_filter(recs, [])

        # check for presence of original items
        assert recs == filtered_recs


    def test_no_overlap(self):

        item_ids = ["234", "345", "456"]
        impressed_item_ids = [9*int(i) for i in item_ids]
        recs = generate_recommendations(item_ids)
        filtered_recs = user_impression_filter(recs, impressed_item_ids)

        # check for presence of original items
        assert recs == filtered_recs

