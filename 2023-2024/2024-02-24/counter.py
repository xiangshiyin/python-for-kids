import tkinter as tk


def increment():
    value = int(l1["text"])
    print(value)
    l1["text"] = f"{value + 1}"


def decrement():
    value = int(l1["text"])
    print(value)
    l1["text"] = f"{value - 1}"


window = tk.Tk()
window.title("Counter")

b1 = tk.Button(text="+", width=6, height=3, command=increment)
b1.grid(row=0, column=0)

l1 = tk.Label(text="0", width=6, height=3)
l1.grid(row=0, column=1)

b2 = tk.Button(text="-", width=6, height=3, command=decrement)
b2.grid(row=0, column=2)


window.mainloop()
