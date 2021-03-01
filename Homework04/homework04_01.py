""" -------------------------------------------------------------------------------------------------------------------
ITEC 136: Homework 04_01

Develop a program to replace parts of the string.

Write a function replace(s, old, new) that replaces all occurrences of old with new in the string s.
It returns the modified string.
Don’t use the built-in replace function.
No global variables are used in the function.
Function parameters must be used.



@author: Dani Hooven
@version: 09/29/2020

-------------------------------------------------------------------------------------------------------------------- """


# ----------------------------------------------------------------------------------------------------------------------
# IMPORT
# ----------------------------------------------------------------------------------------------------------------------


# ----------------------------------------------------------------------------------------------------------------------
# FUNCTIONS
# ----------------------------------------------------------------------------------------------------------------------

def replace(s, old, new):
    """
    Replace Function
    replaces old with new and returns modified string
    :param s: string
    :param old: string
    :param new: string
    :return: modified string
    """
    split_string = s.split(old)  # splits message using old as delimiter
    mod_string = new.join(split_string)  # joins list using new
    return mod_string  # returns modified string


# ----------------------------------------------------------------------------------------------------------------------
# SET VARIABLES
# ----------------------------------------------------------------------------------------------------------------------

message = input("Enter text: ")
delimiter = input("Find: ")
glue = input("Replace: ")
# ----------------------------------------------------------------------------------------------------------------------
# BEGIN PROGRAM"
# ----------------------------------------------------------------------------------------------------------------------

print(replace(message, delimiter, glue))  # replace parts of a string
