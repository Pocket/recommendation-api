import unittest

from unittest.mock import patch

from tests.unit.utils import generate_recommendations, generate_curated_configs
from app.models.clickdata import ClickdataModel
from app.rankers.algorithms import spread_publishers, top5, top15, top30, thompson_sampling, blocklist, \
    personalize_topic_slates
from operator import itemgetter

full_topic_profile = [
    ['Technology', 0.4916270776467738],
    ['Science', 0.4845668326438052],
    ['Self Improvement', 0.4463882336654731],
    ['Career', 0.41259960307038374],
    ['Education', 0.4110607340266076],
    ['Health & Fitness', 0.31604288482458914],
    ['Personal Finance', 0.28910082153539796],
    ['Parenting', 0.2833301590363405],
    ['Business', 0.27844981711121575],
    ['Gaming', 0.27776708204470507],
    ['Politics', 0.2743746579183603],
    ['COVID-19', 0.25085116435066945],
    ['Food', 0.2216703950294493],
    ['Travel', 0.22115116728502504],
    ['Entertainment', 0.20847503562410932],
    ['Sports', 0.10392396923948377]
]

partial_topic_profile = [
    ["Science", 0.4804642592376828 ],
    ["Technology", 0.4215351739562764 ],
    ["Self Improvement", 0.4131880414914616 ],
    ["Education", 0.40942187714103623 ],
    ["Career", 0.36788070441792387 ],
    ["Politics", 0.3082215581232689 ],
    ["Personal Finance", 0.29735881866754704],
    ["Health & Fitness", 0.29727509873834246 ],
    ["Gaming", 0.2748425948728629 ],
    ["COVID-19", 0.2557075404515359 ] ]

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
    def test_it_can_rank_items_with_missing_click_data(self):
        recs = generate_recommendations(['333', '999'])

        click_data = {
            '999': ClickdataModel.parse_obj({
                'mod_item': 'home/999',
                'clicks': '99',
                'impressions': '999',
                'created_at': '0',
                'expires_at': '0'
            }),
        }

        sampled_recs = thompson_sampling(recs, click_data)
        # this needs to be a set since order isn't guaranteed in single trial
        assert {item.item_id for item in sampled_recs} == {"999", "333"}

    def test_invalid_prior(self):
        recs = generate_recommendations(['999'])
        click_data = {
            'default': ClickdataModel.parse_obj({
                'mod_item': 'home/default',
                'clicks': '99',
                'impressions': '-14',
                'created_at': '0',
                'expires_at': '0'
            }),
        }

        sampled_recs = thompson_sampling(recs, click_data)
        # this needs to be a set since order isn't guaranteed in single trial
        assert {item.item_id for item in sampled_recs} == {"999"}

    # Moved from a previous thompson sampling test file
    def test_rank_by_ctr_over_n_trials(self, ntrials=99):
        """
        This routine tests the Thompson sampling ranker by
        aggregating results over multiple trials.  In a single run of the
        ranker results may not be ordered by CTR, but over multiple trials the
        ranks converge to descending by CTR
        :param ntrails is the number of trials for the aggregation
        """
        recs = generate_recommendations(["333333", "666666", "999999", "222222"])

        click_data = {
            '999999': ClickdataModel.parse_obj({
                'mod_item': 'home/999999',
                'clicks': '99',
                'impressions': '999',
                'created_at': '0',
                'expires_at': '0'
            }),
            '666666': ClickdataModel.parse_obj({
                'mod_item': 'home/666666',
                'clicks': '66',
                'impressions': '999',
                'created_at': '0',
                'expires_at': '0'
            }),
            '333333': ClickdataModel.parse_obj({
                'mod_item': 'home/333333',
                'clicks': '33',
                'impressions': '999',
                'created_at': '0',
                'expires_at': '0'
            })
        }

        # goal of test is to rank by CTR over ntrials
        # order should be 999999, 666666, 333333
        ranks = dict()
        for i in range(ntrials):
            sampled_recs = thompson_sampling(recs, click_data)
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

    @patch('app.rankers.algorithms.get_personalized_topics', return_value=partial_topic_profile)
    async def test_partial_recit_response(self):

        input_configs = generate_curated_configs()
        ordered_input_ids = [c.id for c in input_configs]
        input_topics = [c.curator_topic_label for c in input_configs]
        personalized_topics = [t[0] for t in partial_topic_profile if t[0] in input_topics]

        output_configs = await personalize_topic_slates(input_configs, "1234")
        ordered_output_ids = [c.id for c in output_configs]
        ordered_output_topics = [c.curator_topic_label for c in output_configs]

        # COVID-19 is not in input_configs
        # test re-ranking
        assert ordered_output_topics[:len(personalized_topics)] == personalized_topics
        # test that all input slates are in output
        assert set(ordered_input_ids) == set(ordered_output_ids)

    @patch('app.rankers.algorithms.get_personalized_topics', return_value=full_topic_profile)
    async def test_rerank(self):

        input_configs = generate_curated_configs()
        ordered_input_ids = [c.id for c in input_configs]
        input_topics = [c.curator_topic_label for c in input_configs]
        personalized_topics = [t[0] for t in full_topic_profile if t[0] in input_topics]

        output_configs = await personalize_topic_slates(input_configs, "5678")
        ordered_output_ids = [c.id for c in output_configs]
        ordered_output_topics = [c.curator_topic_label for c in output_configs]

        assert ordered_output_topics[:len(full_topic_profile)-1] == personalized_topics
        # test that all input slates are in output
        assert set(ordered_input_ids) == set(ordered_output_ids)





