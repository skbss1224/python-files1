import tkinter as tk
from tkinter import ttk,messagebox,filedialog

import mysql as mysql
import mysql.connector
from tkinter import *
import win32api

def GetValue(event):
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    row_id= listbox.selection()[0]
    select= listbox.set(row_id)
    e1.insert(0,select['id'])
    e2.insert(0,select['stname'])
    e3.insert(0,select['course'])
    e4.insert(0,select['fee'])


root=Tk()
root.geometry("800x500")
global e1
global e2
global e3
global e4
tk.Label(root,text="student registration",fg="blue",font=("times",20,"bold")).place(x=400,y=5)
tk.Label(root,text="student id").place(x=10,y=10)
Label(root,text="name").place(x=10,y=40)
Label(root,text="course").place(x=10,y=70)
Label(root,text="fees").place(x=10,y=100)

e1=Entry(root)
e1.place(x=140,y=10)

e2=Entry(root)
e2.place(x=140,y=40)

e3=Entry(root)
e3.place(x=140,y=70)

e4=Entry(root)
e4.place(x=140,y=100)

def add():
    studid=e1.get()
    studname=e2.get()
    coursename=e3.get()
    feee=e4.get()
    mysqldb = mysql.connector.connect(host='localhost', database='smsschool', user='root', passwd='')
    mycursor = mysqldb.cursor()
    try:
        sql="INSERT INTO record(id,stname,course,fee)VALUES(%s,%s,%s,%s)"
        val=(studid,studname,coursename,feee)
        mycursor.execute(sql,val)
        mysqldb.commit()
        lastid=mycursor.lastrowid
        messagebox.showinfo("info","record insert")
        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        e4.delete(0, END)
        e1.focus_set()
    except Exception as e:
        print(e)
        mysqldb.rollback()
        mysqldb.close()




def update():
    studid=e1.get()
    studname=e2.get()
    coursename=e3.get()
    feee=e4.get()
    mysqldb = mysql.connector.connect(host='localhost', database='smsschool', user='root', passwd='')
    mycursor = mysqldb.cursor()
    try:
        sql="update record set stname=%s,course=%s,fee=%s where id=%s"
        val=(studname,coursename,feee,studid)
        mycursor.execute(sql,val)
        mysqldb.commit()
        lastid=mycursor.lastrowid
        messagebox.showinfo("info","record updated successfully")
        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        e4.delete(0, END)
        e1.focus_set()

    except Exception as e:
        print(e)
        mysqldb.rollback()
        mysqldb.close()

def delete():
    studid = e1.get()
    mysqldb = mysql.connector.connect(host="localhost", user="root", password="", database="smsschool")
    mycursor = mysqldb.cursor()

    try:
        sql="delete from record where id = %s"
        val=(studid,)
        mycursor.execute(sql, val)
        mysqldb.commit()
        lastid=mycursor.lastrowid
        messagebox.showinfo("info","record deleted successfully")
        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        e4.delete(0, END)
        e1.focus_set()

    except Exception as e:
        print(e)
        mysqldb.rollback()
        mysqldb.close()



def show():
    mysqldb=mysql.connector.connect(host="localhost",user="root",password="",database="smsschool")
    mycursor=mysqldb.cursor()
    mycursor.execute("SELECT id,stname,course,fee FROM record")
    records=mycursor.fetchall()
    print(records)

    for i,(id,stname,course,fee) in enumerate(records,start=1):
        listbox.insert("","end",values=(id,stname,course,fee))
        mysqldb.close()



Button(root,text="add",command=add,height=3,width=13).place(x=30,y=130)
Button(root,text="update",command=update,height=3,width=13).place(x=140,y=130)
Button(root,text="delete",command=delete,height=3,width=13).place(x=250,y=130)


cols=('id','stname','course','fee')
listbox=ttk.Treeview(root,columns=cols,show='headings')



for col in cols:
    listbox.heading(col,text=col)
    listbox.grid(row=1,column=0,columnspan=2)
    listbox.place(x=10,y=200)
show()
listbox.bind('<Double-Button-1>',GetValue)
root.mainloop()