""" -------------------------------------------------------------------------------------------------------------------
ITEC 136: Homework 02 - Question 02

Write a program that determines if the number entered is a prime number.
The program should have a function called is_prime(num) that takes a single integer argument
and returns True when the argument is a prime number, and False otherwise.

Hint: Prime number is a positive number whose only factors are 1 and itself.

@author: Dani Hooven
@version: 09/15/2020

-------------------------------------------------------------------------------------------------------------------- """


# ----------------------------------------------------------------------------------------------------------------------
# FUNCTIONS
# ----------------------------------------------------------------------------------------------------------------------

def is_prime(num):
    """"
    Prime Number Checker:
    This function determines if a number is positive and is prime - only factors are 1 and itself
    :param num: int
    :return: true or false
    """
    if num <= 1:  # check if the number is positive
        return False

    for i in range(2, num):
        if num % i == 0:  # divide the input by each number in the range 2 to the number - 1
            return False  # if there is no remainder, the number is not prime
        else:
            return True


# ----------------------------------------------------------------------------------------------------------------------
# VARIABLES
# ----------------------------------------------------------------------------------------------------------------------

int_num = int(input("Enter an integer: "))  # prompt user to enter a number.


# ----------------------------------------------------------------------------------------------------------------------
# PROGRAM
# ----------------------------------------------------------------------------------------------------------------------

if is_prime(int_num):  # determine if number is prime
    print(int_num, "is a prime number.")
else:
    print(int_num, "is not a prime number.")
