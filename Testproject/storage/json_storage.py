import json


def load() -> list[dict]:

    try:

        file = open("categories.json", "r")

        return json.load(file)

    except:

        return []


def save(data):

    file = open("categories.json", "w")

    json.dump(data, file)