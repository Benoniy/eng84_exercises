# Xmas List that never ends
### User Stories:
1. As a user, I want to be able to add items to the list, so I can read it later.
2. As a user, I want to be able to keep adding things to the list until I use exit.
3. As a user, I should be able to use the word exit in a sentence and still have the program terminate, so that anyone can use it.
4. As a user, when the program exits, I want to see the complete list in caps lock and numbered, so that I know what to buy. example:
   1. RC CAR
   2. PS2
   3. GTA VICE CITY

### Tasks:
1. To complete the first 3 user requirements, I created a function called generate_list()  
    * The first user requirement was completed by creating a list `return_list` that had items added to it within the while loop.
    * The second user requirement was completed by adding the line `if user_input.lower().count("exit") > 0: break`
    * The same line that solved the second user requirement also solved the third, by using lower and count the exit command can be used  
    anywhere in the input string and it will still work
```python
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
```
2. To fulfill the fourth user requirement I created a function called print list which prints it in a nicely formatted way.
```python
# This prints the list in a nice format for the user to read
def print_list(item_list):
    print("\nMy Christmas List:")
    count = 1
    for item in item_list:  # For each item in the list print it in a nice format with a unique number
        print(f"{count}. {item.upper()}")
        count += 1
```
3. To call these functions:
```python
# First generate the list, then print it back to the user
if __name__ == "__main__":
    xmas_list = generate_list()
    print_list(xmas_list)
```