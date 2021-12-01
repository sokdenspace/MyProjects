#  --------------------------
# | *If Error Follow Step*   |
# | Pre-installed: Python    |
# | cmd: pip install turtle  |
# | https://www.sokden.com/  |
#  --------------------------

# import turtle packages
import turtle

# create an obj (pen)
sokden = turtle.Turtle()

# draw the shape & fill color
turtle.bgcolor("black")
sokden.begin_fill()
sokden.speed(2)
sokden.color("#00adef")
sokden.penup()
sokden.goto(-50, 60)
sokden.pendown()
sokden.goto(100, 100)
sokden.goto(100, -100)
sokden.goto(-50, -60)
sokden.goto(-50, 60)
sokden.end_fill()

# draw symbol plus sign
sokden.color("black")
sokden.goto(15, 100)
sokden.color("black")
sokden.width(10)
sokden.goto(15, -100)
sokden.penup()
sokden.goto(100, 0)
sokden.pendown()
sokden.goto(-100, 0)

# set color, position & text
sokden.color("white")
sokden.penup()
sokden.goto(30, -150)
sokden.pendown()
sokden.write("Windows 10", move = False,
align="center", font = ("Arial", 24, "bold"))

# keep window open
turtle.done()
