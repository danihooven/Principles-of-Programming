""" --------------------------------------------------------------------------------------------------------------------
ITEC 136: Homework 01 - Question 01

Write a program that prompts user to enter three sides of a triangle.
The program should determine if the three sides can form a triangle.
To form a triangle, the sum of any 2 sides of a triangle must be greater than the length of the third side.

@author: Dani Hooven
@version: 09/08/2020

-------------------------------------------------------------------------------------------------------------------- """

# Functions
def isTriangle(a, b, c):
    """"
    Triangle Inequality Theorem
    this function will take 3 length parameters, and determine if three sides can form a triangle

    :param a: float
    :param b: float
    :param c: float
    :return: true or false

    """

    if (a < (b + c)) and (b < (c + a)) and (c < (a + b)):
        print("Triangle with lengths ", a, ", ", b, ", and ", c, "can form a triangle.")
    else:
        print("Triangle with lengths ", a, ", ", b, ", and ", c, "cannot form a triangle.")

# ---------------------------------------------------------------------------------------------------------------------

# Begin Program

# 1. Prompt user to enter three sides of triangle
side1 = float(input("Enter side 1 length: "))
side2 = float(input("Enter side 2 length: "))
side3 = float(input("Enter side 3 length: "))

# 2. Determine if the three sides can form a triangle
# --- See function isTri

# 3. Display the result to user.
isTriangle(side1, side2, side3)