from tkinter import *
win=Tk()
win.geometry("2000x2000")
win.title("frame")
frame1=Frame(win,highlightbackground="black",highlightthicknes=2,padx=20,pady=20)
frame1.grid(row=0,column=0,padx=50,pady=50)
lab=Label(frame1,text="REGISTRATION",fg="green",font=("times",20,"bold"))
lab.grid(columnspan=2)
lab1=Label(frame1,text="Name",fg="black",font=("times",20,"bold"))
lab1.grid(row=1,column=0)
labentry=Entry(frame1,font=("times",20,"bold"))
labentry.grid(row=1,column=1)

labmail=Label(frame1,text="Email",fg="black",font=("times",20,"bold"))
labmail.grid(row=2,column=0)
labmail=Entry(frame1,font=("times",20,"bold"))
labmail.grid(row=2,column=1)

labadd=Label(frame1,text="Address",fg="black",font=("times",20,"bold"))
labadd.grid(row=3,column=0)
labentry=Entry(frame1,font=("times",20,"bold"))
labentry.grid(row=3,column=1)

subbtn=Button(frame1,text="SUBMIT",bg="green",fg="black",width=5,padx=20,pady=5,font=("times",20,"bold"))
subbtn.grid(row=4,column=1 ,sticky=W)
subclr=Button(frame1,text="CLEAR",bg="red",fg="black",width=5,padx=20,pady=5,font=("times",20,"bold"))
subclr.grid(row=4,column=1,sticky=E)

frame2=Frame(win,highlightbackground="black",highlightthicknes=2,width=100,padx=20,pady=20)
frame2.grid(row=0,column=1,padx=20,pady=50)
lab1=Label(frame2,text="LOGIN",fg="green",font=("times",20,"bold"))
lab1.grid(columnspan=2)


lab1=Label(frame2,text="Name",fg="black",font=("times",20,"bold"))
lab1.grid(row=1,column=0)
labentry=Entry(frame2,font=("times",20,"bold"))
labentry.grid(row=1,column=1)

labmail=Label(frame2,text="Email",fg="black",font=("times",20,"bold"))
labmail.grid(row=2,column=0)
labmail=Entry(frame2,font=("times",20,"bold"))
labmail.grid(row=2,column=1)

subbtn=Button(frame2,text="LOGIN",bg="green",fg="black",width=5,padx=20,pady=5,font=("times",20,"bold"))
subbtn.grid(row=4,column=1 ,sticky=W)
subclr=Button(frame2,text="CLEAR",bg="red",fg="black",width=5,padx=20,pady=5,font=("times",20,"bold"))
subclr.grid(row=4,column=1,sticky=E)

win.mainloop()