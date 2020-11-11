import numpy as np

from scipy.sparse import csr_matrix, hstack


def apply_NB_model(candidates, clf_model, featurizer):
    """
    this routine applies a generic binary NB model that uses the title text, google categories,
    and publisher domain information as features.  it is used for both topic prediction
    and approval prediction
    :param candidates: initial candidate list of dicts with item info in nested dict with key "rec"
    :param clf_model: ranking model trained offline
    :param featurizer: tokenizer for text, and 1-hot mappings for publishers and google categories
    :return:  probabilities per hit of NB model's positive class
    """
    model_vectorizer = featurizer["vectorizer"]
    model_pub_map = featurizer["publisher_mapping"]
    model_gc_map = featurizer["google_category_mapping"]

    npubs = len(model_pub_map)
    ngcats = len(model_gc_map)
    one_hot_domain = list()
    gc_features = list()
    title_data = list()
    for i, rec in enumerate(candidates):
        hit = rec["rec"]
        gc_features.append(np.zeros(ngcats))
        # scoring by google category frequency weights (normalized per category)
        if "google_categories" in hit:
            # create google tag features for approval prediction
            for gc, gc_score in hit["google_categories"].items():
                if gc in model_gc_map:
                    gc_features[-1][model_gc_map[gc]] = gc_score

        # create features per hit for approval prediction
        title_data.append(hit["title"])
        one_hot_domain.append(np.zeros(npubs))
        if hit["top_domain_name"] in model_pub_map:
            one_hot_domain[-1][model_pub_map[hit["top_domain_name"]]] = 1.0
        else:
            one_hot_domain[-1][model_pub_map["other"]] = 1.0

    # assume this is faster than apply model one sample at a time in loop
    # diminishing returns for small # of items?
    one_hot_domain = csr_matrix(np.array(one_hot_domain))
    gc_features = csr_matrix(np.array(gc_features))
    title_data = np.array(title_data)
    approval_preds = clf_model.predict_proba(hstack((model_vectorizer.transform(title_data),
                                                     one_hot_domain,
                                                     gc_features)))[:, 1]

    return approval_preds


def apply_rankers(search_results, topic_predictor, approval_model, count, featurizer):
    """
    This routine applies the topic prediction model and curator approval model
    to search results for a single topic
    :param search_results: search results from elastic search
    :param topic_predictor: the NB classifier to predict topic membership
    :param approval_model: the NB classifier to predict curator approval
    :param count: the desired number of items
    :param featurizer: contains information for generating features per item
    :return:
    """
    topic_probs = apply_NB_model(search_results, topic_predictor, featurizer)

    # add topic scores to search results
    rlist = [dict(hit, **{"topic_score": topic_probs[i]}) for i, hit in enumerate(search_results)]

    ordered_hits = sorted(rlist, key=lambda x: x["topic_score"], reverse=True)
    # remove low ranked items
    ordered_hits = ordered_hits[:(count * 2)]

    approval_preds = apply_NB_model(ordered_hits, approval_model, featurizer)

    # add approval scores to search results
    approval_th = np.percentile(approval_preds, 20)
    for approval_prob, hit in zip(approval_preds, ordered_hits):
        hit["approval_score"] = approval_prob
        hit["final_score"] = int(approval_prob > approval_th) * hit["es_score"]

    reordered_hits = sorted(ordered_hits, key=lambda x: x["final_score"], reverse=True)
    final_results = list()
    for hit in reordered_hits:
        final_results.append({"item_id": hit["rec"]["item_id"], "publisher": hit["rec"]["top_domain_name"],
                              "feed_id": hit["rec"]["feed_id"]})
        if len(final_results) >= count:
            break

    return final_results
