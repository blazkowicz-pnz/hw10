import json


def load_data_from_json():
    with open("data.json", "r", encoding="utf-8") as file:
        data = json.load(file)
    return data

