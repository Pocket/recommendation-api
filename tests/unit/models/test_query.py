import sys
import random
from unittest.mock import MagicMock
sys.modules["elasticsearch_dsl.query"] = MagicMock()
sys.modules["elasticsearch_dsl.function"] = MagicMock()
sys.modules["utils"] = MagicMock()

from typing import List, Dict
from jobs.query import postprocess_search_results

class TestQuery:
    @staticmethod
    def generate_elasticsearch_results() -> Dict:
        hits = [{"_source": {"title": "allow this 1",
                 "resolved_id": 111,
                 "domain": {"domain_name": "something.nytimes.com",
                            "top_domain_name": "nytimes.com"}}},
                {"_source": {"title": "allow this 2",
                 "resolved_id": 333,
                 "domain": {"domain_name": "something.theatlantic.com",
                            "top_domain_name": "theatlantic.com"}}},
                {"_source": {"title": "allow this 3",
                 "resolved_id": 555,
                 "domain": {"domain_name": "onlysortabad.things.com",
                            "top_domain_name": "things.com"}}},
                {"_source": {"title": "block this item",
                 "resolved_id": 351, "resolved_url": "",
                 "domain": {"domain_name": "here.nytimes.com",
                            "top_domain_name": "nytimes.com"}}},
                {"_source": {"title": "block this subdomain",
                 "resolved_id": 777,
                 "domain": {"domain_name": "bad.things.com",
                            "top_domain_name": "things.com"}}},
                {"_source": {"title": "block this not allowed",
                 "resolved_id": 354,
                 "domain": {"domain_name": "here.nowhereinparticular.com",
                            "top_domain_name": "nowhereinparticular.com"}}},
                {"_source": {"title": "block this not allowed",
                 "resolved_id": 369,
                 "domain": {"domain_name": "themost.reallybadthings.com",
                            "top_domain_name": "reallybadthings.com"}}},
                {"_source": {"title": "block this subdomain",
                 "resolved_id": 999,
                 "domain": {"domain_name": "themostbad.things.com",
                            "top_domain_name": "things.com"}}}]

        for this in hits:
            this["_score"] = random.random()
            subdomain = this['_source']['domain']['domain_name']
            this["_source"]["resolved_url"] = f"http://{subdomain}/{random.randint(1, 99)}"

        return {"hits": {"hits": hits}}

    @staticmethod
    def generate_lists() -> (Dict, Dict):
        allowlist = {"nytimes.com": 1, "theatlantic.com": 1, "things.com": 1}
        blocklists = dict()
        blocklists["domains"] = {"themost.badthings.com": 1, "bad.things.com": 1}
        blocklists["items"] = {"351": 1}

        return allowlist, blocklists


    def setup_class(self):
        self.hits = self.generate_elasticsearch_results()
        self.allowlist, self.blocklists = self.generate_lists()

    def test_allowlist(self):

        this_blocklist = {"domains": {}, "items": {}}
        final_recs = postprocess_search_results(self.hits, self.allowlist, this_blocklist, 99)

        for hit in final_recs:
            assert hit["rec"]["top_domain_name"] in self.allowlist

    def test_item_blocklist(self):

        this_blocklist = {"domains": {}, "items": self.blocklists["items"]}
        final_recs = postprocess_search_results(self.hits, self.allowlist, this_blocklist, 99)

        for hit in final_recs:
            assert str(hit["rec"]["item_id"]) not in self.blocklists["items"]

    def test_domain_blocklist(self):

        this_blocklist = {"domains": self.blocklists["domains"], "items": {}}
        final_recs = postprocess_search_results(self.hits, self.allowlist, this_blocklist, 99)

        for hit in final_recs:
            subdomain = hit["rec"]["resolved_url"].split("/")[2]
            assert subdomain not in self.blocklists["domains"]

    def test_postprocess_results(self):

        final_recs = postprocess_search_results(self.hits, self.allowlist, self.blocklists, 99)
        for hit in final_recs:
            assert hit["rec"]["top_domain_name"] in self.allowlist
            assert str(hit["rec"]["item_id"]) not in self.blocklists["items"]
            subdomain = hit["rec"]["resolved_url"].split("/")[2]
            assert subdomain not in self.blocklists["domains"]

