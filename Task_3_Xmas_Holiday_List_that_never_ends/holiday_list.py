

def generate_list():
    xmas_list = []
    print("\nHO HO HO! What do you want for Christmas?")

    user_input = ""
    while True:
        user_input = input()

        if user_input.lower().count("exit") > 0:
            break

        xmas_list.append(user_input)
        print("What else would you like?")

    return xmas_list


def print_list(item_list):
    print("\nMy Christmas List:")
    count = 1
    for item in item_list:
        print(f"{count}. {item.upper()}")
        count += 1


if __name__ == "__main__":
    xmas_list = generate_list()
    print_list(xmas_list)
