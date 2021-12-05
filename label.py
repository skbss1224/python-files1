from tkinter import *
from tkinter.font import Font
win=Tk()
win.title('my app')
win.resizable(height="false",width="false")
win.geometry("500x500")
myfont=Font(family="times",size=20,weight="bold")
lab=Label(win,text="my tkinder",Font=myfont,bg="#0a3d62",fg="white",padx=20,pady=20,relief="raised")
lab.pack()
win.mainloop()