""" -------------------------------------------------------------------------------------------------------------------
ITEC 136: Lab 01

Write a program that will race two turtles based on random inputs.

@author: Dani Hooven
@version: 09/22/2020

-------------------------------------------------------------------------------------------------------------------- """

# ----------------------------------------------------------------------------------------------------------------------
# IMPORTS
# ----------------------------------------------------------------------------------------------------------------------

import turtle  # import turtle module
import random  # import random module

# ----------------------------------------------------------------------------------------------------------------------
# SET VARIABLES
# ----------------------------------------------------------------------------------------------------------------------

window = turtle.Screen()  # Create a screen
window.bgcolor("sky blue")  # Change the background color of the screen
window.setworldcoordinates(-20, 0, 20, 50)  # Set screen coordinates

mario = turtle.Turtle()  # Create two turtle objects
luigi = turtle.Turtle()

mario.color("red")  # Give them different colors
luigi.color("green")

mario.shape("turtle")  # Change their shape to turtle
luigi.shape("turtle")  # Change their shape to turtle

mario.up()  # Hold both turtles up.
luigi.up()

mario.left(90)  # Move both turtles to starting point.
mario.goto(-10, 0) # Change starting point as you wish.
luigi.left(90)
luigi.goto(10, 0)


# ----------------------------------------------------------------------------------------------------------------------
# FUNCTIONS
# ----------------------------------------------------------------------------------------------------------------------

# Write the code for racing.
def race(x, y):
    """ Race Function moves two turtles forward a random amount and will stop when one wins or if a tie """
    if mario.ycor() <= 50 and luigi.ycor() <= 50:
        mario.forward(random.randrange(1, 10))
        luigi.forward(random.randrange(1, 10))
    else:  # Stop when one of them wins. Define a criterion for winning.
        if mario.ycor() == luigi.ycor():  # Question: Could the race end in a draw?
            mario.setposition(0, 10)
            luigi.setposition(0, 20)
            mario.shape("classic")
            luigi.shape("classic")
            mario.write("Tie!")
            luigi.write("Tie!")
            window.exitonclick()
        elif mario.ycor() >= 50:
            mario.shape("classic")
            mario.setposition(0, 25)
            mario.write("Mario is the winner!")
            window.exitonclick()
        elif luigi.ycor() >= 50:
            luigi.shape("classic")
            luigi.setposition(0, 25)
            luigi.write("Luigi is the winner!")
            window.exitonclick()


# ----------------------------------------------------------------------------------------------------------------------
# BEGIN PROGRAM"
# ----------------------------------------------------------------------------------------------------------------------

window.onclick(race)    # With each mouse click, forward each turtle random distance.

window.mainloop()



