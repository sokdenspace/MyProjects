#  --------------------------
# | *If Error Follow Step*   |
# | Pre-installed: Python    |
# | cmd: pip install turtle  |
# | https://www.sokden.com/  |
#  --------------------------

# import turtle package
import turtle

# set screen, decide colors & pensize
screen = turtle.Turtle()
my_colors = ["red", "green", "blue", "yellow", "purple"]
turtle.pensize(5)

# draw star pattern
turtle.penup()
turtle.setpos(-90, 30)
turtle.pendown()
for i in range(5):
    turtle.pencolor(my_colors[i])
    turtle.forward(200)
    turtle.right(144)

turtle.penup()
turtle.setpos(80, -144)
turtle.pendown()

# choose pen color
turtle.pencolor("Black")
turtle.done()