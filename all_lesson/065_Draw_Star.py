#  --------------------------
# | *If Error Follow Step*   |
# | Pre-installed: Python    |
# | cmd: pip install turtle  |
# | https://www.sokden.com/  |
#  --------------------------

# import turtle modules
import turtle

# create an object(pen)
sokden = turtle.Turtle()

# set speed & pen size
sokden.speed("fastest")
sokden.pensize(1)

# loop 200 times
for i in range(200):
    sokden.forward(3 * i)
    sokden.left(20)
    sokden.right(175)

# keep window open
turtle.done()
