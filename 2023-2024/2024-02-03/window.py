import tkinter as tk
from tkinter import messagebox


window = tk.Tk()
window.title("game board")
greeting = tk.Label(text="hello")
greeting.pack()

label = tk.Label(
    text="Hello, Tkinter",
    foreground="white",  # Set the text color to white
    background="black",  # Set the background color to black
    width=10,
    height=10,
)
label.pack()

button = tk.Button(
    text="Click me!",
    width=25,
    height=5,
    fg="black",
    bg="white",
)
button.pack()

entry = tk.Entry(fg="yellow", bg="blue", width=50)
entry.pack()

messagebox.showinfo("Tic Tac Toe", "You've got a message!")


window.mainloop()
