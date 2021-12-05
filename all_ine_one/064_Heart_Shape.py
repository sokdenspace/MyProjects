#  --------------------------
# | *If Error Follow Step*   |
# | Pre-installed: Python    |
# | cmd: pip install turtle  |
# | https://www.sokden.com/  |
#  --------------------------

# import turtle package
import turtle

# create a turtle object(pen)
sokden = turtle.Turtle()

# set color & start fill color
sokden.color("black", "red")
sokden.begin_fill()

# defining a method to draw curve
def curve():
    for i in range(200):
        sokden.right(1)
        sokden.forward(1)

# draw the left line
sokden.left(140)
sokden.forward(113)

# draw the left curve
curve()
sokden.left(120)

# draw the right curve
curve()

# draw the right line & end fill color
sokden.forward(112)
sokden.end_fill()

# set text position & write text
sokden.penup()
sokden.goto(0, 90)
sokden.pendown()
sokden.write("sokden.com", move=False,
align="center", font=("Arial", 18, "normal"))

# to hide turtle & keep window open
sokden.ht()
turtle.done()