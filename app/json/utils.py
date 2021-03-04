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
    print("Validating layout_configs.json")
    layouts = parse_to_dict("slate_lineup_configs.json", "slate_lineup_config.schema.json")
    guid_unique(layouts)

    print("Validating slate_config.json")
    slates = parse_to_dict("slate_configs.json", "slate_config.schema.json")
    guid_unique(slates)

    slates = {r['id']: r for r in slates}
    for layout in layouts:
        print(f"Lineup: {layout['id']} {layout['description']}")
        for experiment in layout['experiments']:
            print(f"- Experiment: {experiment['description']}")
            for slate_id in experiment['slates']:
                print(f"-- Slate: {slate_id} {slates[slate_id]['displayName']}")
                for slate_experiment in slates[slate_id]["experiments"]:
                    print(f"--- Experiment: {slate_experiment['description']}")
                    for candidate_set in slate_experiment['candidateSets']:
                        print(f"---- Candidate Set: {candidate_set}")
        print()

