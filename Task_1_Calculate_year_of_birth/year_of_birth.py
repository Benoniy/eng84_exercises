# Create a program that calculates the year of birth of a user
import datetime

# Get the current year
current_year = datetime.datetime.now().year

name = input("Please enter your name:\n")  # Get the users name

# This loop will continue until the user inputs a number
age = input("Please enter your age using digits:\n")
while not age.isdigit():
    age = input("error not a number, Please enter your age using digits:\n")

age = int(age)  # cast to in for math operations

# Subtract age from year to get the year of birth
year = current_year - age

# This loop will continue until the user inputs yes or no
# This is for correcting the year prediction if the user has had a birthday this year
b_day = input("Did you already have your birthday this year? (y or n):\n").lower()
while b_day != "y" and b_day != "n":
    b_day = input("Sorry I don't understand, did you already have your birthday this year? (y or n):\n").lower()

# Subtract a year if they haven't had their birthday this year
if b_day == "n":
    year -= 1


print(f"OMG {name}, you are {age} years old so you were born in {year}")

