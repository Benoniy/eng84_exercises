# Calculate the year of birth of a user  
### Tasks:
Part one:
* Define the variables `age` and `name`
* Using `age` calculate the year in which the user was born
* Print out "OMG [person], you are [age] years old, so you were born in [year]" with the correct values

Part two:
* Prompt the user to input values for the variables `age` and `name`
* Check the user's input to make sure it is correct (age must be a number)
* Figure out a way to account for if the user's birthday has already happened this year or not

Extra:
* Go look into the library time
* Print out how long this person has lived in hours

### Solutions:
1. To calculate the user's date of birth I first declared the variables `age` and `name`
```python
name = input("Please enter your name:\n")  # Get the users name

# This loop will continue until the user inputs a number
age = input("Please enter your age using digits:\n")
while not age.isdigit():
    age = input("error not a number, Please enter your age using digits:\n")

age = int(age)  # cast to in for math operations
```
2. I then subtracted the users age from the current year which I got from the `datetime` module  
```python
# Get the current year
current_year = datetime.datetime.now().year
# Subtract age from year to get the year of birth
year = current_year - age
```
3. To correct my date of birth prediction, I then created an input to ask the user if they had their birthday already this year.
```python
# This loop will continue until the user inputs yes or no
# This is for correcting the year prediction if the user has had a birthday this year
b_day = input("Did you already have your birthday this year? (y or n):\n").lower()
while b_day != "y" and b_day != "n":
    b_day = input("Sorry I don't understand, did you already have your birthday this year? (y or n):\n").lower()

# Subtract a year if they haven't had their birthday this year
if b_day == "n":
    year -= 1
```  
4. Finally I displayed a message to the user
```python
print(f"OMG {name}, you are {age} years old so you were born in {year}")
```
