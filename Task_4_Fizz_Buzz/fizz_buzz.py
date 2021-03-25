fizz = 3
buzz = 5


def is_fizz(num):
    return num % fizz == 0


def is_buzz(num):
    return num % buzz == 0


def run():
    for num in range(1, 101, 1):
        if is_fizz(num) and is_buzz(num):
            print("FizzBuzz")
        elif is_fizz(num):
            print("Fizz")
        elif is_buzz(num):
            print("Buzz")
        else:
            print(num)


fizz = input("please enter fizz: ")
while not fizz.isdigit():
    fizz = input("please enter fizz as a digit: ")
fizz = int(fizz)

buzz = input("please enter buzz: ")
while not buzz.isdigit():
    buzz = input("please enter buzz as a digit: ")
buzz = int(buzz)

run()
