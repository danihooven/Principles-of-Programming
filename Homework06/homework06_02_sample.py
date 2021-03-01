""" -------------------------------------------------------------------------------------------------------------------
ITEC 136: Homework 06_02_sample

Please develop a program to help you crack the following secret message. - See mysterysample.txt
For the encryption we have used simple Caesar cipher.
You can find more information on https://en.wikipedia.org/wiki/Caesar_cipher.
Write a function to decrypt the message - mysterysample.txt
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
# VARIABLES
# ----------------------------------------------------------------------------------------------------------------------

infile = open("../../../AppData/Roaming/JetBrains/PyCharmCE2020.2/scratches/mysterysample.txt", "r")  # read students' grades
outfile = open("messagesample.txt", "w")  # write their names and average into a new file
key = -17


# ----------------------------------------------------------------------------------------------------------------------
# FUNCTIONS
# ----------------------------------------------------------------------------------------------------------------------

def encrypt(input, offset, output):
    message = ""
    mystery = input.readline()
    for i in range(len(mystery)):
        char = mystery[i]
        if char.isupper():
            message += chr((ord(char) + offset - 65) % 26 + 65) # 65 = A %26 can be 0 = 25 (26 letter in the alpha)
        elif char.islower():
            message += chr((ord(char) + offset - 97) % 26 + 97)
        else:
            message += char
    return output.write(message + "/n")


# ----------------------------------------------------------------------------------------------------------------------
# BEGIN PROGRAM"
# ----------------------------------------------------------------------------------------------------------------------

print(encrypt(infile, key, outfile))
