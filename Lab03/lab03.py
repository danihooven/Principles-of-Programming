""" -------------------------------------------------------------------------------------------------------------------
ITEC 136: Lab 03

Develop a program that asks the user to enter a text.

The program should analyze the text and print out unique letters,
in alphabetical order,
with the percentage information of each letter.
Case should be ignored.

Write a function to analyze the text string.
No global variables are used in the function.
Function parameters must be used.


@author: Dani Hooven
@version: 10/20/2020

-------------------------------------------------------------------------------------------------------------------- """

import turtle

def drawTurtle(t, c, height):
    """ Get turtle t to draw one bar, of height. """
    # -----------------------
    t.up()
    t.write(c)  # write character.lkl
    t.left(90)
    t.forward(2)
    t.right(90)
    t.down()
    t.begin_fill()  # start filling this shape
    t.left(90)
    t.forward(height)
    t.right(90)
    t.forward(20)
    t.right(90)
    t.forward(height)
    # t.left(90)
    t.end_fill()  # stop filling this shape
    t.up()
    t.forward(2)
    t.left(90)
    t.down()

#text = input("Enter text: ")

text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore " \
       "magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo " \
       "consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. " \
       "Excep zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz"

alpha = 'abcdefghijklmnopqrstuvwxyz'
text_lower = text.lower()
text_length = 0
max_count = 0
letter_count = {}  # empty dictionary

for char in text_lower:
    if char in alpha:
        if char in letter_count:
            letter_count[char] = letter_count[char] + 1
            if (letter_count[char]) > max_count:
                max_count = letter_count[char]
        else:
            letter_count[char] = 1
            text_length = text_length + 1


window = turtle.Screen()
awesome = turtle.Turtle()
awesome.speed(100)
border = 2
window.bgcolor("lightblue")
window.setworldcoordinates(0 - border, 0 - border, 20 * text_length + border + 20, max_count + border)

keys = letter_count.keys()

percentage = 0
awesome.up()
awesome.left(90)
for i in range(11):
    awesome.write(percentage)
    awesome.forward(max_count * .1)
    awesome.goto(0, awesome.ycor())
    percentage = round(percentage + 0.1, 1)
awesome.right(90)
awesome.goto(0 - border, 0 - border)
awesome.forward(20)


for char in sorted(keys):
    drawTurtle(awesome, char, letter_count[char])

window.exitonclick()
