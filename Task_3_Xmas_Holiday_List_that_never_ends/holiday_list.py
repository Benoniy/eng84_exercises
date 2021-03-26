

# Generates a list by accepting user input until "exit" is used
# Returns the generated list
def generate_list():
    return_list = []  # This is the list it will return
    print("\nHO HO HO! What do you want for Christmas?")

    # This will loop until the word exit forces a break
    while True:
        user_input = input()  # get input

        if user_input.lower().count("exit") > 0:  # break if there is 1 or more instances of the word "exit" in the input
            break

        return_list.append(user_input)  # Add the item to the list
        print("What else would you like?")

    return return_list


# This prints the list in a nice format for the user to read
def print_list(item_list):
    print("\nMy Christmas List:")
    count = 1
    for item in item_list:  # For each item in the list print it in a nice format with a unique number
        print(f"{count}. {item.upper()}")
        count += 1


# First generate the list, then print it back to the user
if __name__ == "__main__":
    xmas_list = generate_list()
    print_list(xmas_list)
