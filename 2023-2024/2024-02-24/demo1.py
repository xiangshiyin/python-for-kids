import tkinter as tk

window = tk.Tk()
window.title("Tic Tac Toe")

for i in range(3):
    window.rowconfigure(weight=1, index=i)

for j in range(3):
    window.columnconfigure(weight=1, index=j)


def create_buttons(rows, columns):
    buttons = []
    for i in range(rows):
        for j in range(columns):
            b = tk.Button(text="Click\n\nme")
            b.grid(row=i, column=j)
            buttons.append(b)
    return buttons


buttons = create_buttons(rows=3, columns=3)

window.mainloop()
