def update(label: str, lis: list):
    while True:
        try:
            id = int(input(f"Enter {label} ID: "))
            break
        except:
            print("Give Proper Number")
        

    for item in lis:

        if item["id"] == id:
            print("DEBUG 1.")

            item["name"] = input(f"Enter New {label} Name: ")
            print("DEBUG 2")

            if label == "Product":
                item["price"] = input("Enter New Product Price: ")
                print("DEBUG 3")

            print(f"{label} Updated Successfully!")
            print("----------------------")
            return

        print(f"{label} Not Found!")
        print("----------------------")
        