from tkinter import *
from tkinter import ttk
from tkinter import messagebox

import pymysql
import tkinter

con = pymysql.connect(host='localhost', database='', user='root', passwd='')
cur = con.cursor()

win=Tk()
win.geometry("2000x2000")
win.title("tree view")
global sno
sno=1

def addrecord():
    if(txtname.get()!="" and txtadd.get()!="" and txtcon.get()!="" and txtmail.get()!=""):
        global sno
        mytree.insert("",index="end",iid=sno,values=(sno,txtname.get()  ,txtadd.get(),txtcon.get(),txtmail.get()))
        txtname.delete(0,END)
        txtadd.delete(0, END)
        txtcon.delete(0, END)
        txtmail.delete(0, END)
        sno+=1


    else:
        messagebox.showinfo("message","please fill all fields")

def SelectRecord():
    txtname.delete(0, END)
    txtadd.delete(0, END)
    txtcon.delete(0, END)
    txtmail.delete(0, END)
    selected=mytree.focus()
    values=mytree.item(selected,'values')

    txtname.insert(0,values[1])
    txtadd.insert(0,values[2])
    txtcon.insert(0,values[3])
    txtmail.insert(0,values[4])


def updateRecord():
    if (txtname.get() != "" and txtadd.get() != "" and txtcon.get() != "" and txtmail.get() != ""):
        no=mytree.focus()[0]
        selected=mytree.focus()
        mytree.item(selected,values=(no, txtname.get(), txtadd.get(), txtcon.get(), txtmail.get()))
        txtname.delete(0, END)
        txtadd.delete(0, END)
        txtcon.delete(0, END)
        txtmail.delete(0, END)


    else:
        messagebox.showinfo("message", "no fields in entry box fields")


def delete():
    record=mytree.selection()[0]
    mytree.delete(record)

    txtname.delete(0, END)
    txtadd.delete(0, END)
    txtcon.delete(0, END)
    txtmail.delete(0, END)

def deletemany():
    record=mytree.selection()
    for data in record:
        mytree.delete(data)

def deleteall():
    for record in mytree.get_children():
        mytree.delete(record)
myframe=Frame(win)
myframe.pack()

lblname=Label(myframe,text="Name",font=("times",15,"bold"),pady=15)
lblname.grid(row=1,column=0,sticky=E)

txtname=Entry(myframe,font=("times",15,"bold"))
txtname.grid(row=1,column=1)

lbladd=Label(myframe,text="address",font=("times",15,"bold"),pady=15)
lbladd.grid(row=2,column=0,sticky=E)

txtadd=Entry(myframe,font=("times",15,"bold"))
txtadd.grid(row=2,column=1)

lblcon=Label(myframe,text="contact",font=("times",15,"bold"),pady=15)
lblcon.grid(row=3,column=0,sticky=E)

txtcon=Entry(myframe,font=("times",15,"bold"))
txtcon.grid(row=3,column=1)

lblmail=Label(myframe,text="mail",font=("times",15,"bold"),pady=15)
lblmail.grid(row=4,column=0,sticky=E)

txtmail=Entry(myframe,font=("times",15,"bold"))
txtmail.grid(row=4,column=1)

btnframe=Frame(win)
btnframe.pack()

btnadd=Button(btnframe,text="Add record",bg="#1289A7",fg="white",padx=5,pady=5,font=("times",12,"bold"),command=addrecord)
btnadd.grid(row=1,column=0,padx=5,pady=10)

btnsel=Button(btnframe,text="Select record",bg="#10ac84",fg="white",padx=5,pady=5,font=("times",12,"bold"),command=SelectRecord)
btnsel.grid(row=1,column=1,padx=5,pady=10)

btnupd=Button(btnframe,text="Update record",bg="blue",fg="white",padx=5,pady=5,font=("times",12,"bold"),command=updateRecord)
btnupd.grid(row=1,column=2,padx=5,pady=10)

btndel=Button(btnframe,text="Delete",bg="red",fg="white",padx=5,pady=5,font=("times",12,"bold"),command=delete)
btndel.grid(row=1,column=3,padx=5,pady=10)

btndelmany=Button(btnframe,text="Delete many",bg="orange",fg="white",padx=5,pady=5,font=("times",12,"bold"),command=deletemany)
btndelmany.grid(row=1,column=4,padx=5,pady=10)

btndelall=Button(btnframe,text="Delete all",bg="pink",fg="white",padx=5,pady=5,font=("times",12,"bold"),command=deleteall)
btndelall.grid(row=1,column=5,padx=5,pady=10)

mytree=ttk.Treeview(win)
mytree['columns']=('s.no','name','address','contact','mail')

mytree.column("#0",width=0,stretch=NO)
mytree.column("#1",width=250)
mytree.column("#2",width=250)
mytree.column("#3",width=250)
mytree.column("#4",width=250)

mytree.heading("#0",text="")
mytree.heading("#1",text="s.no")
mytree.heading("#2",text="name")
mytree.heading("#3",text="address")
mytree.heading("#4",text="contact")
mytree.heading("#5",text="mail")

data=[
    ["sasi","salem","987655677","sasi@gmail.com"],
    ["kumar","namakkal","987677877","kumar@gmail.com"],
    ["abbash","erode","987659778","abbash@gmail.com"],
    ["vino","chennai","7877785677","vino@gmail.com"],
    ["kavin","cbe","36465677","kavin@gmail.com"]
]

for datas in data:
    mytree.insert("",index="end",iid=sno,values=(sno,datas[0],datas[1],datas[2],datas[3]))
    sno+=1
def mybind(event):
    SelectRecord()

mytree.bind("<ButtonRelease-1>",mybind)

mytree.pack()
win.mainloop()