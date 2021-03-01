""" -------------------------------------------------------------------------------------------------------------------
ITEC 136: Homework 07_02

Modify your first program to print count of the words instead of percentage of the letters.
In this exercise you will get your input from a file.
Case should be ignored.
Write functions to analyze the words in file.


@author: Dani Hooven
@version: 10/20/2020

-------------------------------------------------------------------------------------------------------------------- """

f = open('data.txt', 'r')

count = {}

for line in f:
    for word in line.split():

        # remove punctuation
        word = word.replace('_', '').replace('"', '').replace(',', '').replace('.', '')
        word = word.replace('-', '').replace('?', '').replace('!', '').replace("'", "")
        word = word.replace('(', '').replace(')', '').replace(':', '').replace('[', '')
        word = word.replace(']', '').replace(';', '')

        # ignore case
        word = word.lower()

        # ignore number
        if word.isalpha():
            if word in count:
                count[word] = count[word] + 1
            else:
                count[word] = 1
keys = count.keys()
# keys.sort()

for word in sorted(keys):
    print(word, " ", str(count[word]))



