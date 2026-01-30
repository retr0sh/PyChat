#import os
#import math
from tkinter import *
from tkinter import ttk

def set_user_name():
    global user_name
    if user_name_box.get() == "":
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
root.geometry("960x540")
root.resizable(False, False)

title = Label(root, text="PyChat", font=("Arial", 10))
title.place(x=0, y=0)

user_name_box = ttk.Entry()
user_name_box.place(x=0, y=50)

user_name_btn = ttk.Button(root, text="Save", command=set_user_name)
user_name_btn.place(x=126, y=48)


massage_box = ttk.Entry(state="disabled")
massage_box.grid(row=0, column=0, padx=0, pady=270)

send_btn = ttk.Button(root, text="Send", state="disabled", command=send_massage)
send_btn.grid(row=0, column=1, padx=0, pady=270)

root.mainloop()
