list_names = []  # Used in name_loop and names_lower_loop
list_names_lower = []  # Used in names_lower_loop
list_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # Used in list_values_is_even


# For loop using range that prints hello 10 times
def hello_loop():
    for _ in range(0, 10, 1):
        print("Hello")


# For loop that asks the user to input 10 names to add to a list
def name_loop():
    print("Could you please provide me with a set of 10 names?")

    for num in range(1, 11, 1):  # Loop 10 times and add user input to list_names
        list_names.append(input(f"Please enter name {num}: "))

    print(f"list_names = {list_names}")  # Print list_names when function ends


# For each loop that converts all the names provided by list_names,
# converts them to lower case and adds them to list_names_lower
def names_lower_loop():
    for name in list_names:  # loop through list_names
        list_names_lower.append(name.lower())  # lower name and add it to list_names_lower

    print(f"list_names_lower = {list_names_lower}")


# A simple for each loop that uses modulus to determine if values
# in a list are even or odd
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
