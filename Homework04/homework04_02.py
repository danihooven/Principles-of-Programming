""" -------------------------------------------------------------------------------------------------------------------
ITEC 136: Homework 04_02

Develop a program to maintain a list of homework assignments.
When an assignment is assigned, add it to the list with a due date, and when it is completed, remove it.
No global variables are used in the function.
Function parameters must be used.

Your program should provide the following functions:
a.  Add a new assignment.
b.	Remove an assignment.
c.	Provide a list of the assignments in the order they were assigned.
    The output should display each assignment line by line.
d.	Provide a list of the assignments in the order they are due.
    The output should display each assignment line by line.


@author: Dani Hooven
@version: 09/29/2020

-------------------------------------------------------------------------------------------------------------------- """


# ----------------------------------------------------------------------------------------------------------------------
# IMPORT
# ----------------------------------------------------------------------------------------------------------------------


# ----------------------------------------------------------------------------------------------------------------------
# FUNCTIONS
# ----------------------------------------------------------------------------------------------------------------------

def add_assignment(assignment_list, assignment):
    """
    Add Assignment Function - adds new assignment to running list
    :param assignment_list: string
    :param assignment: list item
    :return: updated assignment list
    """
    assignment_list.append(assignment)  # add assignment to assignment_list
    print("Assignment added: ", assignment)


def remove_assignment(assignment_list, assignment):
    """
    Remove Assignment Function - removes existing assignment from running list
    :param assignment_list:
    :param assignment:
    :return: updated assignment list
    """
    # remove an assignment from the assignment list
    if assignment in assignment_list:   # if the assignment exists in list
        assignment_list.remove(assignment)  # removed the assignment
    print("Assignment removed: ", assignment)


def display_assignment(assignment_list):
    """
    Displays List of Assignments
    :param assignment_list:
    :return: assignments
    """
    print("Assignments in the order they were assigned: ")
    for assignment in assignment_list:  # print each assignment line by line
        print(assignment)


def display_assignment_due(assignment_list):
    """
    Displays list of assignments sorted by due date
    :param assignment_list:
    :return: assignments
    """
    assignment_list.sort()  # sort list by date
    print("Assignments in the order they are due")
    for assignment in assignment_list:  # print each assignment line by line
        print(assignment)


# ----------------------------------------------------------------------------------------------------------------------
# SET VARIABLES
# ----------------------------------------------------------------------------------------------------------------------

my_class = []
assignment1 = ["2020/09/29", "ITEC136"]
assignment2 = ["2020/11/11", "COMP204"]
assignment3 = ["2020/10/01", "ENV101"]

# ----------------------------------------------------------------------------------------------------------------------
# BEGIN PROGRAM"
# ----------------------------------------------------------------------------------------------------------------------

add_assignment(my_class, assignment1)  # add a new assignment
add_assignment(my_class, assignment2)
add_assignment(my_class, assignment3)
print()
display_assignment(my_class)  # provide a list of assignments by order assigned
display_assignment_due(my_class)  # provide a list of assignments by due date
print()
remove_assignment(my_class, assignment2)  # remove an assignment
print()
display_assignment(my_class)  # provide a list
display_assignment_due(my_class)  # provide a list
