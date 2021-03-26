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
1. Completing all of the requirements for part one was simple, I created it in [fizz_buzz.py]().
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
2. I went on to complete the extra tasks too, I completed them in [fizz_buzz_functions]().