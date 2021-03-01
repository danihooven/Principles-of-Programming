""" -------------------------------------------------------------------------------------------------------------------
ITEC 136: Homework 05_02

Please create your tree by customizing the following code.

• Modify the thickness of the branches so that as the branchLen gets smaller, the line gets thinner.
• Modify the color of the branches so that as the branchLen gets very short it is colored like a leaf.

@author: Dani Hooven
@version: 10/06/2020

-------------------------------------------------------------------------------------------------------------------- """

# ----------------------------------------------------------------------------------------------------------------------
# IMPORT
# ----------------------------------------------------------------------------------------------------------------------

import turtle


# ----------------------------------------------------------------------------------------------------------------------
# FUNCTIONS
# ----------------------------------------------------------------------------------------------------------------------

def tree(branch_len, t, thick, c):
    if branch_len > 5:
        t.width(thick)
        t.color(c)
        t.forward(branch_len)
        t.right(20)
        tree(branch_len - 15, t, thick - 1, "green")
        t.left(40)
        tree(branch_len - 15, t, thick - 1, "green")
        t.right(20)
        t.width(thick)
        t.color(c)
        t.backward(branch_len)


def main():
    t = turtle.Turtle()
    my_win = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    # t.color("brown")
    tree(75, t, 5, "brown")
    my_win.exitonclick()


# ----------------------------------------------------------------------------------------------------------------------
# BEGIN PROGRAM
# ----------------------------------------------------------------------------------------------------------------------

main()
