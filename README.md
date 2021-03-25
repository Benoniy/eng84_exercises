# Python Exercises

## 01 - Program that calculates year of birth!
Cool, we've used strings to make a program that made a welcome message. Now let's use some numerical types.  
Create a program that calculates the year of birth.

### Part one:
* Define the variables `age` and `name`
* Using `age` calculate the year in which the user was born
* Print out "OMG [person], you are [age] years old, so you were born in [year]" with the correct values

### Part two:
* Prompt the user to input values for the variables `age` and `name`
* Check the user's input to make sure it is correct (age must be a number)
* Figure out a way to account for if the user's birthday has already happened this year or not

### Extra:
* Go look into the library time
* Print out how long this person has lived in hours

### Acceptance Criteria: 
* Program defines the variable `age` and `name`
* Program prints the string "OMG <person>, you are <age> years old, so you were born in <year>"

------------------------------------------------
## 02 - A Restaurant Waiter Helper program

### Summary
Now that we've created had some time to use our lists, time to make something more useful.  
You are going to make a program that helps a waiter with his menu and his orders.

### Tasks:
Using the following **User stories**, create a program that fulfills all the requirements:  
* As a User I want to be able to see the menu in a formatted way, so that I can order my meal.
* As a User I want to be able to order 3 times, and have my responses added to a list, so they aren't forgotten.
* As a user, I want to have my order read back to me in formatted way, so I know what I ordered.

### Acceptance Criteria:
* Must be on both your PC and Git-Hub
* Have 5 commits minimum!
* Have proper documentation (readme)
* follows best practices

------------------------------------------------
## 03 - Xmas Holiday List that never ends!
Amazing, you've learned about for loops!
Time to use that, plus a while loop to keep things going!

### Tasks:
Your task is to create a list of xmas gifts using control flow!
Fulfill the user stories to complete the task.

Hint: While loops and break conditions, use lists and append, iterate to print.

User stories:
* As a user, I want to be able to add items to the list, so I can read it later.
* As a user, I want to be able to keep adding things to the list until I use exit.
* As a user, I should be able to use the word exit in a sentence and still have the program terminate, so that anyone can use it.
* As a user, when the program exits, I want to see the complete list in caps lock and numbered, so that I know what to buy. example:
  1. RC CAR
  2. PS2
  3. GTA VICE CITY

### Acceptance Criteria:

* All user stories are completed
* Has documentation

------------------------------------------------
## 04 - Fizz Buzz!
Super simple game that will substitute multiples of 3 and 5 for fizz and buzz respectively, or fizzbuzz for multiples of both.

### Tasks:
* Write a program that prints the numbers from 1 to 100.
* For multiples of three print "Fizz" instead of the number.
* For the multiples of five print "Buzz" instead of the number.
* For numbers which are multiples of both three and five print "FizzBuzz".

### Extra:
* Make a second fizzbuzz file and make it use functions
* In the second file make so that we can decide which numbers to substitute for fizz and buzz using functions

Hint: loop, range, control flow

### Acceptance Criteria:
* All tasks are complete
* Code compiles without error

------------------------------------------------
## 05 - Functional Calculator
Amazing you now know functions, lets make a functional calculator.

### Part one:
* Create an `add` function
* Create an `subtract` function
* Create an `multipy` function
* Create an `divide` function

### Part two:
* Create an `area of a circle` function
* Create an `area of a square` function
* Create an `area of a triangle` function
```python
#example
def add_funtion(arg1, arg2):
    return arg1 + arg2
```

### Extra:
* Run each of the functions with arguments and print the results
* Check you functions against known values - for example 10 + 30 will always be 40

```python
#example
print("Calling add_funtion() with 10 and 30, I expect 40 to be the result")
print(add_funtion(10, 30) == 40)
print('got:', add_funtion(10, 30))
```

Hint: do one function at a time and use my structure for the running the functions

### Acceptance Criteria:
* All core functions done
* Separation of concerns if followed
* DRY code and functions  

------------------------------------------------
## 06 - Loops and lists
Let's loop over some lists!

### Tasks:

* Make a for loop using range() that prints hello 10 times
* Create another for loop using range that asks the user for names and appends it to a list called list_names
* Make a loop that iterates over each name in list_names and format's so that each name is lowercase, then add these names to a new list called list_names_lower
* Iterate over the list of values to find if the are even ### No clue what this is asking for

### Acceptance Criteria
* All tasks are completed

------------------------------------------------
