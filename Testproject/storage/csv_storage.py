import csv


def load() -> list[dict]:

    try:

        file = open("categories.csv")

        reader = csv.DictReader(file)

        data = []

        for row in reader:

            data.append({
                "id": row["id"],
                "name": row["name"],
                "products": []
            })

        return data

    except:

        return []


def save(data):

    file = open("categories.csv", "w")

    writer = csv.DictWriter(file, fieldnames=["id", "name"])

    writer.writeheader()

    for category in data:

        writer.writerow({
            "id": category["id"],
            "name": category["name"]
        })