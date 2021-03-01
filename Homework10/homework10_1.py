""" -------------------------------------------------------------------------------------------------------------------
ITEC 136: Homework 10 - 01

Implement a stack data structure in Python.
Test your code with boundary cases, like trying to remove an element from an already empty stack.
If removing or peek an item from an empty stack, return None instead of throwing an exception.

@author: Dani Hooven
@version: 11/12/2020

-------------------------------------------------------------------------------------------------------------------- """


# ----------------------------------------------------------------------------------------------------------------------
# IMPORT
# ----------------------------------------------------------------------------------------------------------------------


# ----------------------------------------------------------------------------------------------------------------------
# CLASSES
# ----------------------------------------------------------------------------------------------------------------------

class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.isEmpty():
            return "None"
        else:
            return self.items.pop()

    def peek(self):
        if self.isEmpty():
            return "None"
        else:
            return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


# ----------------------------------------------------------------------------------------------------------------------
# FUNCTIONS
# ----------------------------------------------------------------------------------------------------------------------


# ----------------------------------------------------------------------------------------------------------------------
# VARIABLES
# ----------------------------------------------------------------------------------------------------------------------

s = Stack()

# ----------------------------------------------------------------------------------------------------------------------
# BEGIN PROGRAM
# ----------------------------------------------------------------------------------------------------------------------

print(s.isEmpty())
print(s.peek())  # remove an element from an already empty stack
print(s.pop())   # peek an item from an empty stack
s.push(4)
s.push('dog')
print(s.peek())
s.push(True)
print(s.size())
print(s.isEmpty())
s.push(8.4)
print(s.pop())
print(s.pop())
print(s.size())

