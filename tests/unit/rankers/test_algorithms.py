import unittest

from tests.unit.utils import generate_recommendations
from app.models.clickdata import ClickdataModel
from app.rankers.algorithms import spread_publishers, top15, top30, thompson_sampling
from operator import itemgetter


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
        assert [x.item_id for x in reordered] == [1, 2, 3, 5, 4, 6, 7, 8]

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
        assert [x.item_id for x in reordered] == [1, 2, 5, 7, 4, 3, 6, 8]

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
        assert [x.item_id for x in reordered] == [1, 2, 3, 4, 6, 5, 7, 8]

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
        assert [x.item_id for x in reordered] == [1, 2, 3, 4, 5, 6, 7, 8]


class TestAlgorithmsTop15(unittest.TestCase):
    def test_get_top_15_items(self):
        recs = generate_recommendations([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])
        top_15 = top15(recs)
        assert [x.item_id for x in top_15] == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

    def test_get_all_items_when_less_than_15(self):
        recs = generate_recommendations([1, 2])
        top_15 = top15(recs)
        assert [x.item_id for x in top_15] == [1, 2]


class TestAlgorithmsTop30(unittest.TestCase):
    def test_get_top_30_items(self):
        recs = generate_recommendations(
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25,
             26, 27, 28, 29, 30, 31])
        top_30 = top30(recs)
        assert [x.item_id for x in top_30] == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
                                               21, 22, 23, 24, 25,
                                               26, 27, 28, 29, 30]

    def test_get_all_items_when_less_than_30(self):
        recs = generate_recommendations([1, 2])
        top_30 = top30(recs)
        assert [x.item_id for x in top_30] == [1, 2]


class TestAlgorithmsThompsonSampling(unittest.TestCase):
    def test_thompson_sampling(self):
        recs = generate_recommendations(["333", "666", "999"])

        click_data = {
            "999": ClickdataModel.parse_obj({
                "mod_item": "home/999",
                "clicks": "99",
                "impressions": "999",
                "created_at": "0",
                "expires_at": "0"
            }),
            "666": ClickdataModel.parse_obj({
                "mod_item": "home/666",
                "clicks": "66",
                "impressions": "999",
                "created_at": "0",
                "expires_at": "0"
            }),
            "333": ClickdataModel.parse_obj({
                "mod_item": "home/333",
                "clicks": "33",
                "impressions": "999",
                "created_at": "0",
                "expires_at": "0"
            })
        }

        sampled_recs = thompson_sampling(recs, click_data)
        assert [item.item_id for item in sampled_recs] == ["999", "666", "333"]

    def test_it_can_rank_items_with_missing_click_data(self):
        recs = generate_recommendations(["333", "999"])

        click_data = {
            "999": ClickdataModel.parse_obj({
                "mod_item": "home/999",
                "clicks": "99",
                "impressions": "999",
                "created_at": "0",
                "expires_at": "0"
            }),
        }

        sampled_recs = thompson_sampling(recs, click_data)
        assert [item.item_id for item in sampled_recs] == ["999", "333"]

    # Moved from a previous thompson sampling test file
    def test_rank_by_ctr_over_n_trials(self):
        recs = generate_recommendations(["333333", "666666", "999999", "222222"])

        click_data = {
            "999999": ClickdataModel.parse_obj({
                "mod_item": "home/999999",
                "clicks": "99",
                "impressions": "999",
                "created_at": "0",
                "expires_at": "0"
            }),
            "666666": ClickdataModel.parse_obj({
                "mod_item": "home/666666",
                "clicks": "66",
                "impressions": "999",
                "created_at": "0",
                "expires_at": "0"
            }),
            "333333": ClickdataModel.parse_obj({
                "mod_item": "home/333333",
                "clicks": "33",
                "impressions": "999",
                "created_at": "0",
                "expires_at": "0"
            })
        }

        # goal of test is to rank by CTR over ntrials
        # order should be 999999, 666666, 333333
        ntrials = 36
        ranks = dict()
        for i in range(ntrials):
            sampled_recs = thompson_sampling(recs, click_data)
            c = 1
            for rec in sampled_recs:
                # compute average positional rank over the trials
                ranks[rec.item_id] = ranks.get(rec.item_id, 0) + (c / ntrials)
                c += 1

        final_ranks = sorted(ranks.items(), key=itemgetter(1))

        assert final_ranks[0][0] == "999999"
        assert final_ranks[1][0] == "666666"
        assert final_ranks[2][0] == "333333"
        # click data here should sample from default prior a = 0.02 b = 1, mean = 0.019
        assert final_ranks[3][0] == "222222"

        # ranks are not deterministic
        assert (1 < ranks["999999"] < 2)
        assert (2 < ranks["666666"] < 3)
        assert (3 < ranks["333333"] < 4)
        # final_ranks["222222"] is reliably in [3.7, 3.9] but I haven't figured out
        # the actual confidence interval for the ranks
        # the scores themselves aren't coming back from thompson_sampling because I am using
        # RecommendationModel for the recs
        assert (ranks["222222"] > 3.5 and ranks["222222"] > ranks["333333"])
