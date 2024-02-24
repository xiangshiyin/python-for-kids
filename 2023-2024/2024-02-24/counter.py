import tkinter as tk

window = tk.Tk()
window.title("Counter")

b1 = tk.Button(text="+", width=6, height=3, command=lambda: increment)
b1.grid(row=0, column=0)

l1 = tk.Label(text="0", width=6, height=3)
l1.grid(row=0, column=1)

b2 = tk.Button(text="-", width=6, height=3, command=lambda: decrement)
b2.grid(row=0, column=2)

def increment():
    l1.config(text=int(l1.get("text")) + 1)

def decrement():
    l1.config(text=int(l1.get("text")) - 1)

window.mainloop()