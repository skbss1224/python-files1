import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox,filedialog
from tkinter.ttk import Treeview
import csv
import os

import mysql.connector

mydb=mysql.connector.connect(host='localhost',password='',user='root',database='school')
cursor=mydb.cursor()

root=Tk()

mydata=[]

q=StringVar()
t1=StringVar()
t2=StringVar()
t3=StringVar()
t4=StringVar()

def update(rows):
    global mydata
    mydata=rows
    table.delete(*table.get_children())
    for i in rows:
        table.insert('',END,values=i)

def search():
    q2=q.get()
    qry="SELECT id,name,course,fees FROM record WHERE name LIKE '%"+q2+"%' OR course LIKE '%"+q2+"%'"
    cursor.execute(qry)
    rows=cursor.fetchall()
    update(rows)

def clear():
    qry = "Select * from record"
    cursor.execute(qry)
    rows=cursor.fetchall()
    update(rows)

def getrow(evet):
    srow = table.focus()
    data = table.item(srow)
    global row
    row = data["values"]
    t1.set(row[0])
    t2.set(row[1])
    t3.set(row[2])
    t4.set(row[3])

def updatestudent():
   pass

def delete():
    id=t1.get()
    qry = "delete from record where id=" + id
    cursor.execute(qry)
    mydb.commit()
    clear()


def add():
    qry = """insert into record(id,name,course,fees) values(%d,'%s','%s',%d)""" % \
          (int(ent1.get()), ent2.get(), ent3.get(), int(ent4.get()))
    ack=cursor.execute(qry)

    if ack != 0:
        messagebox.showinfo("ack", "vehicle added into logs")
        clear()
    else:
        messagebox.showinfo("ack", "vehicle can't added into logs")

def export():
    if len(mydata)<1:
        messagebox.showerror("nodata","no data available to export")

    fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="save CSV",filetypes=(("CSV File","*.csv"),("All Files","*.*")))
    with open(fln,mode='w')as myfile:
        expwriter=csv.writer(myfile,delimiter=',')
        for i in mydata:
            expwriter.writerow(i)
    messagebox.showinfo("data expoted","your data has been exported to"+os.path.basename(fln)+"succefully.")

def imp():
    fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="open csv",filetypes=(("CSV File","*.csv"),("All File")))
    with open(fln)as myfile:
        csvread=csv.reader(myfile,delimeter=",")
        for i in csvread:
            mydata.append(i)
    update(mydata)
def savedb():
    pass

wrapper1=LabelFrame(root,text="customer list")
wrapper2=LabelFrame(root,text="search")
wrapper3=LabelFrame(root,text="customer data")

wrapper1.pack(fill=X,expand=True,padx=20,pady=10)
wrapper2.pack(fill=X,expand=True,padx=20,pady=10)
wrapper3.pack(fill=X,expand=True,padx=20,pady=10)

style=ttk.Style()
style.configure("Treeview",font=("times",13),rowheight=35,width=12)
style.configure("Treeview.Heading",font=("times",10,"bold"),width=12)
table=ttk.Treeview(wrapper1,columns=(0,1,2,3))

table.heading(0,text="id")
table.heading(1,text="name")
table.heading(2,text="course")
table.heading(3,text="fees")
table.bind('<Double-1>',getrow)

table["show"]="headings"
table.pack(fill=X)

qry = "Select * from record"
cursor.execute(qry)
rows=cursor.fetchall()
update(rows)

# search
lbl=Label(wrapper2,text="search")
lbl.pack(side=tkinter.LEFT,padx=10)
ent=Entry(wrapper2,textvariable=q)
ent.pack(side=tkinter.LEFT,padx=6)
sea=Button(wrapper2,text="search",command=search)
sea.pack(side=tkinter.LEFT,padx=6)
clr=Button(wrapper2,text="clear",command=clear)
clr.pack(side=tkinter.LEFT,padx=8)

#user data
lbl1=Label(wrapper3,text="id")
lbl1.grid(row=0,column=0,padx=5,pady=3)
ent1=Entry(wrapper3,textvariable=t1)
ent1.grid(row=0,column=1,padx=5,pady=3)

lbl2=Label(wrapper3,text="studentname")
lbl2.grid(row=1,column=0,padx=5,pady=3)
ent2=Entry(wrapper3,textvariable=t2)
ent2.grid(row=1,column=1,padx=5,pady=3)

lbl3=Label(wrapper3,text="course")
lbl3.grid(row=2,column=0,padx=5,pady=3)
ent3=Entry(wrapper3,textvariable=t3)
ent3.grid(row=2,column=1,padx=5,pady=3)

lbl4=Label(wrapper3,text="fees")
lbl4.grid(row=3,column=0,padx=5,pady=3)
ent4=Entry(wrapper3,textvariable=t4)
ent4.grid(row=3,column=1,padx=5,pady=3)

addbtn=Button(wrapper3,text="add",command=add)
upbtn=Button(wrapper3,text="update",command=updatestudent)
deletebtn=Button(wrapper3,text="delete",command=delete)
addbtn.grid(row=4,column=0,padx=5,pady=3)
upbtn.grid(row=4,column=1,padx=5,pady=3)
deletebtn.grid(row=4,column=2,padx=5,pady=3)

expbtn=Button(wrapper1,text="export csv",command=export)
expbtn.pack(side=tkinter.LEFT,padx=10,pady=10)
impbtn=Button(wrapper1,text="import csv",command=imp)
impbtn.pack(side=tkinter.LEFT,padx=10,pady=10)
savebtn=Button(wrapper1,text="savedata",command=savedb)
savebtn.pack(side=tkinter.LEFT,padx=10,pady=10)
expbtn=Button(wrapper1,text="export",command=lambda :exit())
expbtn.pack(side=tkinter.LEFT,padx=10,pady=10)



root.title("my application")
root.geometry("800x700")
root.mainloop()

