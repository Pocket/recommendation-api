import json

from jsonschema import validate


def parse_to_dict(json_file: str, schema_file: str) -> dict:
    """
    Ensures that both json_file and schema_file are valid JSON, and that json_file conforms to the schema_file schema.
    Returns a dict from the parsed JSON from json_file.

    :param json_file: path to a json file to validate
    :param schema_file: path to the schema for the specified json_file
    :return: dict representation of parsed JSON from json_file
    """
    # this verifies the json is valid
    with open(json_file) as f:
        parsed_json = json.load(f)

    with open(schema_file) as f:
        parsed_schema = json.load(f)

    # validates against the schema
    validate(parsed_json, parsed_schema)

    return parsed_json


def guid_unique(config_dict, guid_attr="id"):
    guids = [r[guid_attr] for r in config_dict]
    c = Counter(guids)
    for guid, count in c.items():
        if count > 1:
            raise AssertionError(f"{guid} is used {count} times")


if __name__ == "__main__":
    from collections import Counter
    import hashlib
    import argparse
    parser = argparse.ArgumentParser(description="Validate and visualize the RecsAPI configuration")
    parser.add_argument('--full-guids', help="Show full guids rather than the first 7 characters", action='store_true')
    parser.add_argument('--lineup', help="Only show lineups that start with these characters", default=None, type=str)
    args = parser.parse_args()

    layouts = parse_to_dict("slate_lineup_configs.json", "slate_lineup_config.schema.json")
    guid_unique(layouts)

    slates = parse_to_dict("slate_configs.json", "slate_config.schema.json")
    guid_unique(slates)

    if args.full_guids:
        # Print all of the GUID
        guid_len = None
    else:
        # Only print this much of the GUID, reduces visual clutter
        guid_len = 7

    PIPE = "│"
    ELBOW = "└──"
    TEE = "├──"
    PIPE_PREFIX = "│   "
    SPACE_PREFIX = "    "

    def get_pipes(idx, col):
        """Returns the appropriate prefix and connector based on the current `idx` for `col`."""
        if idx + 1 == len(col):
            return SPACE_PREFIX, ELBOW
        else:
            return PIPE_PREFIX, TEE

    def generate_exp_hash(experiment_dict):
        """Code taken from `models/experiment.py` to generate hashes here"""
        return hashlib.sha1(
            json.dumps(experiment_dict, sort_keys=True).encode()
        ).hexdigest()

    PREFIXES = [SPACE_PREFIX] * 3
    slates = {r['id']: r for r in slates}
    for layout in layouts:
        if args.lineup and not layout['id'].startswith(args.lineup):
            continue
        print(f"[{layout['id'][:guid_len]}] {layout['description']}")
        for idx, experiment in enumerate(layout['experiments']):
            s, p = get_pipes(idx, layout['experiments'])
            PREFIXES[0] = s
            exp_hash = generate_exp_hash(experiment)
            print(f"{p} [{exp_hash[:guid_len]}] Experiment: {experiment['description']}")
            for idx, slate_id in enumerate(experiment['slates']):
                s, p = get_pipes(idx, experiment['slates'])
                PREFIXES[1] = s
                print(f"{''.join(PREFIXES[:1])}{p} [{slate_id[:guid_len]}] Slate:  {slates[slate_id]['displayName']}")
                for idx, slate_experiment in enumerate(slates[slate_id]["experiments"]):
                    s,p = get_pipes(idx, slates[slate_id]['experiments'])
                    PREFIXES[2] = s
                    exp_hash = generate_exp_hash(slate_experiment)
                    print(f"{''.join(PREFIXES[:2])}{p} [{exp_hash[:guid_len]}] Experiment: {slate_experiment['description']}")
                    for idx, candidate_set in enumerate(slate_experiment['candidateSets']):
                        s, p = get_pipes(idx, slate_experiment['candidateSets'])
                        print(f"{''.join(PREFIXES[:3])}{p} [{candidate_set[:guid_len]}] Candidate Set")
        print()

