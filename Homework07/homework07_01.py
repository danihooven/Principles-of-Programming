""" -------------------------------------------------------------------------------------------------------------------
ITEC 136: Homework 07_01

Develop a program that asks the user to enter a text.

The program should analyze the text and print out unique letters,
in alphabetical order,
with the percentage information of each letter.
Case should be ignored.

Write a function to analyze the text string.
No global variables are used in the function.
Function parameters must be used.


@author: Dani Hooven
@version: 10/20/2020

-------------------------------------------------------------------------------------------------------------------- """


# ----------------------------------------------------------------------------------------------------------------------
# IMPORT
# ----------------------------------------------------------------------------------------------------------------------


# ----------------------------------------------------------------------------------------------------------------------
# FUNCTIONS
# ----------------------------------------------------------------------------------------------------------------------

def letter_percent(s):
    """
    Function that takes a string, converts to lower case,
    counts each letter, and return the percentage of each letter in the string
    :param s: string
    :return: percentage of letter occurrence in string
    """

    alpha = 'abcdefghijklmnopqrstuvwxyz'
    s_lower = s.lower()
    s_length = 0
    letter_count = {}  # empty dictionary
    keys = letter_count.keys()

    for char in s_lower:
        if char in alpha:
            s_length = s_length + 1
            if char in letter_count:
                letter_count[char] = letter_count[char] + 1
            else:
                letter_count[char] = 1

    for char in sorted(keys):
        letter_count[char] = (letter_count[char] / s_length) * 100
        print(char, "{:.1f}%".format(letter_count[char]))


# ----------------------------------------------------------------------------------------------------------------------
# VARIABLES
# ----------------------------------------------------------------------------------------------------------------------

text = input("Enter text: ")

# ----------------------------------------------------------------------------------------------------------------------
# BEGIN PROGRAM"
# ----------------------------------------------------------------------------------------------------------------------

print(letter_percent(text))
