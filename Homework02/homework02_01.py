""" -------------------------------------------------------------------------------------------------------------------

TEC 136: Homework 02 - Question 01

Write a program that prompts user to enter three sides of a triangle.  The program should determine if the three sides
can form a triangle.  If the three sides can form a triangle, then determine the type of the triangle.

There are three types of triangles:
o	Equilateral triangle (all 3 sides are equal)
o	Isosceles triangle (two sides are equal, the third side is of a different length)
o	Scalene triangle (all 3 sides are of different lengths)

The program should have a function called triangle_type() that takes 3 parameters, the lengths of each side.
The triangle_type() function should return Equilateral, Isosceles, or Scalene according to the descriptions above.
Do not use global variables. Function parameters must be used.

@author: Dani Hooven
@version: 09/15/2020

-------------------------------------------------------------------------------------------------------------------- """


# ----------------------------------------------------------------------------------------------------------------------
# FUNCTIONS
# ----------------------------------------------------------------------------------------------------------------------

def is_triangle(a, b, c):
    """"
    Triangle Inequality Theorem
    this function will take 3 length parameters, and determine if three sides can form a triangle
    :param a: float
    :param b: float
    :param c: float
    :return: true or false
    """
    if (a < (b + c)) and (b < (c + a)) and (c < (a + b)):  # the sum of two sides is greater than the third
        return True
    else:
        return False


def triangle_type(a, b, c):
    """"
    Triangle Type
    this function will take 3 length parameters and return triangle type
    - Equilateral - all three sides are equal
    - Isosceles - two sides are equal, the third is a different length
    - Scalene - all three sides are different lengths
    :param a: float
    :param b: float
    :param c: float
    :return: Equilateral, Isosceles, or Scalene
    """
    if a == b and b == c and c == a:  # equilateral
        print("Triangle with lengths", a, ",", b, " and ", c, " is an Equilateral triangle")
    elif a == b or b == c or a == c:  # isosceles
        print("Triangle with lengths", a, ",", b, " and ", c, " is an Isosceles triangle")
    else:  # scalene
        print("Triangle with lengths", a, ",", b, " and ", c, " is a Scalene triangle")


# ----------------------------------------------------------------------------------------------------------------------
# VARIABLES
# ---------------------------------------------------------------------------------------------------------------------

# prompt user to enter three sides of a triangle.
side1 = float(input("Enter side 1 length: "))
side2 = float(input("Enter side 2 length: "))
side3 = float(input("Enter side 3 length: "))


# ----------------------------------------------------------------------------------------------------------------------
# PROGRAM
# ----------------------------------------------------------------------------------------------------------------------

if is_triangle(side1, side2, side3):  # test if three sides can form a triangle
    triangle_type(side1, side2, side3)  # determine the type of triangle & print result
else:
    print("Triangle with lengths ", side1, ", ", side2, " and ", side3, "cannot form a triangle.")
