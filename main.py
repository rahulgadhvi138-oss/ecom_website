from category.add import add
from category.show import show
from category.update import update
from category.delete import delete


# from product.add import add_product
# from product.show import show_product
# from product.update import update_product
# from product.delete import delete_product
categories = []

while True:

    print("\n===== MAIN MENU =====")
    print("1. Manage Category")
    print("2. Exit")

    choice = int(input("Enter Choice: ")) 
    if choice == 1:

        while True:

                print("\n===== MANAGE CATEGORY =====")
                print("1. Add Category")
                print("2. Show Category")
                print("3. Update Category")
                print("4. Delete Category")
                print("5. Manage Product")
                print("6. Back")

                ch = int(input("Enter Choice: "))

                if ch == 1:
                    add(label="category",lis=categories)

                elif ch == 2:
                    show(label="Category", lis=categories)

                elif ch == 3:
                     update(label="Category", lis=categories)

                elif ch == 4:
                      delete(label="Category", lis=categories)
                 


                elif ch == 5:

                    print("\n===== CATEGORY LIST =====")

                    for i, category in enumerate(categories, start=1):
                       
                        print(i, category["name"])


                    ch = int(input("Enter Your Choice: "))

                    selected_category = categories[ch - 1]
                    for product in selected_category["products"]:
                        print(product)
                    print("[DEBUG]", selected_category)


                    print("\n===== MANAGE PRODUCT =====")
                    print("1. Add Product")
                    print("2. Show Product")
                    print("3. Update Product")
                    print("4. Delete Product")
                    print("5. Back")

                    product_choice = int(input("Enter Your Choice: "))


                    # Add Product
                    if product_choice == 1:
                        print(selected_category)
                        add(label="Product", lis=selected_category["products"])
                        

                    elif product_choice == 2:
                        print(selected_category)
                        show(label="Product", lis=selected_category["products"])


                    # Update Product
                    elif product_choice == 3:

                            update(label="Product", lis=selected_category["products"])


                # Delete Product
                    elif product_choice == 4:

                                delete(label="Product", lis=selected_category["products"])


                    # Back
                    elif product_choice == 5:

                            print("Back TO Manage category:")
                   
                else:

                            print("Invalid Choice")





# Exit
    elif choice == 2:
     print("Program Closed")
    break

else:
    print("Invalid Choice")                                                                                                                                                          