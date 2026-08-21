def get_integer(message):
    while True:
        try:
            return int(input(message))

        except ValueError:
            print("Please enter a valid number.")