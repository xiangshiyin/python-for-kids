import tkinter as tk
from tkinter import messagebox


def display_input():
    user_input = entry.get()
    label["text"] = user_input
    # messagebox.showinfo("a", "testing testing")


window = tk.Tk()
window.title("User Input Display")

# Entry widget to collect user input
entry = tk.Entry(width=30)
entry.grid(row=0, column=0)
# entry.pack()

# Button to trigger displaying user input
button = tk.Button(text="Display Input", command=display_input)
button.grid(row=0, column=1)
# button.pack()

# Label widget to display user input
label = tk.Label(text="")
label.grid(row=0, column=2)
print(label["text"])
# label.pack()

window.mainloop()
