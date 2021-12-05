from tkinter import *
from tkinter import messagebox
win=Tk()
win.geometry("2000x2000")
win.title("checkbutton")

def submit():
    if(c1.get()==1):
        val=ch1.cget("text")
        #val=c1.get()
        messagebox.showinfo("message",val)

    if (c2.get() == 1):
        val=ch2.cget("text")
        #val = c2.get()
        messagebox.showinfo("message", val)

    if (c2.get() == 1):
        val=ch3.cget("text")
        #val = c2.get()
        messagebox.showinfo("message", val)


def clear():
    ch1.deselect()
    ch2.deselect()
    ch3.deselect()
    messagebox.showinfo("message","Checkbutton cleared")


c1=IntVar()
c2=IntVar()
c3=IntVar()
lbl=Label(win,text='checkbutton',bg="blue",fg="white",padx=30,pady=10,font=("times",15,"bold"))
lbl.pack(fill=X)
ch1=Checkbutton(win,text="java",variable=c1,onvalue=1,offvalue=0)
ch2=Checkbutton(win,text="python",variable=c2,onvalue=1,offvalue=0)
ch3=Checkbutton(win,text="asp.net",variable=c3,onvalue=1,offvalue=0)
ch1.pack()
ch2.pack()
ch3.pack()
btnsub=Button(win,text="submit",bg="green",fg="white",padx=30,pady=40,width=10,font=("times",15,"bold"),command=submit)
btnclr=Button(win,text="clear",bg="red",fg="white",padx=30,pady=40,width=10,font=("times",15,"bold"),command=clear)
btnsub.pack()
btnclr.pack()
win.mainloop()