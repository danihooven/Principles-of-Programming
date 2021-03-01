""" -------------------------------------------------------------------------------------------------------------------
ITEC 136: Homework 03_02

Write a function that implements a substitution cipher.
In the substitution cipher one letter is substituted for another to garble the message.
For example A -> Q, B -> T, C -> G etc.
Your function should take two parameters,
the message you want to encrypt,
and a string that represents the mapping of the 26 letters in the alphabet.
Your function should return a string that is the encrypted version of the message.
Don’t encrypt non-alphabet characters.

@author: Dani Hooven
@version: 09/22/2020

-------------------------------------------------------------------------------------------------------------------- """

# ----------------------------------------------------------------------------------------------------------------------
# IMPORT
# ----------------------------------------------------------------------------------------------------------------------

import string


# ----------------------------------------------------------------------------------------------------------------------
# FUNCTIONS
# ----------------------------------------------------------------------------------------------------------------------

def encrypt(txt, mapping):
    """
    Encryption Function
    Takes two parameters (message for encryption and mapping string)
    returns an encrypted version of the message
    :param txt: string
    :param mapping: string
    """

    message_out = ""  # holds encoded message for output
    alpha = "abcdefghijklmnopqrstuvwxyz"  # alphabet for mapping

    for position in range(len(txt)):  # for each character in the message
        if txt[position].isdigit() or txt[position] in string.punctuation:  # check if digit or punctuation
            message_out = message_out + txt[position]  # add digit or punctuation to output message
        elif not txt[position].isspace():  # check if character is not blank
            for idx in range(len(alpha)):  # for each letter in the alphabet
                if txt[position].isupper():  # check if character is uppercase
                    if txt[position] == alpha[idx].upper():  # check if character matches current letter in alpha
                        message_out = message_out + mapping[idx].upper()  # add the mapped character to output message
                elif txt[position].islower():  # check if character is lowercase
                    if txt[position] == alpha[idx]:  # check if character matches current letter in alpha
                        message_out = message_out + mapping[idx]  # add the mapped character to output message
        else:
            message_out = message_out + " "  # add a blank space to output message
    print(message_out)  # print out total message


# ----------------------------------------------------------------------------------------------------------------------
# SET VARIABLES
# ----------------------------------------------------------------------------------------------------------------------

message_in = input("Enter your message: ")  # user input message to be encoded
key = "qwertyuiopasdfghjklzxcvbnm"  # mapping string 26 characters

# ----------------------------------------------------------------------------------------------------------------------
# BEGIN PROGRAM"
# ----------------------------------------------------------------------------------------------------------------------

encrypt(message_in, key)
