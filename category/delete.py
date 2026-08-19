def delete(label: str, lis: list):

    id = int(input(f"Enter {label} ID: "))

    for item in lis:

        if item["id"] == id:

            item["name"] = input(f"Enter New {label} Name: ")

            if label == "Product":
                item["price"] = input("Enter New Product Price: ")

            print(f"{label} Updated Successfully!")
            print("----------------------")
            return

    print(f"{label} Not Found!")
    print("----------------------")