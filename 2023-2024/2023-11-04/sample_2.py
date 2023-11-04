import turtle

t = turtle.Turtle()

while True:
    cmd = input()
    if cmd == 'q':
        break
    if cmd == 'f':
        t.forward(100)
    elif cmd == 'b':
        t.backward(100)

turtle.done()