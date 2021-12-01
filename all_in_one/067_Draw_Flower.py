# import turtle packages
import turtle

# create the object(pen)
sokden = turtle.Turtle()

# set colour, speed, pensize & position
sokden.color("black", "#58bf3b")
sokden.begin_fill()
sokden.speed("fastest")
sokden.pensize(2)
sokden.goto(0, -100)
sokden.right(90)
sokden.goto(0, -100)

# draw the curve
def curve():
    for i in range(100):
        sokden.forward(1.5)
        sokden.left(-2)
curve()

# draw the same shape 7 times
for j in range(7):
    sokden.goto(0, 0)
    sokden.right(205)
    sokden.forward(100)
    curve()

# draw the trunk
sokden.goto(0, -118)
sokden.end_fill()
sokden.color("#5f3014")
sokden.pensize(10)
sokden.goto(0, -200)

# draw the left line
sokden.color("#633a2a", "#b77054")
sokden.begin_fill()
sokden.pensize(5)
sokden.left(65)
sokden.forward(100)
sokden.left(110)
sokden.forward(100)
sokden.left(70)
sokden.forward(132)

# draw the right line
sokden.left(70)
sokden.forward(100)
sokden.goto(0, -200)
sokden.end_fill()

# to hide obj & keep window running
sokden.hideturtle()
turtle.mainloop()
