"""
Change the text on the button with alternating X and O
"""

import tkinter as tk

class game:
    def __init__(self):
        self.player = 1
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe")
        self.buttons = self.create_buttons(rows=3, columns=3)
        self.window.mainloop()

    # automate the board creation
    def create_buttons(self, rows, columns):
        buttons = []
        for i in range(rows):
            self.window.rowconfigure(i, weight=1, minsize=50)
        for j in range(columns):
            self.window.columnconfigure(j, weight=1, minsize=75)

        for i in range(rows):
            for j in range(columns):
                b = tk.Button(
                    text="",
                    width=6,
                    height=3,
                    command=lambda row=i, col=j: self.click(row, col),
                )
                b.grid(row=i, column=j)
                buttons.append(b)
        return buttons

    def click(self, row, col):
        if self.player == 1:
            self.buttons[row * 3 + col].config(text="O")
        else:
            self.buttons[row * 3 + col].config(text="X")
        self.change_player()

    def change_player(self):
        if self.player == 1:
            self.player = 2
        else:
            self.player = 1


game()
