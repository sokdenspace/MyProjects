#  --------------------------
# | *If Error Follow Step*   |
# | Pre-installed: Python    |
# | cmd: pip install turtle  |
# | https://www.sokden.com/  |
#  --------------------------

# import turtle modules
import turtle

# create a obj (point) in
# the middle on the screen
sokden = turtle.Turtle()

# set color, pensize
# speed & fill color
sokden.color("red", "yellow")
sokden.pensize(2)
sokden.speed(5)
sokden.begin_fill()

# loop the same thing 8 times
for i in range(8):
    sokden.forward(200)
    sokden.left(135)
    sokden.forward(200)

# end fill color & keep window open
sokden.end_fill()
turtle.done()