# import turtle libraries
import turtle

# create the object(pen)
sokden = turtle.Turtle()

# start filling colour & pen position
sokden.begin_fill()
sokden.color("#00a4ef")
sokden.penup()
sokden.goto(-100, 100)
sokden.pendown()

# create a square shape
for i in range(4):
    sokden.forward(200)
    sokden.right(90)

sokden.end_fill()

# set colour & new position pen
sokden.color("white")
sokden.penup()
sokden.forward(100)
sokden.pendown()

# set plus sign in the shape
sokden.right(90)
sokden.width(10)
sokden.forward(200)
sokden.penup()
sokden.goto(-100, 0)
sokden.pendown()
sokden.right(-90)
sokden.forward(200)

# set text colour & text position
sokden.color("#00a4ef")
sokden.penup()
sokden.goto(5, -160)
sokden.pendown()
sokden.write("Windows 11", move = False,
align = "center", font = ("Arial", 24, "bold"))

# to hide pen & keep window running
sokden.hideturtle()
turtle.done()
