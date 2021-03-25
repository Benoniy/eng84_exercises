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