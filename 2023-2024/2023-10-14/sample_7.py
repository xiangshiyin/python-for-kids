"""
Available commands:
    f: go forward 100 units
    b: go backward 100 units
    r: turn right 90 degrees
    l: turn left 90 degrees
    stop: terminate the game
If wrong command is typed in, say
    "WRONG COMMAND!!"
"""

import turtle

t = turtle.Turtle()



start = input("Do you want to start the game? [Y/N]")

if start.lower() in ['y', 'yes']:
    print("GAME STARTED")
    print("##########")

while True:
    command = input("What next?\n")
    if command.lower() == 'f':
        t.forward(100)
    elif command.lower() == 'b':
        t.backward(100)
    elif command.lower() == 'l':
        t.left(90)
    elif command.lower() == 'r':
        t.right(90)
    elif command.lower() == "stop":
        break
    else:
        print("WRONG COMMAND")

turtle.done()
print("##########")
print("GAME ENDED")
