from services.categories_services import add_category, get_all_categories

categories = []

def main():
    print('1.Manage Category\n2.Exit')
    ch = int(input("Enter Choice : "))

    loop = True
    while loop:
        if ch == 1:
            print('1.Add \n 2. Show \n 3.Back')
            ch2 = int(input("Enter Choice : "))

            while ch2 != 3:
                if ch2 == 1:
                    name: str = input("Enter category name: ")

                    category: dict = add_category(
                        category={"name": name}
                    )

                    print(f"{category['id']}.{category['name']} is added.")

                elif ch2 == 2:
                    for c in get_all_categories():
                        print(f"{c['id']}. {c['name']}")

                else:
                    print("Enter valid Choice")
                    print()
                    print()

                print('1.Add \n 2. Show \n 3.Back')
                ch2 = int(input("Enter Choice : "))

        elif ch == 2:
            break

        else:
            print("enter valid input")

        print('1.Manage Category\n2.Exit')
        ch = int(input("Enter Choice : "))


if "__main__" == "__main__":
    main()