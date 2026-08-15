def delete_category(categories):

    cid = int(input("Enter Category ID: "))

    for category in categories:

        if category["id"] == cid:

            ch = input("Delete Category? (y/n): ").lower()

            if ch == "y":

                categories.remove(category)

                print("Category Deleted!")

            return

    print("Category Not Found!")