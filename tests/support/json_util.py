import json


def read_json(filepath) -> dict:
    with open(filepath, encoding='utf8') as json_file:
        data = json.load(json_file)
    return data


def json_pretty(json_obj):
    if type(json_obj) is dict:
        json_obj = json.dumps(json_obj)
    json_to_convert = json.loads(json_obj)
    _json_pretty = json.dumps(json_to_convert, indent=2, sort_keys=True)
    return _json_pretty


def write_json(file_path, dictionary):
    with open(file_path, "wb") as f:
        f.write(json.dumps(dictionary).encode("uft-8"))

