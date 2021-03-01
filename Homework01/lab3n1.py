import turtle
import sys

#sys.setExecutionLimit(1500000)


def seq3np1(n):
    """ Print the 3n+1 sequence from n, terminating when it reaches 1."""
    count = 0
    while n != 1:
        # print(n)
        count += 1
        if n % 2 == 0:  # n is even
            n = n // 2
        else:  # n is odd
            n = n * 3 + 1
    # print(n)                  # the last print is 1
    return (count)


def drawTurtle(t, height):
    """ Get turtle t to draw one bar, of height. """
    t.write(str(height))  # write x,y values on bottom
    t.up()
    t.left(90)
    t.forward(10)
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
    t.forward(10)
    t.left(90)
    t.down()


window = turtle.Screen()
awesome = turtle.Turtle()
awesome.color('red')
awesome.fillcolor('pink')
# awesome.pensize(2)
awesome.speed(100)
upbound = 50
border = 2
numbars = upbound
maxheight = 120
maxsofar = 0
window.bgcolor("lightblue")
window.setworldcoordinates(0 - border, 0 - border, 20 * numbars + border, maxheight + border)

for i in range(1, upbound + 1):
    start = i
    result = seq3np1(start)
    drawTurtle(awesome, result)
    if result > maxsofar:
        maxsofar = result
    # print(" value:", start, " number of items:", xs)

print(maxsofar)

window.exitonclick()
