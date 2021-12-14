import tkinter

from tkinter import ttk
from tkinter import messagebox,filedialog
from tkinter.ttk import Treeview
import csv
import os
import numpy
import pandas as pd
import openpyxl
import mysql.connector
from tkinter import *
from tkinter import messagebox

class enter(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title("Login")
        self.geometry("1350x1080")
        self.configure(bg="gray36")

        self.frame2 = Frame(self, highlightbackground="gold",bg="black", highlightthicknes=2, width=100, padx=20, pady=20)
        self.frame2.grid(row=1000, column=1000, sticky="N")
        self.frame2.grid_rowconfigure(0, weight=1)
        self.frame2.grid_columnconfigure(0, weight=1)
        self.lab1 = Label(self.frame2, text="LOGIN",bg="black", fg="gold",font=("times", 20, "bold"))
        self.lab1.grid(columnspan=2)

        self.lab1 = Label(self.frame2, text="Name", fg="gold",bg="black", font=("times", 20, "bold"))
        self.lab1.grid(row=1, column=0)
        self.labentry = Entry(self.frame2, font=("times", 20, "bold"),bg="yellow")
        self.labentry.grid(row=1, column=1)

        self.labmail = Label(self.frame2, text="Email", fg="gold",bg="black", font=("times", 20, "bold"))
        self.labmail.grid(row=2, column=0)
        self.labmail = Entry(self.frame2, font=("times", 20, "bold"),bg="yellow")
        self.labmail.grid(row=2, column=1)

        self.subbtn = Button(self.frame2, text="LOGIN", bg="gold", fg="black", width=3, padx=20, pady=5,
                        font=("times", 15, "bold"),command=self.log)
        self.subbtn.grid(row=4, column=1, sticky=W)
        self.subclr = Button(self.frame2, text="CLEAR", bg="gold", fg="black", width=3, padx=20, pady=5,
                        font=("times", 15, "bold"))
        self.subclr.grid(row=4, column=1, sticky=E)

    def log(self):
        if self.labentry.get()=='mani' and self.labmail.get()=='kumar':
            self.destroy()
            home()

        else:messagebox.showinfo("error","Invalid login")

def home():
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
        qry = """update record set name='%s',course='%s',fees=%d where id=%d""" \
              % (ent2.get(), ent3.get(), int(ent4.get()),int(ent1.get()))
        ack = cursor.execute(qry)
        mydb.commit()
        if ack != 0:
            messagebox.showinfo("Info", "Updated")
            clear()
        else:
            messagebox.showinfo("Info", "Not Updated")

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
        mydb.commit()

        if ack != 0:
            messagebox.showinfo("ack", "record added")
            clear()
        else:
            messagebox.showinfo("ack", "record not saved")

    def export():
        if len(mydata) < 1:
            messagebox.showerror("nodata", "no data available to export")
            return False

        fln = filedialog.asksaveasfilename(initialdir=os.getcwd(), title="save CSV",
                                           filetypes=(("xlsx files", "*.xlsx"), ("All FIles", "*.*")))
        with open(fln, mode='w') as myfile:
            expwriter = csv.writer(myfile, delimiter='\t')
            for i in mydata:
                expwriter.writerow(i)
        messagebox.showinfo("data expoted", "your data has been exported to" + os.path.basename(fln) + "succefully.")
    def imp():
       filename=filedialog.askopenfilename(initialdir="C:/Users/Administrator",title="open a file",filetype=(("xlsx files","*.xlsx"),("All FIles","*.*")))
       if filename:
           try:
               filename=r"{}".format(filename)
               df=pd.read_excel(filename)
           except ValueError:
               mylabel.configure(text="file could not be opened... try again")
           except FileNotFoundError:
               mylabel.configure(text="file could not be found... try again")

       table["column"]=list(df.columns)
       table["show"]="headings"
       for column in table["column"]:
           table.heading(column,text="column")
       df_rows=df.to_numpy().tolist()
       clear()
       for row in df_rows:
           table.insert("","end",values=row)
       table.pack()
       update()

    def savedb():
        for i in mydata:
            id=i[0]
            name=i[1]
            course=i[2]
            fees=i[3]
        if messagebox.askyesno("information","are you sure you want to save data to database"):
                qry = """insert into record(id,name,course,fees) values(%d,'%s','%s',%d)"""
                cursor.execute(qry,(id,name,course,fees))
                rows = cursor.fetchall()
                update(rows)
                messagebox.showinfo("data saved","data has been saved in database")

    wrapper1=LabelFrame(root,text="customer list",bg="gray36",fg="gold",font=("times",20,"bold"))
    wrapper2=LabelFrame(root,text="search",bg="gold",fg="black",font=("times",20,"bold"))
    wrapper3=LabelFrame(root,text="customer data",bg="olive",fg="black",font=("times",20,"bold"))

    wrapper1.pack(fill=X,expand=True,padx=20,pady=10)
    wrapper2.pack(fill=X,expand=True,padx=20,pady=10)
    wrapper3.pack(fill=X,expand=True,padx=20,pady=10)

    style=ttk.Style()
    style.configure("Treeview",font=("times",13),rowheight=20,width=12,bg="gray36",fg="white")
    style.configure("Treeview.Heading",font=("times",10,"bold"),width=12,bg="gray36",fg="white")
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
    lbl=Label(wrapper2,text="search",bg="gold",fg="black",font=("times",15,"bold"))
    lbl.pack(side=tkinter.LEFT,padx=10)
    ent=Entry(wrapper2,textvariable=q,width=50)
    ent.pack(side=tkinter.LEFT,padx=6)
    sea=Button(wrapper2,text="search",command=search,bg="yellow",fg="black",font=("times",15,"bold"))
    sea.pack(side=tkinter.LEFT,padx=6)
    clr=Button(wrapper2,text="clear",command=clear,bg="yellow",fg="black",font=("times",15,"bold"))
    clr.pack(side=tkinter.LEFT,padx=8)

    #user data
    lbl1=Label(wrapper3,text="id",bg="olive",fg="black",font=("times",15,"bold"))
    lbl1.grid(row=0,column=0,padx=5,pady=3)
    ent1=Entry(wrapper3,textvariable=t1,width=50,font=("times",13),bg="gray36",fg="white")
    ent1.grid(row=0,column=1,padx=5,pady=3)

    lbl2=Label(wrapper3,text="studentname",bg="olive",fg="black",font=("times",15,"bold"))
    lbl2.grid(row=1,column=0,padx=5,pady=3)
    ent2=Entry(wrapper3,textvariable=t2,width=50,font=("times",13),bg="gray36",fg="white")
    ent2.grid(row=1,column=1,padx=5,pady=3)

    lbl3=Label(wrapper3,text="course",bg="olive",fg="black",font=("times",15,"bold"))
    lbl3.grid(row=2,column=0,padx=5,pady=3)
    ent3=Entry(wrapper3,textvariable=t3,width=50,font=("times",13),bg="gray36",fg="white")
    ent3.grid(row=2,column=1,padx=5,pady=3)

    lbl4=Label(wrapper3,text="fees",bg="olive",fg="black",font=("times",15,"bold"))
    lbl4.grid(row=3,column=0,padx=5,pady=3)
    ent4=Entry(wrapper3,textvariable=t4,width=50,font=("times",13),bg="gray36",fg="white")
    ent4.grid(row=3,column=1,padx=5,pady=3)

    addbtn=Button(wrapper3,text="add",command=add,bg="olive",fg="black",font=("times",15,"bold"))
    upbtn=Button(wrapper3,text="update",command=updatestudent,bg="olive",fg="black",font=("times",15,"bold"))
    deletebtn=Button(wrapper3,text="delete",command=delete,bg="olive",fg="black",font=("times",15,"bold"))
    addbtn.grid(row=4,column=0,padx=5,pady=3)
    upbtn.grid(row=4,column=1,padx=5,pady=3)
    deletebtn.grid(row=4,column=2,padx=5,pady=3)

    expbtn=Button(wrapper1,text="export csv",command=export,bg="yellow",fg="black",font=("times",15,"bold"))
    expbtn.pack(side=tkinter.LEFT,padx=10,pady=10)
    impbtn=Button(wrapper1,text="import csv",command=imp,bg="yellow",fg="black",font=("times",15,"bold"))
    impbtn.pack(side=tkinter.LEFT,padx=10,pady=10)
    savebtn=Button(wrapper1,text="savedata",command=savedb,bg="yellow",fg="black",font=("times",15,"bold"))
    savebtn.pack(side=tkinter.LEFT,padx=10,pady=10)
    expbtn=Button(wrapper1,text="exit",command=lambda :exit(),bg="yellow",fg="black",font=("times",15,"bold"))
    expbtn.pack(side=tkinter.LEFT,padx=10,pady=10)

    mylabel=Label(wrapper1,text="")
    mylabel.pack(pady=20)

    root.title("my application")
    root.geometry("1350x1080")
    root.configure(bg="black")

    root.mainloop()

h=enter()
h=mainloop()

