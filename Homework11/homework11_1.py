""" -------------------------------------------------------------------------------------------------------------------
ITEC 136: Homework 11 - 01
Given a list of numbers in random order, write insertion sort algorithm to sort the list.
Discuss the complexity of your solution in terms of Big-O notation.

@author: Dani Hooven
@version: 11/22/2020

-------------------------------------------------------------------------------------------------------------------- """


# ----------------------------------------------------------------------------------------------------------------------
# IMPORT
# ----------------------------------------------------------------------------------------------------------------------


# ----------------------------------------------------------------------------------------------------------------------
# FUNCTIONS
# ----------------------------------------------------------------------------------------------------------------------

def insertion_sort(alist):
    for index in range(1, len(alist)):

        currentvalue = alist[index]
        position = index

        while position > 0 and alist[position-1] > currentvalue:
            alist[position] = alist[position-1]
            position = position - 1

        alist[position] = currentvalue


# ----------------------------------------------------------------------------------------------------------------------
# VARIABLES
# ----------------------------------------------------------------------------------------------------------------------

alist = [23, 45, 67, 98, 54, 21, 12, 68, 99]

# ----------------------------------------------------------------------------------------------------------------------
# BEGIN PROGRAM
# ----------------------------------------------------------------------------------------------------------------------

insertion_sort(alist)
print(alist)
