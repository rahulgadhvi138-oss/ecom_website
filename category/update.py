def update_category(categories):

    cid = int(input("Enter Category ID: "))

    for category in categories:

        if category["id"] == cid:

            category["name"] = input("Enter New Category Name: ")

            print("Category Updated!")

            return

    print("Category Not Found!")
