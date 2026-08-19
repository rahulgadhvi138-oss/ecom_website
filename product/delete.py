# def delete_product(selected_category):

#     print("Delete Product")

#     delete_id = int(input("Enter Product ID: "))

#     products = selected_category["products"]

#     found = False

#     for product in products:

#         if product["id"] == delete_id:

#             products.remove(product)

#             print("Product Deleted!")

#             found = True
#             break

#     if not found:

#         print("Product Not Found!")