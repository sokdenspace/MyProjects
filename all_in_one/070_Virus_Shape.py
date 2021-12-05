#  --------------------------
# | *If Error Follow Step*   |
# | Pre-installed: Python    |
# | cmd: pip install turtle  |
# | https://www.sokden.com/  |
#  --------------------------

# import turtle packages
import turtle

# create the two object(pen)
sokden = turtle.Turtle()
sokden.penup()
sokden.goto(300, 50)
sokden.pendown()
sokden.speed(20)
sokden.color("cyan")
turtle.bgcolor("black")

# draw virus shape here
count = 200
while count > 0:
    sokden.left(count)
    sokden.forward(count * 3)
    count = count - 1

# write the text here
sokden.penup()
sokden.goto(0, -360)
sokden.pendown()
sokden.color("white")
sokden.write("Coronavirus", move=False,
align="center", font=("Arial", 40, "bold"))

# hide & keep window running
sokden.hideturtle()
turtle.done()
