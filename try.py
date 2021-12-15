from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk
from tkinter import messagebox
import pymysql
import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox, filedialog
from tkinter.ttk import Treeview
import csv
import os
import numpy
import pandas as pd
import openpyxl
import mysql.connector
class register():
    def __init__(self,win):
        self.win=win
        self.win.title("login")
        self.win.configure(bg="gray36")
        self.win.geometry("1350x700")

        self.bg=ImageTk.PhotoImage(file="C:/Users/Administrator/PycharmProjects/pythonProject1/tkinder/image/h.jpg")
        bg=Label(self.win,image=self.bg).place(x=300,y=0,relwidth=1,relheight=1)

        frame1=Frame(self.win,bg="white")
        frame1.place(x=480,y=100,width=700,height=500)
        title=Label(frame1,text="REGISTER HERE",font=("times",20,"bold"),bg="white",fg="green").place(x=50,y=30)

        f_name=Label(frame1,text="first name",font=("times",15,"bold"),bg="white",fg="gray").place(x=50,y=100)
        self.txt_fname=Entry(frame1,font=("times",15),bg="lightgray")
        self.txt_fname.place(x=50,y=130,width=250)

        l_name = Label(frame1, text="last name", font=("times", 15, "bold"), bg="white", fg="gray").place(x=370, y=100)
        self.txt_lname = Entry(frame1, font=("times", 15), bg="lightgray")
        self.txt_lname.place(x=370, y=130, width=250)
        contact = Label(frame1, text="contact", font=("times", 15, "bold"), bg="white", fg="gray").place(x=50, y=170)

        self.txt_contact = Entry(frame1, font=("times", 15), bg="lightgray")
        self.txt_contact.place(x=50, y=200, width=250)

        mail = Label(frame1, text="mail", font=("times", 15, "bold"), bg="white", fg="gray").place(x=370, y=170)

        self.txt_mail = Entry(frame1, font=("times", 15), bg="lightgray")
        self.txt_mail.place(x=370, y=200, width=250)
        question = Label(frame1, text="security question", font=("times", 15, "bold"), bg="white", fg="gray").place(x=50, y=240)
        self.cmdquestion = ttk.Combobox(frame1, font=("times", 15),state="read only",justify=CENTER)
        self.cmdquestion["values"]=("select","your first pet name","your birth place","your best friend name")
        self.cmdquestion.place(x=50, y=270, width=250)
        self.cmdquestion.current(0)
        answer = Label(frame1, text="answer", font=("times", 15, "bold"), bg="white", fg="gray").place(x=370, y=240)
        self.txt_answer = Entry(frame1, font=("times", 15), bg="lightgray")
        self.txt_answer.place(x=370, y=270, width=250)

        password = Label(frame1, text="password", font=("times", 15, "bold"), bg="white", fg="gray").place(x=50, y=310)

        self.txt_password = Entry(frame1, font=("times", 15), bg="lightgray")
        self.txt_password.place(x=50, y=340, width=250)
        conpassword = Label(frame1, text="confirm password", font=("times", 15, "bold"), bg="white", fg="gray").place(x=370, y=310)
        self.txt_conpassword = Entry(frame1, font=("times", 15), bg="lightgray")
        self.txt_conpassword.place(x=370, y=340, width=250)
        self.var_chk=IntVar()
        chk=Checkbutton(frame1,text="I agree The Terms & conditions",onvalue=1,offvalue=0,bg="white",font=("times",12),variable=self.var_chk).place(x=50,y=370)

        reg=Button(frame1,text="REGISTER NOW",bg="green",fg="white",width=25,font=("times",15),command=self.register_data).place(x=50,y=420)
        signin = Button(self.win, text="Sign In", bg="gold", fg="black", width=20,font=("times",20),command=self.signin).place(x=100, y=400)

    def clear(self):
        self.txt_fname.delete(0,END)
        self.txt_lname.delete(0, END)
        self.txt_contact.delete(0, END)
        self.txt_mail.delete(0, END)
        self.cmdquestion.current(0)
        self.txt_answer.delete(0, END)
        self.txt_password.delete(0, END)
        self.txt_conpassword.delete(0, END)
    def register_data(self):
        if(self.txt_fname.get()==""or self.txt_lname.get()==""or self.txt_contact.get()==""or self.txt_mail.get()==""or self.cmdquestion.get()==""or self.txt_answer.get()==""or self.txt_password.get()==""or self.txt_conpassword.get()==""):
            messagebox.showerror("error","All fields are required",parent=self.win)

        elif self.txt_password.get()!=self.txt_conpassword.get():
            messagebox.showerror("error","password & confirm password should be same",parent=self.win)

        elif self.var_chk.get()==0:
            messagebox.showerror("error","please agree our terms & condition",parent=self.win)

        else:
            try:
                con=pymysql.connect(host='localhost',password='',user='root',database='employee')
                cur=con.cursor()
                cur.execute("select * from record where email=%s",self.txt_mail.get())
                row=cur.fetchone()
                print(row)
                if row !=None:
                    messagebox.showerror("error","this email already used please use another email",parent=self.win)
                else:
                    cur.execute("insert into record(f_name,l_name,contact,email,question,answer,password) values(%s,%s,%s,%s,%s,%s,%s)",
                                (self.txt_fname.get(),
                                 self.txt_lname.get(),
                                 self.txt_contact.get(),
                                 self.txt_mail.get(),
                                 self.cmdquestion.get(),
                                 self.txt_answer.get(),
                                 self.txt_password.get(),
                                ))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Error", "register successfully", parent=self.win)


            except Exception as es:
                  messagebox.showerror("Error",f"Error due to:{str(es)}",parent=self.win)
    def signin(self):
        self.win.destroy()
        win1=Tk()
        win1.configure(bg="gray36")
        win1.title("login")
        win1.geometry("1350x700")

        def login():
            if txtuser.get() == "" or txt_password1.get() == "":
                messagebox.showerror("Error", "Enter User Name And Password", parent=win1)
            else:
                try:
                    con = pymysql.connect(host='localhost', password='', user='root', database='employee')
                    cur = con.cursor()

                    cur.execute("select * from record where email=%s and password = %s",
                                (txtuser.get(), txt_password1.get()))
                    row = cur.fetchone()

                    if row == None:
                        messagebox.showerror("Error", "Invalid User Name And Password", parent=win1)

                    else:
                        messagebox.showinfo("Success", "Successfully Login", parent=win1)
                        win1.destroy()
                        self.main()
                    con.close()
                except Exception as es:
                    messagebox.showerror("Error", f"Error Dui to : {str(es)}", parent=win1)

        def clear():
            txtuser.delete(0, END)
            txt_password1.delete(0, END)

        bg1 = ImageTk.PhotoImage(file="C:/Users/Administrator/PycharmProjects/pythonProject1/tkinder/image/blur1.jpg")
        bg1 = Label(win1, image=bg1).place(x=300, y=0, relwidth=1, relheight=1)

        frame2 = Frame(win1, bg="white")
        frame2.place(x=480, y=100, width=700, height=500)
        title = Label(frame2, text="LOGIN HERE", font=("times", 20, "bold"), bg="white", fg="green").place(x=50,y=30)

        user = Label(frame2, text="User name", font=("times", 15, "bold"), bg="white", fg="gray").place(x=50, y=100)
        txtuser = Entry(frame2, font=("times", 15), bg="lightgray")
        txtuser.place(x=50, y=130, width=250)

        password = Label(frame2, text="password", font=("times", 15, "bold"), bg="white", fg="gray").place(x=370, y=100)
        txt_password1 = Entry(frame2, font=("times", 15), bg="lightgray")
        txt_password1.place(x=370, y=130, width=250)
        login=Button(frame2,text="login",bg="Blue",fg="white",width=15,font=("times",15),command=login).place(x=55,y=200)
        clr=Button(frame2,text="clear",bg="red",fg="white",width=15,font=("times",15),command=clear).place(x=380,y=200)

        win1.mainloop()







    def main(self):
        mydb = mysql.connector.connect(host='localhost', password='', user='root', database='school')
        cursor = mydb.cursor()

        root = Tk()

        mydata = []

        q = StringVar()
        t1 = StringVar()
        t2 = StringVar()
        t3 = StringVar()
        t4 = StringVar()

        def update(rows):
            global mydata
            mydata = rows
            table.delete(*table.get_children())
            for i in rows:
                table.insert('', END, values=i)

        def search():
            q2 = q.get()
            qry = "SELECT id,name,course,fees FROM record WHERE name LIKE '%" + q2 + "%' OR course LIKE '%" + q2 + "%'"
            cursor.execute(qry)
            rows = cursor.fetchall()
            update(rows)

        def clear():
            qry = "Select * from record"
            cursor.execute(qry)
            rows = cursor.fetchall()
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
                  % (ent2.get(), ent3.get(), int(ent4.get()), int(ent1.get()))
            ack = cursor.execute(qry)
            mydb.commit()
            if ack != 0:
                messagebox.showinfo("Info", "Updated")
                clear()
            else:
                messagebox.showinfo("Info", "Not Updated")

        def delete():
            id = t1.get()
            qry = "delete from record where id=" + id
            cursor.execute(qry)
            mydb.commit()
            clear()

        def add():
            qry = """insert into record(id,name,course,fees) values(%d,'%s','%s',%d)""" % \
                  (int(ent1.get()), ent2.get(), ent3.get(), int(ent4.get()))
            ack = cursor.execute(qry)
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
            messagebox.showinfo("data expoted",
                                "your data has been exported to" + os.path.basename(fln) + "succefully.")

        def imp():
            filename = filedialog.askopenfilename(initialdir="C:/Users/Administrator", title="open a file",
                                                  filetype=(("xlsx files", "*.xlsx"), ("All FIles", "*.*")))
            if filename:
                try:
                    filename = r"{}".format(filename)
                    df = pd.read_excel(filename)
                except ValueError:
                    mylabel.configure(text="file could not be opened... try again")
                except FileNotFoundError:
                    mylabel.configure(text="file could not be found... try again")
                clear()
            table["column"] = list(df.columns)
            table["show"] = "headings"
            for column in table["column"]:
                table.heading(column, text="column")
            df_rows = df.to_numpy().tolist()

            for row in df_rows:
                table.insert("", "end", values=row)
            table.pack()
            update()

        def savedb():
            for i in mydata:
                id = i[0]
                name = i[1]
                course = i[2]
                fees = i[3]
            if messagebox.askyesno("information", "are you sure you want to save data to database"):
                qry = """insert into record(id,name,course,fees) values(%d,'%s','%s',%d)"""
                cursor.execute(qry, (id, name, course, fees))
                rows = cursor.fetchall()
                update(rows)
                messagebox.showinfo("data saved", "data has been saved in database")

        wrapper1 = LabelFrame(root, text="customer list", bg="gray36", fg="gold", font=("times", 20, "bold"))
        wrapper2 = LabelFrame(root, text="search", bg="gold", fg="black", font=("times", 20, "bold"))
        wrapper3 = LabelFrame(root, text="customer data", bg="olive", fg="black", font=("times", 20, "bold"))

        wrapper1.pack(fill=X, expand=True, padx=20, pady=10)
        wrapper2.pack(fill=X, expand=True, padx=20, pady=10)
        wrapper3.pack(fill=X, expand=True, padx=20, pady=10)

        style = ttk.Style()
        style.configure("Treeview", font=("times", 13), rowheight=20, width=12, bg="gray36", fg="white")
        style.configure("Treeview.Heading", font=("times", 10, "bold"), width=12, bg="gray36", fg="white")
        table = ttk.Treeview(wrapper1, columns=(0, 1, 2, 3))

        table.heading(0, text="id")
        table.heading(1, text="name")
        table.heading(2, text="course")
        table.heading(3, text="fees")
        table.bind('<Double-1>', getrow)

        table["show"] = "headings"
        table.pack(fill=X)

        qry = "Select * from record"
        cursor.execute(qry)
        rows = cursor.fetchall()
        update(rows)

        # search
        lbl = Label(wrapper2, text="search", bg="gold", fg="black", font=("times", 15, "bold"))
        lbl.pack(side=tkinter.LEFT, padx=10)
        ent = Entry(wrapper2, textvariable=q, width=50)
        ent.pack(side=tkinter.LEFT, padx=6)
        sea = Button(wrapper2, text="search", command=search, bg="yellow", fg="black", font=("times", 15, "bold"))
        sea.pack(side=tkinter.LEFT, padx=6)
        clr = Button(wrapper2, text="clear", command=clear, bg="yellow", fg="black", font=("times", 15, "bold"))
        clr.pack(side=tkinter.LEFT, padx=8)

        # user data
        lbl1 = Label(wrapper3, text="id", bg="olive", fg="black", font=("times", 15, "bold"))
        lbl1.grid(row=0, column=0, padx=5, pady=3)
        ent1 = Entry(wrapper3, textvariable=t1, width=50, font=("times", 13), bg="gray36", fg="white")
        ent1.grid(row=0, column=1, padx=5, pady=3)

        lbl2 = Label(wrapper3, text="studentname", bg="olive", fg="black", font=("times", 15, "bold"))
        lbl2.grid(row=1, column=0, padx=5, pady=3)
        ent2 = Entry(wrapper3, textvariable=t2, width=50, font=("times", 13), bg="gray36", fg="white")
        ent2.grid(row=1, column=1, padx=5, pady=3)

        lbl3 = Label(wrapper3, text="course", bg="olive", fg="black", font=("times", 15, "bold"))
        lbl3.grid(row=2, column=0, padx=5, pady=3)
        ent3 = Entry(wrapper3, textvariable=t3, width=50, font=("times", 13), bg="gray36", fg="white")
        ent3.grid(row=2, column=1, padx=5, pady=3)

        lbl4 = Label(wrapper3, text="fees", bg="olive", fg="black", font=("times", 15, "bold"))
        lbl4.grid(row=3, column=0, padx=5, pady=3)
        ent4 = Entry(wrapper3, textvariable=t4, width=50, font=("times", 13), bg="gray36", fg="white")
        ent4.grid(row=3, column=1, padx=5, pady=3)

        addbtn = Button(wrapper3, text="add", command=add, bg="olive", fg="black", font=("times", 15, "bold"))
        upbtn = Button(wrapper3, text="update", command=updatestudent, bg="olive", fg="black",
                       font=("times", 15, "bold"))
        deletebtn = Button(wrapper3, text="delete", command=delete, bg="olive", fg="black", font=("times", 15, "bold"))
        addbtn.grid(row=4, column=0, padx=5, pady=3)
        upbtn.grid(row=4, column=1, padx=5, pady=3)
        deletebtn.grid(row=4, column=2, padx=5, pady=3)

        expbtn = Button(wrapper1, text="export csv", command=export, bg="yellow", fg="black",
                        font=("times", 15, "bold"))
        expbtn.pack(side=tkinter.LEFT, padx=10, pady=10)
        impbtn = Button(wrapper1, text="import csv", command=imp, bg="yellow", fg="black", font=("times", 15, "bold"))
        impbtn.pack(side=tkinter.LEFT, padx=10, pady=10)
        savebtn = Button(wrapper1, text="savedata", command=savedb, bg="yellow", fg="black", font=("times", 15, "bold"))
        savebtn.pack(side=tkinter.LEFT, padx=10, pady=10)
        expbtn = Button(wrapper1, text="exit", command=lambda: exit(), bg="yellow", fg="black",
                        font=("times", 15, "bold"))
        expbtn.pack(side=tkinter.LEFT, padx=10, pady=10)

        mylabel = Label(wrapper1, text="")
        mylabel.pack(pady=20)

        root.title("my application")
        root.geometry("1350x1080")
        root.configure(bg="black")

        root.mainloop()

win = Tk()
obj = register(win)
win.mainloop()

