import tkinter as tk

window = tk.Tk()
window.title("Tic Tac Toe")


def react():
    l1 = tk.Label(text="hello hello")
    l1.pack()


b1 = tk.Button(text="Click me", command=react)
b1.pack()


window.mainloop()
