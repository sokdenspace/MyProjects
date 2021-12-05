#  --------------------------
# | *If Error Follow Step*   |
# | Pre-installed: Python    |
# | cmd: pip install turtle  |
# | https://www.sokden.com/  |
#  --------------------------

# import turtle modules
import turtle

# create two object(pen)
sokden = turtle.Turtle()
cir = turtle.Turtle()

# hide first object(pen)
sokden.hideturtle()

# set position to start
cir.penup()
cir.goto(0, -150)
cir.pendown()

# create the circle
cir.color("#1877f2")
cir.begin_fill()
cir.circle(150)
cir.end_fill()
cir.hideturtle()

# start line at the left
sokden.begin_fill()
sokden.color("white")
sokden.penup()
sokden.goto(-35, -150)
sokden.pendown()
sokden.left(90)
sokden.forward(110)

# show first object(pen)
sokden.showturtle()

# start the left rectangle
sokden.left(90)
sokden.forward(50)
sokden.right(90)
sokden.forward(50)
sokden.right(90)
sokden.forward(50)
sokden.left(90)
sokden.forward(30) # first line at corner

# draw the first curve
for i in range(90):
	sokden.right(1)
	sokden.forward(1)

sokden.forward(45) # second line at corner
sokden.right(90)
sokden.forward(50)
sokden.right(90)
sokden.forward(20) # third line at corner

# draw the second curve
for j in range(50):
	sokden.left(2)
	sokden.forward(1.1)

# start the right rectangle
sokden.left(80)
sokden.forward(50)
sokden.right(90)
sokden.forward(50)
sokden.right(90)
sokden.forward(50)

# end line at the right
sokden.left(90)
sokden.forward(113)
sokden.penup()
sokden.goto(-35, -150)
sokden.pendown()
sokden.end_fill()

# write the text
sokden.penup()
sokden.goto(0, -220)
sokden.pendown()
sokden.color("black")
sokden.write("Facebook", move=False,
align="center", font=("Arial", 40, "bold"))

# hide pen & keep window running
sokden.hideturtle()
turtle.mainloop()
