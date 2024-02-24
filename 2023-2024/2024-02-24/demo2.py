import tkinter as tk

# create the window
window = tk.Tk()
window.title("Counter")


window.rowconfigure(weight=1, index=0)
for j in range(3):
    window.columnconfigure(weight=1, index=j)


def increase():
    # 1. get the current label value
    curr_val = l1.cget("text")
    new_val = int(curr_val) + 1

    # 2. update the value by increasing it by 1
    ## make sure the label display the updated value (+1)
    l1.config(text=f"{new_val}")


def decrease():
    # 1. get the current label value
    curr_val = l1.cget("text")
    new_val = int(curr_val) - 1

    # 2. update the value by decreasing it by 1
    ## make sure the label display the updated value (-1)
    l1.config(text=f"{new_val}")


# add the widgets (2 buttons and 1 label in the middle)
b1 = tk.Button(text="-", command=decrease)
b1.grid(row=0, column=0)

l1 = tk.Label(text="0")
l1.grid(row=0, column=1)

b2 = tk.Button(text="+", command=increase)
b2.grid(row=0, column=2)

# make the window interactive
window.mainloop()
