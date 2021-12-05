#  --------------------------
# | *If Error Follow Step*   |
# | Pre-installed: Python    |
# | cmd: pip install turtle  |
# | https://www.sokden.com/  |
#  --------------------------

# import the turtle modules all
from turtle import *

# set speed, bgcolor,
# color and pensize
speed(5)
bgcolor("black")
color("greenyellow")
pensize(5)

for i in range(8):
    left(45) # degree
    for i in range(8):
        forward(100) # distance
        right(45) # degree

hideturtle()
# using screen events
done()
