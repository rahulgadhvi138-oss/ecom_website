def update_product(selected_category):

    print("Update Product")

    products = selected_category["products"]

    update_id = int(input("Enter Product ID: "))

    found = False

    for product in products:

        if product["id"] == update_id:

            product["name"] = input("Enter New Product Name: ")
            product["price"] = input("Enter New Product Price: ")

            print("Product Updated!")

            found = True
            break

    if not found:

        print("Product Not Found!")
