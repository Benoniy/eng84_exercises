# Create a program that helps a waiter with his menu and his orders.
menu = {1: {"name": "Burger", "price": 3.0},
        2: {"name": "Fries", "price": 1.2},
        3: {"name": "Chicken wings", "price": 4.0}
        }

order = []


def print_menu():
    print("Menu:")
    for item_no, content in menu.items():
        print(f"{item_no}: {content['name']} £{content['price']}")



print_menu()
print("\n")
usr_input = ""
while usr_input != "exit":
    usr_input = input("Please enter the number of the item you wish to add:\n")
