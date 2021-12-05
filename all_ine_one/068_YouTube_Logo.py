#  --------------------------
# | *If Error Follow Step*   |
# | Pre-installed: Python    |
# | cmd: pip install turtle  |
# | https://www.sokden.com/  |
#  --------------------------

# Import turtle modules
import turtle

# Create an object(pen)
sokden = turtle.Turtle()

# Set position to start
sokden.color("black", "red")
sokden.begin_fill()
sokden.penup()
sokden.goto(-100, 100)
sokden.pendown()
sokden.forward(200)

# Draw the curve at corner
def curve():
    for i in range(90):
        sokden.right(1)
        sokden.forward(1)
curve()
sokden.forward(100)
curve()
sokden.forward(200)
curve()
sokden.forward(100)
curve()
sokden.end_fill()

# Draw the triangle shape
sokden.color("black", "white")
sokden.begin_fill()
sokden.penup()
sokden.goto(50, 0)
sokden.pendown()

sokden.goto(-50, -50)
sokden.goto(-50, 50)
sokden.goto(50, 0)
sokden.end_fill()

# Set the text position & write
sokden.penup()
sokden.goto(0, -200)
sokden.pendown()
sokden.write("YouTube", move=False,
align="center", font=("Arial", 40, "bold"))

# To hide pen & keep window running
sokden.hideturtle()
turtle.mainloop()
