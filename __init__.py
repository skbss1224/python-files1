from functools import partial
from tkinter import *
import pymysql


def validateLogin(username, password):
	print("username entered :", username.get())
	print("password entered :", password.get())
	return
tkWindow = Tk()
tkWindow.config(bg='gold')
tkWindow.geometry('500x500')
tkWindow.title('log in form')
usernameLabel = Label(tkWindow, text="User Name",font="times",bg="gold",fg="blue",padx=10,pady=10).grid(row=0, column=0)
username = StringVar()
usernameEntry = Entry(tkWindow, textvariable=username).grid(row=0, column=1)
passwordLabel = Label(tkWindow,text="Password",font="times",fg="blue",bg="gold",padx=10,pady=10).grid(row=1, column=0)
password = StringVar()
passwordEntry = Entry(tkWindow, textvariable=password, show='*').grid(row=1, column=1)

validateLogin = partial(validateLogin, username, password)

loginButton = Button(tkWindow, text="Login", command=validateLogin,font="times",bg="green",fg="white").grid(row=10, column=0)
tkWindow.mainloop()