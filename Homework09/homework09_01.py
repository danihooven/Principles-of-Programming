""" -------------------------------------------------------------------------------------------------------------------
ITEC 136: Homework 09 - 01

Given a list of numbers in random order,
write an algorithm that works in O(n2) to sort the list.
Do not use the list sort method or sorted function.

@author: Dani Hooven
@version: 11/06/2020

-------------------------------------------------------------------------------------------------------------------- """

def selectionSort(alist):
    # for each item in list, start check at end and go backwards
   for fillslot in range(len(alist)-1,0,-1):
       positionOfMax=0 # start with assuming index 0 as max
       for location in range(1,fillslot+1): # for each item in range of 1 to spot being checked
           if alist[location]>alist[positionOfMax]: # if item is greater than assumed max
               positionOfMax = location # item becomes max

       temp = alist[fillslot] # temporary variable equal to value of item being checked
       alist[fillslot] = alist[positionOfMax] # end of list item being checked is replaced with maximum value
       alist[positionOfMax] = temp # value of previous last item is placed in the maximum value old spot - switch

alist = [54,26,93,17,77,31,44,55,20]
selectionSort(alist)
print(alist)



