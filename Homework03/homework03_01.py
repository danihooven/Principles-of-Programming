""" -------------------------------------------------------------------------------------------------------------------
ITEC 136: Homework 03_01

Write a function that takes one parameter, a text string.
It counts the number of alphabetic characters (a through z, or A through Z)
in the text string and then keeps track of the count and percentage of the lowercase letter 'a'.
Do not use global parameters.  No global variables are used in the function.  Function parameters must be used.
The output must show percentage in one decimal place.  Use string format to show one decimal place output.

@author: Dani Hooven
@version: 09/22/2020

-------------------------------------------------------------------------------------------------------------------- """


# ----------------------------------------------------------------------------------------------------------------------
# FUNCTIONS
# ----------------------------------------------------------------------------------------------------------------------

def count_char(t):
    """
    Count Total Characters
    This function will take a string and return the total number of characters
    :param t: string
    """
    return len(t)


def count_a(s):
    """
    Count Total Number of "a" in Text
    This function will take a string and return the total number of "a" characters
    :param s: string
    """
    total_a = 0
    for i in range(len(s)):
        if s[i] == "a":
            total_a = total_a + 1
    return total_a


# ----------------------------------------------------------------------------------------------------------------------
# SET VARIABLES
# ----------------------------------------------------------------------------------------------------------------------

text = input("Enter text: ")

# ----------------------------------------------------------------------------------------------------------------------
# BEGIN PROGRAM"
# ----------------------------------------------------------------------------------------------------------------------

percentage = count_a(text) / count_char(text) * 100
print("Your text contains", count_char(text), "alphabetic characters, of which", percentage, "% are 'a'")
