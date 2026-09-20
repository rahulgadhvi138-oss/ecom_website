from storage.router import load, save

categories = load()


def add_category(category: dict) -> dict:

    category["id"] = len(categories) + 1

    category["products"] = []

    categories.append(category)

    save(categories)

    return category


def get_all_categories():

    return categories