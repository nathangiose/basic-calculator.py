from tkinter import *

# function to add the two entries



def add_numbers():
    add = int(Entry_1.get()) + int(Entry_2.get())
    label_text.set(add)

# function to clear the contents


def clear():
    Entry_1.delete(0, END)
    Entry_2.delete(0, END)

# function for the exit button


def exit():
    return root.destroy()
root = Tk()
label_text = StringVar()
root.geometry("600x200")

root.grid_columnconfigure((0, 1), weight=1)

Label_1 = Label(root, text="Please Enter First Number :")
Label_2 = Label(root, text="Please Enter Second Number :")
Label_3 = Label(root, text="Results :")
add = Label(root, text="", textvariable=label_text).grid(row=5, column=1, sticky=W)

Entry_1 = Entry(root)
Entry_2 = Entry(root)

Label_1.grid(row=3, column=0)
Entry_1.grid(row=3, column=1, sticky="ew")
Label_2.grid(row=4, column=0)
Entry_2.grid(row=4, column=1, sticky="ew")
Label_3.grid(row=5, column=0)

b = Button(root, text="Add", command=add_numbers)
b2 = Button(root, text="Clear", command=clear)
b3 = Button(root, text="Exit", command=exit)
b.grid(row=6, column=1, sticky=W+E+N+S, padx=5, pady=5)
b2.grid(row=6, column=2, sticky=W+E+N+S, padx=5, pady=5)
b3.grid(row=6, column=3, sticky=W+E+N+S, padx=5, pady=5)
root.mainloop()
