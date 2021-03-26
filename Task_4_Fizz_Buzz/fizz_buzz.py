

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
