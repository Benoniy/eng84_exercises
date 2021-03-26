# Functional Calculator
### Tasks:
Part one:
1. Create an `add` function
2. Create an `subtract` function
3. Create an `multipy` function
4. Create an `divide` function

Part two:
5. Create an `area of a circle` function
6. Create an `area of a square` function
7. Create an `area of a triangle` function
```python
#example
def add_funtion(arg1, arg2):
    return arg1 + arg2
```

Extra:
8. Run each of the functions with arguments and print the results
9. Check you functions against known values - for example 10 + 30 will always be 40

```python
#example
print("Calling add_funtion() with 10 and 30, I expect 40 to be the result")
print(add_funtion(10, 30) == 40)
print('got:', add_funtion(10, 30))
```

Hint: do one function at a time and use my structure for the running the functions  

### Solutions:
1. I started by creating one function for each of the required simple functions.
    * Addition
    ```python
    # This function is for adding num2 to num1
    def add_function(num1, num2):
        return num1 + num2
    ```
    * Subtraction
    ```python
    # This function is for subtracting num2 from num1
    def sub_function(num1, num2):
        return num1 - num2
    ```
    * Multiplication
    ```python
    # This function is for multiplying num1 by num2
    def mult_function(num1, num2):
        return num1 * num2
    ```
    * Division
    ```python
    # This function is for dividing num1 by num2
    def div_function(num1, num2):
        return num1 / num2
    ```  
2. I then created the more complex functions all of which used my simple functions to perform arithmetic operations.  
    * Area of a circle
    ```python
    import math  # Imported for use in area of a circle function
   
    # This function is for finding the area of a circle
    # It uses the math package to import an accurate value for PI
    def area_circle_function(radius):
        return mult_function(math.pi, radius) ** 2
    ```
   * Area of a square
    ```python
    # This function is for finding the area of a square
    def area_square_function(height, width):
        return mult_function(height, width)
    ```
   * Area of a right angle triangle
    ```python
    # This function is for finding the area of a right angle triangle
    def area_right_angle_triangle_function(side_a, side_b):
        return div_function(mult_function(side_a, side_b), 2)
    ```  
3. Lastly I printed the results of each function against known results using the suggested structure.
    * Addition
    ```python
    # Add function
    print("\nCalling add_funtion() with 10 and 30, I expect 40 to be the result!")
    print(add_function(10, 30) == 40)
    print('got:', add_function(10, 30))
    ```
    * Subtraction
    ```python
    # Subtract function
    print("\nCalling sub_function() with 50 and 20, I expect 30 to be the result!")
    print(sub_function(50, 20) == 30)
    print('got:', sub_function(50, 20))
    ```
    * Multiplication
    ```python
    # Multiply function
    print("\nCalling mult_function() with 5 and 4, I expect 20 to be the result!")
    print(mult_function(5, 4) == 20)
    print('got:', mult_function(5, 4))
    ```
    * Division
    ```python
    # Divide function
    print("\nCalling div_function() with 10 and 2, I expect 5 to be the result!")
    print(div_function(10, 2) == 5)
    print('got:', div_function(10, 2))
    ```  
    * Area of a circle
    ```python
    # Area of a circle function
    print("\nCalling area_circle_function() with a radius of 6, I expect 355 to be the result!")
    print(round(area_circle_function(6)) == 355)
    print('got:', round(area_circle_function(6)))
    ```
   * Area of a square
    ```python
    # Area of a square function
    print("\nCalling area_square_function() with 15 and 17, I expect 255 to be the result!")
    print(area_square_function(15, 17) == 255)
    print('got:', area_square_function(15, 17))
    ```
   * Area of a right angle triangle
    ```python
    # Area of a right angle triangle function
    print("\nCalling area_right_angle_triangle_function() with 10 and 12, I expect 60 to be the result!")
    print(area_right_angle_triangle_function(10, 12) == 60)
    print('got:', area_right_angle_triangle_function(10, 12))
    ```  
4. I am happy to say that all of my test cases where successful.
