# Fizz Buzz

### Tasks: 
Part One:
1. Write a program that prints the numbers from 1 to 100.
2. For multiples of three print "Fizz" instead of the number.
3. For the multiples of five print "Buzz" instead of the number.
4. For numbers which are multiples of both three and five print "FizzBuzz".

Extra:
5. Make a second fizzbuzz file and make it use functions
6. In the second file make so that we can decide which numbers to substitute for fizz and buzz using functions

Hint: loop, range, control flow

### Solutions:
1. Completing all of the requirements for part one was simple, I created it in [fizz_buzz.py](https://github.com/Benoniy/eng84_exercises/blob/main/Task_4_Fizz_Buzz/fizz_buzz.py).
    * I completed task one by using a for loop to run through 100 numbers.  
    `for num in range(1, 101, 1):`
    * I completed task two, three and four by using an if statement and modulus to find if numbers where divisible by fizz, buzz or both.  
    `if num % 3 == 0 and num % 5 == 0:` - FizzBuzz  
    `elif num % 3 == 0:` - Fizz  
    `elif num % 5 == 0:` - Buzz
```python
# A basic fizz buzz program
for num in range(1, 101, 1):  # Loop through 100 numbers
    if num % 3 == 0 and num % 5 == 0:  # If number is fizz and buzz
        print("FizzBuzz")
    elif num % 3 == 0:  # Or if number is only fizz
        print("Fizz")
    elif num % 5 == 0:  # Or if number is only buzz
        print("Buzz")
    else:  # Or if number is none of the above
        print(num)
```  
2. I went on to complete the extra tasks too, I completed them in [fizz_buzz_functions.py](https://github.com/Benoniy/eng84_exercises/blob/main/Task_4_Fizz_Buzz/fizz_buzz_functions.py).
    * I first created variables to hold the values of fizz and buzz.
    ```python
    fizz = 3  # holds value for fizz
    buzz = 5  # holds value for buzz
    ```
    * I split fizz and buzz into separate functions that I could access later.
    ```python
    # Returns true if a number is fizz
    def is_fizz(num):
        return num % fizz == 0
    
    
    # Returns true if a number is buzz
    def is_buzz(num):
        return num % buzz == 0
    ``` 
   * Then I created a function called run_fizzbuzz() that would make use of these functions within a loop to achieve fizz buzz.
    ```python
    # Generates 1 to 100 and enacts methods to change numbers to fizz, buzz and fizzbuzz accordingly
    def run_fizzbuzz():
        for num in range(1, 101, 1):
            if is_fizz(num) and is_buzz(num):  # If number is fizz and buzz
                print("FizzBuzz")
            elif is_fizz(num):  # Or if number is only fizz
                print("Fizz")
            elif is_buzz(num):  # Or if number is only buzz
                print("Buzz")
            else:  # Or if number is none of the above
                print(num)

    ```
   * Last of all I added in a function that would allow the user to change the values of fizz and buzz if they wanted to
    ```python
    # Changes the values of fizz and buzz if the user wants it
    def change_fizz_buzz():
        # This allows the user to change the value of fizz
        fizz = input("please enter fizz: ")
        while not fizz.isdigit():
            fizz = input("please enter fizz as a digit: ")
        fizz = int(fizz)
    
        # This allows the user change the value of buzz
        buzz = input("please enter buzz: ")
        while not buzz.isdigit():
            buzz = input("please enter buzz as a digit: ")
        buzz = int(buzz)
    ```
   * To run this file:
    ```python
    if __name__ == "__main__":
    
        # Change fizz and buzz if the user wants to
        user_input = input("Would you like to change the default values of fizz and buzz?: ")
        while not user_input.lower() in ("y", "n"):
            user_input = input("please enter your answer as either y or n: ")
    
        if user_input == "y":
            change_fizz_buzz()
    
        # Run fizz buzz
        run_fizzbuzz()
    ```