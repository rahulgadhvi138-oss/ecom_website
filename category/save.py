import json


def save_categories(filename, categories):

    with open(filename, "w") as file:
        json.dump(categories, file, indent=4)