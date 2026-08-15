# def add_category(categories):

#     category = {
#         "id": int(input("Enter Category ID: ")),
#         "name": input("Enter Category Name: "),
#         "products": []
#     }

#     categories.append(category)

#     print("Category Added Successfully!")









# def add(label: str, lis: list):
#     if len(lis) == 0:
#         print(f"No {label} Found!")

#     else:
#         print(f"\n==== {label.upper()} LIST")

#         for elem in lis:
#             print("[DEBUG] :", elem, type(elem))
#             for key, value in elem.items():
#                 # print(f"[DEBUG] : VALUE - {value}, {isinstance(value, list)}")
#                 if not isinstance(value, list):
#                     print(f"{key.upper()} : {value}")

#             print("----------------------")

def add(label: str, lis: list):

    item = {
        "id": int(input(f"Enter {label} ID: ")),
        "name": input(f"Enter {label} Name: ")
    }

    if label == "category":
        item["products"] = []

    elif label == "Product":
        item["price"] = input("Enter Product Price: ")

    lis.append(item)

    print(f"{label} Added Successfully!")