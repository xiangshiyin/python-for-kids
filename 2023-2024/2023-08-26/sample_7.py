# draw a circle with Turtle
import turtle

t = turtle.Turtle()
radius = 100
t.circle(radius, 90)
t.left(90)
t.forward(200)
t.right(90)
t.circle(-radius, 90)
t.right(90)
t.forward(200)
turtle.done()
