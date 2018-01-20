## Making some patterns with python turtles. Run in python 3.
## Author: Jason Kolbly - jason@rscheme.org

import turtle

turtle.mode("logo")

screen = turtle.Screen()

screen.tracer(0,0)

joe = turtle.Turtle()
joe.shape("turtle")
joe.speed(10)

steve = joe.clone()
fred = joe.clone()
bob = joe.clone()

joe.setheading(0)
steve.setheading(90)
fred.setheading(180)
bob.setheading(270)

turtle_list = [joe, steve, fred, bob]


for x in range(270):
    for i in turtle_list:
        i.forward(1)
        i.right(1)
    screen.update()

for i in turtle_list:
    i.penup()

for x in range(90):
    for i in turtle_list:
        i.forward(1)
        i.right(1)
    screen.update()

for i in turtle_list:
    i.pendown()
    i.stamp()
    i.hideturtle()
    for x in range(180):
        i.forward(1)
        i.right(1)
    i.left(45)

for x in range(163):
    for i in turtle_list:
        i.forward(1)
        i.right(1)
        screen.update()

for i in turtle_list:
    i.left(135)

for x in range(177):
    for i in turtle_list:
        i.forward(1)
        i.right(1)
        screen.update()

for i in turtle_list:
    i.penup()
    i.home()
    i.pendown()

screen.update()
