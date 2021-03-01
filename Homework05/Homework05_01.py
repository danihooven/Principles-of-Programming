""" -------------------------------------------------------------------------------------------------------------------
ITEC 136: Homework 05_01

Develop a recursive function called is_palindrome
that takes a string as a parameter and returns True if the string is a palindrome, False otherwise.
Remember that a string is a palindrome if it is spelled the same both forward and backward.
No global variables are used in the function.  Function parameters must be used.

@author: Dani Hooven
@version: 10/06/2020

-------------------------------------------------------------------------------------------------------------------- """

# ----------------------------------------------------------------------------------------------------------------------
# IMPORT
# ----------------------------------------------------------------------------------------------------------------------

import string


# ----------------------------------------------------------------------------------------------------------------------
# FUNCTIONS
# ----------------------------------------------------------------------------------------------------------------------

def only_alpha(s):
    """
    Function that will produce a new string without spaces or punctuation
    :param s: string
    :return: modified lower case string without spaces or punctuation
    """
    mod = ""    # variable to hold modified string
    for char in s:  # for each character in the string
        if char != " " and char not in string.punctuation:  # if the character is not a punctuation and not a space
            mod = mod + char    # add the character to the modified string
    return mod.lower()  # return a lower case version of the modified string


def is_palindrome(s):
    """
    Function that check if a string is a palindrome
    :param s: string
    :return: True if string is palindrome, false if not
    """
    if len(s) <= 2:  # length of 0 or 1 is a palindrome
        return True
    if s[0] != s[-1]:  # not pal if the first and last letters do not match
        return False
    return is_palindrome(s[1:-1])  # run check again after removing first and last letter


# ----------------------------------------------------------------------------------------------------------------------
# VARIABLES
# ----------------------------------------------------------------------------------------------------------------------


# ----------------------------------------------------------------------------------------------------------------------
# BEGIN PROGRAM
# ----------------------------------------------------------------------------------------------------------------------

print(is_palindrome(only_alpha("kayak")))
print(is_palindrome(only_alpha("Live not on evil")))
print(is_palindrome(only_alpha("Reviled did I live, said I, as evil I did deliver")))
print(is_palindrome(only_alpha("Go hang a salami; I'm a lasagna hog.")))
print(is_palindrome(only_alpha("Kanakanak")))
print(is_palindrome(only_alpha("Wassamassaw")))
print(is_palindrome(only_alpha("Hello")))
