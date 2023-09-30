import turtle

t = turtle.Turtle()
t.pen(pencolor="red", fillcolor="white", pensize=30, speed=9)
t.begin_fill()
t.circle(90)
t.end_fill()

t.penup()
t.speed(1)
t.goto(0, 90)
t.pendown()
t.dot(50)
turtle.done()
