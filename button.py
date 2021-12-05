from tkinter import *
from tkinter.font import Font
from tkinter import messagebox
win=Tk()
def submit():
    #btnsub=Label(win,text="submit button clicked",fg="green",font=myfont)
    #btnsub.pack()
    messagebox.showinfo("messagebox","submit button clicked")
def clear():
    #btnclr=Label(win,text="clear button clicked",fg="red",font=myfont)
    #btnclr.pack()
    messagebox.showinfo("messagebox", "clear button clicked")
win.geometry("500x500")
win.title("button")
myfont=Font(family="times",size=15,weight="bold")
sub=Button(win,text="submit",bg="green",fg="white",padx=30,pady=10,width=10,font=myfont,activebackground="#009432",activeforeground="yellow",command=submit)
sub.pack(fill=BOTH,expand="true")
myfont1=Font(family="times",size=15,weight="bold")
clr=Button(win,text="clear",bg="red",fg="white",padx=30,pady=10,width=10,font=myfont1,activebackground="#ff3838",activeforeground="yellow",command=clear)
clr.pack(fill=BOTH,expand="true")
win.mainloop()