import turtle

t = turtle.Turtle()
t.speed(5)
colours=["red","blue","yellow","brown","black","purple","green"]

t.penup(); t.left(90); t.forward(200);t.right(90);t.pendown()
for i in range (0,18):
    t.pencolor(colours[i%7])
    t.right(20)
    t.forward(50)

t.right(180)
t.home()  
turtle.done()
