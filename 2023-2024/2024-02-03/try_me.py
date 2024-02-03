import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title("Tic Tac Toe")


def popwindow():
    messagebox.showinfo("pop message", entry.get())


entry = tk.Entry()
entry.pack()

button = tk.Button(text="click me", command=popwindow)
button.pack()

window.mainloop()
