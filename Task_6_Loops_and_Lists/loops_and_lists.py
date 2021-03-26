list_names = []
list_names_lower = []
list_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# For loop using range that prints hello 10 times
def hello_loop():
    for _ in range(0, 10, 1):
        print("Hello")


def name_loop():
    print("Could you please provide me with a set of 10 names?")

    for num in range(1, 11, 1):
        list_names.append(input(f"Please enter name {num}: "))

    print(f"list_names = {list_names}")


def names_lower_loop():
    for name in list_names:
        list_names_lower.append(name.lower())

    print(f"list_names_lower = {list_names_lower}")


def list_values_is_even():
    for value in list_values:
        if value % 2 == 0:
            print(f"{value} is even!")
            continue

        print(f"{value} is odd!")


if __name__ == "__main__":
    hello_loop()
    name_loop()
    names_lower_loop()
    list_values_is_even()
