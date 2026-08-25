from category.save import save_categories
import traceback


def add(label: str, lis: list, filename: str, all_categories=None):

    print("debug 1.")

    try:

        print("debug 2.")

        item = {
            "id": int(input(f"Enter {label} ID: ")),
            "name": input(f"Enter {label} Name: ")
        }

        print("debug 3.")

        if label == "category":

            print("debug 4.")

            item["products"] = []

            print("debug 5.")

        elif label == "Product":

            print("debug 6.")

            item["price"] = float(
                input("Enter Product Price: ")
            )

            print("debug 7.")

        print("debug 8.")

        lis.append(item)

       

        if label == "category":
            save_categories(filename, lis)

        elif label == "Product":
            save_categories(filename, all_categories)

        print(f"{label} Added Successfully!")
        print("----------------------")

    except ValueError:

        print("Please enter a valid number!")

    except Exception as e:

        traceback.print_exc()
        print("Something went wrong:", e)