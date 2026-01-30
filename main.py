#import os
#import math
from tkinter import *
from tkinter import ttk


def set_user_name():
    global user_name
    if user_name_box.get() == "" or user_name_box.get() == "admin":
        pass
    else:
        user_name = user_name_box.get()
        user_name_box.config(state="disabled")
        user_name_btn.config(state="disabled")
        massage_box.config(state="normal")
        send_btn.config(state="normal")


def send_massage():
    if massage_box.get() == "":
        pass
    else:
        print(user_name, ":", massage_box.get())
        massage_box.delete(0, END)


user_name = ""

root = Tk()
root.title("PyChat")
root.iconbitmap("icon.ico")
root.geometry("750x540")
root.resizable(False, False)

root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)


title = Label(root, text="PyChat", font=("Arial", 14, "bold"))
title.place(x=10, y=0)

user_name_label = Label(root, text="User Name:")
user_name_label.place(x=300, y=5)

user_name_box = ttk.Entry()
user_name_box.place(x=370, y=5)

user_name_btn = ttk.Button(root, text="Save", command=set_user_name)
user_name_btn.place(x=500, y=4)


massage_window = Text(width=70, height=20)
massage_window.place(x=10, y=30)

massage_box = ttk.Entry(state="disabled", width=80)
massage_box.place(x=10, y=360)

send_btn = ttk.Button(text="Send", state="disabled", command=send_massage)
send_btn.place(x=500, y=358)


root.mainloop()
