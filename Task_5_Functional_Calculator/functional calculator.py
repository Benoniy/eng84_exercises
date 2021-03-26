import math  # Imported for use in area of a circle function


# This function is for adding num2 to num1
def add_function(num1, num2):
    return num1 + num2


# This function is for subtracting num2 from num1
def sub_function(num1, num2):
    return num1 - num2


# This function is for multiplying num1 by num2
def mult_function(num1, num2):
    return num1 * num2


# This function is for dividing num1 by num2
def div_function(num1, num2):
    return num1 / num2


# This function is for finding the area of a circle
# It uses the math package to import an accurate value for PI
def area_circle_function(radius):
    return mult_function(math.pi, radius) ** 2


# This function is for finding the area of a square
def area_square_function(height, width):
    return mult_function(height, width)


# This function is for finding the area of a right angle triangle
def area_right_angle_triangle_function(side_a, side_b):
    return div_function(mult_function(side_a, side_b), 2)


if __name__ == "__main__":
    # Add function
    print("\nCalling add_funtion() with 10 and 30, I expect 40 to be the result!")
    print(add_function(10, 30) == 40)
    print('got:', add_function(10, 30))

    # Subtract function
    print("\nCalling sub_function() with 50 and 20, I expect 30 to be the result!")
    print(sub_function(50, 20) == 30)
    print('got:', sub_function(50, 20))

    # Multiply function
    print("\nCalling mult_function() with 5 and 4, I expect 20 to be the result!")
    print(mult_function(5, 4) == 20)
    print('got:', mult_function(5, 4))

    # Divide function
    print("\nCalling div_function() with 10 and 2, I expect 5 to be the result!")
    print(div_function(10, 2) == 5)
    print('got:', div_function(10, 2))

    # Area of a circle function
    print("\nCalling area_circle_function() with a radius of 6, I expect 355 to be the result!")
    print(round(area_circle_function(6)) == 355)
    print('got:', round(area_circle_function(6)))

    # Area of a square function
    print("\nCalling area_square_function() with 15 and 17, I expect 255 to be the result!")
    print(area_square_function(15, 17) == 255)
    print('got:', area_square_function(15, 17))

    # Area of a right angle triangle function
    print("\nCalling area_right_angle_triangle_function() with 10 and 12, I expect 60 to be the result!")
    print(area_right_angle_triangle_function(10, 12) == 60)
    print('got:', area_right_angle_triangle_function(10, 12))

