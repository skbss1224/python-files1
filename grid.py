from tkinter import *
win=Tk()
win.geometry("2000x2000")
win.title("grid")
lbltitle=Label(win,text="REGISTRATION",bg="pink",fg="black",padx=30,pady=10,font=("times",15,"bold"))
lbltitle.grid(columnspan=2)
lblname=Label(win,text="NAME",fg="black",padx=30,pady=10,font=("times",15,"bold"))
lblname.grid(row=1,column=0)
txtname=Entry(win,font=("times",15,"bold"))
txtname.grid(row=1,column=1)
lblmail=Label(win,text="E-MAIL",fg="black",padx=30,pady=10,font=("times",15,"bold"))
lblmail.grid(row=2,column=0)
txtmail=Entry(win,font=("times",15,"bold"))
txtmail.grid(row=2,column=1)
lbladdress=Label(win,text="ADDRESS",fg="black",padx=30,pady=10,font=("times",15,"bold"))
lbladdress.grid(row=3,column=0)
txtaddress=Entry(win,font=("times",15,"bold"))
txtaddress.grid(row=3,column=1)
btnsub=Button(win,text="SUBMIT",bg="green",fg="black",padx=20,pady=5,width=5,font=("times",15,"bold"))
btnsub.grid(row=4,column=1,sticky=E)
btnclr=Button(win,text="CLEAR",bg="red",fg="black",padx=20,pady=5,width=5,font=("times",15,"bold"))
btnclr.grid(row=4,column=1,sticky=W)
win.mainloop()