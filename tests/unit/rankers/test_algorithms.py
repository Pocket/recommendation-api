import posixpath
import unittest
import os
import json

from app.models.metrics.metrics_model import MetricsModel
from tests.unit.utils import generate_recommendations, generate_curated_configs, generate_nontopic_configs, generate_lineup_configs
from app.config import ROOT_DIR
from app.rankers.algorithms import spread_publishers, top5, top15, top30, thompson_sampling, rank_topics, \
    thompson_sampling_1day, thompson_sampling_7day, thompson_sampling_14day, blocklist, top1_topics, top3_topics
from app.models.personalized_topic_list import PersonalizedTopicList, PersonalizedTopicElement
from app.models.slate_lineup_config import SlateLineupConfigModel
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


class TestAlgorithmsThompsonSampling(unittest.TestCase):
    def test_it_can_rank_items_with_missing_metrics(self):
        recs = generate_recommendations(['333', '999'])

        metrics = {
            '999': MetricsModel(
                id='home/999',
                trailing_1_day_opens=0,
                trailing_1_day_impressions=0,
                trailing_7_day_opens=0,
                trailing_7_day_impressions=0,
                trailing_14_day_opens=0,
                trailing_14_day_impressions=0,
                trailing_28_day_opens=99,
                trailing_28_day_impressions=999,
                created_at=0,
                expires_at=0
            ),
        }

        sampled_recs = thompson_sampling(recs, metrics)
        # this needs to be a set since order isn't guaranteed in single trial
        assert {item.item_id for item in sampled_recs} == {"999", "333"}

    def test_invalid_prior(self):
        recs = generate_recommendations(['999'])
        metrics = {
            'default': MetricsModel(
                id='home/default',
                trailing_1_day_opens=0,
                trailing_1_day_impressions=0,
                trailing_7_day_opens=0,
                trailing_7_day_impressions=0,
                trailing_14_day_opens=0,
                trailing_14_day_impressions=0,
                trailing_28_day_opens=99,
                trailing_28_day_impressions=-14,
                created_at=0,
                expires_at=0,
            ),
        }

        sampled_recs = thompson_sampling(recs, metrics)
        # this needs to be a set since order isn't guaranteed in single trial
        assert {item.item_id for item in sampled_recs} == {"999"}

    # Moved from a previous thompson sampling test file
    def test_rank_by_ctr_over_n_trials(self, ntrials=99):
        """
        This routine tests the Thompson sampling ranker by
        aggregating results over multiple trials.  In a single run of the
        ranker results may not be ordered by CTR, but over multiple trials the
        ranks converge to descending by CTR
        :param ntrials is the number of trials for the aggregation
        """

        all_time_windows = [1, 7, 14, 28]

        recs = generate_recommendations(["333333", "666666", "999999", "222222"])

        for current_window in all_time_windows:

            open_attr = f"trailing_{current_window}_day_opens"

            metrics = dict()
            for item_id in ["999999", "666666", "333333"]:

                opens = int(item_id[:2])
                metrics[item_id] = MetricsModel.parse_obj(dict(id=f"home/{item_id}",
                             trailing_1_day_opens=(opens * int(open_attr == "trailing_1_day_opens")),
                             trailing_1_day_impressions=999,
                             trailing_7_day_opens=(opens * int(open_attr == "trailing_7_day_opens")),
                             trailing_7_day_impressions=999,
                             trailing_14_day_opens=(opens * int(open_attr == "trailing_14_day_opens")),
                             trailing_14_day_impressions=999,
                             trailing_28_day_opens=(opens * int(open_attr == "trailing_28_day_opens")),
                             trailing_28_day_impressions=999,
                             created_at=0,
                             expires_at=0))


            # goal of test is to rank by CTR over ntrials
            # order should be 999999, 666666, 333333
            ranks = {}
            for i in range(ntrials):
                if current_window == 1:
                    sampled_recs = thompson_sampling_1day(recs, metrics)
                elif current_window == 7:
                    sampled_recs = thompson_sampling_7day(recs, metrics)
                elif current_window == 14:
                    sampled_recs = thompson_sampling_14day(recs, metrics)
                else:
                    sampled_recs = thompson_sampling(recs, metrics)
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
