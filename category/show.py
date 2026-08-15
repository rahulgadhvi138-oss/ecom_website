def show(label: str, lis: list):

    if len(lis) == 0:
        print(f"No {label} Found!")

    else:
        print(f"\n==== {label.upper()} LIST ====")

        for elem in lis:

            for key, value in elem.items():

                if not isinstance(value, list):
                    print(f"{key.upper()} : {value}")

            print("----------------------")




# def show(label: str, lis: list):

#     if len(lis) == 0:
#         print(f"No {label} Found!")

#     else:
#         print(f"\n==== {label.upper()} LIST ====")

#         for elem in lis:  

#             for key, value in elem.items():

#                 if not isinstance(value, list):
#                     print(f"{key.upper()} : {value}")

#             print("----------------------")