fizz = 3  # holds value for fizz
buzz = 5  # holds value for buzz


# Returns true if a number is fizz
def is_fizz(num):
    return num % fizz == 0


# Returns true if a number is buzz
def is_buzz(num):
    return num % buzz == 0


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


if __name__ == "__main__":

    # Change fizz and buzz if the user wants to
    user_input = input("Would you like to change the default values of fizz and buzz?: ")
    while not user_input.lower() in ("y", "n"):
        user_input = input("please enter your answer as either y or n: ")

    if user_input == "y":
        change_fizz_buzz()

    # Run fizz buzz
    run_fizzbuzz()
