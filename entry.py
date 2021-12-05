from tkinter import *
from tkinter.font import Font
win=Tk()
win.title("entry")
win.geometry("500x500")
TxtName=Entry(win,width=30,font=("times",20),bg="#55efc4",fg="orange"
              ,selectbackground="black",selectforeground="yellow",show="*")
TxtName.pack()

win.mainloop()