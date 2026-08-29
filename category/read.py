import json


def read_categories(filename):
    try:
        with open(filename, "r") as file:
            categories = json.load(file)

        return categories

    except FileNotFoundError:
        return []