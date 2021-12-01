# importing package
import turtle

# set bgcolor, pensize and speed
turtle.bgcolor("black")
turtle.pensize(2)
turtle.speed(0)

# outer loop
for i in range(6):
    # nested loop in list
    # meant a circle is a color
    for colours in ["red",
    "magenta", "blue", "cyan",
    "green", "yellow", "white"]:
        turtle.color(colours)
        turtle.circle(100)
        turtle.left(10)

# hide the turtle or invisible
turtle.hideturtle()

# tell the window don't close
# automatically after a run finished
turtle.mainloop()
