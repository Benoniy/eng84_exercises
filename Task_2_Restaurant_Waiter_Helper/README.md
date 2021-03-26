# Restaurant waiter helper
### Tasks:
1. To fulfill user requirement 1 I created a function that when called, prints a nicely formatted menu.
```python
# A dictionary that contains all the items a customer can order
menu = {1: {"name": "Burger", "price": 3.0},
        2: {"name": "Fries", "price": 1.2},
        3: {"name": "Chicken wings", "price": 4.0}
        }


# This function prints the menu by extracting values from a dictionary
def print_menu():
    print("Menu:")
    for item_no, content in menu.items():
        print(f"{item_no}: {content['name']} £{content['price']}")
```  
2. To fulfill user requirement 2 I created a list and a while loop that could accept user input
```python
# A list that stores the customers ordered items
order = []

# This controls user input
print("\n")
usr_input = ""
while usr_input != "exit":
    usr_input = input("Commands: exit | clear \nPlease enter the number of the item you wish to add:\n")

    if usr_input.isdigit():  # If its a digit treat it as an order
        order.append(int(usr_input))
    else:  # else treat it as a command
        usr_input = usr_input.lower()
        if usr_input == "clear":
            order.clear()

    print_order()
```
3. Finally to satisfy requirement 3 I created a function that prints the order list in a nice format
```python
# This function prints orders by pulling the item numbers from the list
# and using them to reference values in the menu dictionary
def print_order():
    total = 0
    print("\nCurrent Order:")
    for item in order:
        print(f"{menu[item]['name']} £{menu[item]['price']}")
        total += menu[item]['price']
    print(f"Total = £{total}\n")
```