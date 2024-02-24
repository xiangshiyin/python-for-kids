import tkinter as tk
from tkinter import messagebox

class game:
    def __init__(self):
        self.create_board()
        self.player = 1
        self.winner = 0
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe")
        self.buttons = self.create_buttons(rows=3, columns=3)
        self.window.mainloop()

    def create_board(self):
        self.board = ["_"] * 9

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
        mark = "O" if self.player == 1 else "X" 
        self.buttons[row * 3 + col].config(text=mark)
        self.board[row * 3 + col] = mark
        print(self.board)
        self.change_player()
        if self.check_winner():
            messagebox.showinfo(
                "Tic Tac Toe", f"Player {self.winner} wins!"
            )

    def change_player(self):
        if self.player == 1:
            self.player = 2
        else:
            self.player = 1
    
    def get_player(self, mark):
        if mark == "O":
            return 1
        else:
            return 2

    def check_winner(self):
        for i in range(0, 9, 3):
            if self.board[i] == self.board[i + 1] == self.board[i + 2] != "_":
                self.winner = self.get_player(self.board[i])
                print(f"Winner: {self.winner}")
                return True
        
        for j in range(3):
            if self.board[j] == self.board[j + 3] == self.board[j + 6] != "_":
                self.winner = self.get_player(self.board[j])
                print(f"Winner: {self.winner}")
                return True
            
        if (self.board[0] == self.board[4] == self.board[8] != "_") or (self.board[2] == self.board[4] == self.board[6] != "_"):
            self.winner = self.get_player(self.board[4])
            print(f"Winner: {self.winner}")
            return True


game()
