# Loops and Lists

### Tasks:
1. Make a for loop using range() that prints hello 10 times
2. Create another for loop using range that asks the user for names and appends it to a list called list_names
3. Make a loop that iterates over each name in list_names and format's so that each name is lowercase, then add these names to a new list called list_names_lower
4. Iterate over a list of values and display if they are odd or even

### Solutions:
1. First I defined some lists as I knew I would have to use some of them for multiple tasks
```python
list_names = []  # Used in name_loop and names_lower_loop
list_names_lower = []  # Used in names_lower_loop
list_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # Used in list_values_is_even
```
2. I completed task one by creating a function called hello_loop
```python
# For loop using range that prints hello 10 times
def hello_loop():
    for _ in range(0, 10, 1):  # Loops 10 times
        print("Hello")
```  
3. I completed task two by creating a function called name_loop which added items to list_names
```python
# For loop that asks the user to input 10 names to add to a list
def name_loop():
    print("Could you please provide me with a set of 10 names?")

    for num in range(1, 11, 1):  # Loop 10 times and add user input to list_names
        list_names.append(input(f"Please enter name {num}: "))

    print(f"list_names = {list_names}")  # Print list_names when function ends
```  
4. Using list_names, I created a loop that populated list_names_lower by converting them to lower case and appending
```python
# For each loop that converts all the names provided by list_names,
# converts them to lower case and adds them to list_names_lower
def names_lower_loop():
    for name in list_names:  # loop through list_names
        list_names_lower.append(name.lower())  # lower name and add it to list_names_lower

    print(f"list_names_lower = {list_names_lower}")
```
5. Finally I created a function called list_values_is_even, which would loop through a list and display if the value is odd or even
```python
# A simple for each loop that uses modulus to determine if values
# in a list are even or odd
def list_values_is_even():
    for value in list_values:
        if value % 2 == 0:
            print(f"{value} is even!")
            continue

        print(f"{value} is odd!")
```
6. To run this code: 
```python
if __name__ == "__main__":
    hello_loop()
    name_loop()
    names_lower_loop()
    list_values_is_even()
```