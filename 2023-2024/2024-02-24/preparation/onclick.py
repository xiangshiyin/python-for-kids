"""
Change the text of the button when clicked
"""

import tkinter as tk


# automate the board creation
def create_buttons(rows, columns):
    buttons = []
    for i in range(rows):
        window.rowconfigure(i, weight=1, minsize=50)
    for j in range(columns):
        window.columnconfigure(j, weight=1, minsize=75)

    for i in range(rows):
        for j in range(columns):
            b = tk.Button(
                text="",
                width=6,
                height=3,
                command=lambda row=i, col=j: click(row, col),
            )
            b.grid(row=i, column=j)
            buttons.append(b)
    return buttons


def click(row, col):
    buttons[row * 3 + col].config(text="X")


window = tk.Tk()
window.title("Tic Tac Toe")
buttons = create_buttons(rows=3, columns=3)
window.mainloop()
