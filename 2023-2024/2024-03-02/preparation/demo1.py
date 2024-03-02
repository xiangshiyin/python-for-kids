import tkinter as tk
from tkinter import messagebox


class game:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe")
        for i in range(3):
            self.window.rowconfigure(weight=1, index=i)
        for j in range(3):
            self.window.columnconfigure(weight=1, index=j)

        self.player = "X"

        self.board = self.create_buttons(rows=3, columns=3)
        self.board_tracker = [" " for i in range(3 * 3)]
        self.window.mainloop()

    def switch_player(self):
        # self.player = "O" if self.player == "X" else "X"
        if self.player == "X":
            self.player = "O"
        else:
            self.player = "X"

    def click(self, row, column):
        curr_mark = self.board[3 * row + column].cget("text")
        if curr_mark not in ["X", "O"]:
            self.board[3 * row + column].config(text=self.player)
            self.board_tracker[3 * row + column] = self.player
            if self.check_winner():
                messagebox.showinfo("Tic Tac Toe", f"Player {self.player} wins!")
            elif self.check_tie():
                messagebox.showinfo("Tic Tac Toe", f"It's a tie!")

            self.switch_player()

    # check winner
    ## if there is a winner, terminate the game and pop up message "X is the winner"
    def check_winner(self):
        for i in range(0, 9, 3):
            if (
                self.board_tracker[i]
                == self.board_tracker[i + 1]
                == self.board_tracker[i + 2]
                != " "
            ):
                return True

        for j in range(3):
            if (
                self.board_tracker[j]
                == self.board_tracker[j + 3]
                == self.board_tracker[j + 6]
                != " "
            ):
                return True

        if (
            self.board_tracker[0]
            == self.board_tracker[4]
            == self.board_tracker[8]
            != " "
        ) or (
            self.board_tracker[2]
            == self.board_tracker[4]
            == self.board_tracker[6]
            != " "
        ):
            return True

    # check tie
    ## if this is a tie, terminate the game and pop up message "This is a tie"
    def check_tie(self):
        for i in range(9):
            if self.board_tracker[i] == " ":
                return False
        return True

    def create_buttons(self, rows, columns):
        buttons = []
        for i in range(rows):
            for j in range(columns):
                b = tk.Button(
                    text=" ",
                    command=lambda row=i, column=j: self.click(row, column),
                )
                b.grid(row=i, column=j)
                buttons.append(b)
        return buttons


g = game()
