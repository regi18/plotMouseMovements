"""
Plot raw mouse data.
For example if you pass as input a copy of '/dev/input/mice' it will replay everything done on a plot.
Created by: regi18
Version: 2.0.0
Github: https://github.com/regi18/plotMouseMovements
"""

import turtle
from struct import unpack
import argparse

data = [[0, 0, 0]]


# Sets the arguments (launch the program with --help to see them better)
parser = argparse.ArgumentParser()
parser.add_argument("inputfile", help="the input file (raw mouse data, e.g. from /dev/input/mice)", nargs="+", type=str, default=8)
parser.add_argument('--scale', help="set the scale of the plot", nargs="?", type=int, default=8)
parser.add_argument('--speed', help="set the speed of the drawing", nargs="?",type=int, default=5)
parser.add_argument('--click', help="update plot relative to mouse clicks; (1 = Update on mouse clicks, 0 = Do NOT update on mouse clicks)", 
    nargs="?",type=int, default=1, metavar="0;1")
args = parser.parse_args()


# Read mouse data from file
def getMouseEvent():
    button, x, y = unpack('3b', f.read(3))
    # Add the data to the list. Since the coordinates are relative to the
    # last movement, add to the received value the last in the list
    data.append([x + (data[len(data) - 1][0]), y + (data[len(data) - 1][1]), button])


f = open(args.inputfile[0], "rb")
try:
    while True:
        getMouseEvent()
finally:

    # Setup turtle
    screen = turtle.Screen()
    turtle.tracer(0, 0)
    t = turtle.Turtle()
    t.setposition(0, 0)
    t.hideturtle()
    t.speed(args.speed)

    # iterate over the data
    for i in data:
        # If left button clicked, write on plot
        if i[2] & 0x1:
            t.pendown()
            t.setposition(i[0] / args.scale + 250, i[1] / args.scale)  # set coordinates
        else:
            t.penup()
            # Check for arg "--click";
            if (args.click):
                turtle.update()

    # Update at the end if arg "--click" is checked
    if (args.click == 0):
        turtle.update()

    turtle.exitonclick()
    f.close()
    exit()
