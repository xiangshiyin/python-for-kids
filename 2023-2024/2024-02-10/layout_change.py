import tkinter as tk

window = tk.Tk()
window.title("Tic Tac Toe")

l1 = tk.Label(text="Hello World")
l1.grid(row=0, column=0)

b1 = tk.Button(text="Click me")
b1.grid(row=0, column=1)

b2 = tk.Button(text="Click me")
b2.grid(row=0, column=2)

b3 = tk.Button(text="Click me")
b3.grid(row=1, column=0)

b4 = tk.Button(text="Click me")
b4.grid(row=1, column=1)

b5 = tk.Button(text="Click me")
b5.grid(row=1, column=2)

window.mainloop()
