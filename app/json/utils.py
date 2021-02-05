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
