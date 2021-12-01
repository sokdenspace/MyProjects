#  --------------------------
# | *If Error Follow Step*   |
# | Pre-installed: Python    |
# | cmd: pip install turtle  |
# | https://www.sokden.com/  |
#  --------------------------

# import the turtle modules all
from turtle import *

# return or set pencolor
# and fillcolor
color("red", "yellow")
begin_fill()

# check while statement
# is true working
while True:
    # move or draw
    forward(200)
    left(170)
    # check decision
    if abs(pos()) < 1:
        break
end_fill()
# using screen events
done()
