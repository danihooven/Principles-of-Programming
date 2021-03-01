""" -------------------------------------------------------------------------------------------------------------------
ITEC 136: Homework 06_02

Please develop a program to help you crack the following secret message. - See mystery.txt
For the encryption we have used simple Caesar cipher.
You can find more information on https://en.wikipedia.org/wiki/Caesar_cipher.
Write a function to decrypt the message - mystery.txt
The function must have offset value, input file and output file parameters.
The offset value is the number n as described in the wiki.
No global variables are used in the function.
Function parameters must be used.


@author: Dani Hooven
@version: 10/13/2020

-------------------------------------------------------------------------------------------------------------------- """

# ----------------------------------------------------------------------------------------------------------------------
# IMPORT
# ----------------------------------------------------------------------------------------------------------------------


# ----------------------------------------------------------------------------------------------------------------------
# FUNCTIONS
# ----------------------------------------------------------------------------------------------------------------------

def encrypt(input, offset, output):
    """
    Function to encrypt or decrypt using input message file, shift key, and outputting new file
    """
    mystery = input.readline()
    while mystery:
        message = ""
        for char in mystery:
            if char.isupper():
                message += chr((ord(char) + offset - 65) % 26 + 65)
            elif char.islower():
                message += chr((ord(char) + offset - 97) % 26 + 97)
            else:
                message += char
        output.write(message)
        mystery = input.readline()
    input.close()
    output.close()


# ----------------------------------------------------------------------------------------------------------------------
# VARIABLES
# ----------------------------------------------------------------------------------------------------------------------

infile = open("mystery.txt", "r")
outfile = open("message.txt", "w")
key = -17


# ----------------------------------------------------------------------------------------------------------------------
# BEGIN PROGRAM"
# ----------------------------------------------------------------------------------------------------------------------

print(encrypt(infile, key, outfile))
