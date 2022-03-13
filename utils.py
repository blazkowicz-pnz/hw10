import json
from pprint import pprint

def load_data_from_json():
    with open("data.json", "r", encoding="utf-8") as file:
        data = json.load(file)
        candidates = {}
        for d in data:
            candidates[d["id"]] = d
    return candidates



