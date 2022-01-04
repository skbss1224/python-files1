from tkinter import messagebox
from tkinter.font import BOLD, ITALIC
from tkinter.ttk import Treeview

from pymysql import *
from tkinter import *

con = connect(host='localhost', database='kabilan', user='root', passwd='')
cur = con.cursor()

class Home(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title("JOBS")
        self.geometry('700x700')
        icon=PhotoImage(file="C:\\Users\\SRDB\\PycharmProjects\\KabilanPython\\gui\\photos.ico")
        self.iconphoto(False,icon)
        f=('Arial',15,ITALIC)
        self.head = Label(self, text='Garriage Service Log', font=('Arial', 20, BOLD))
        self.head.grid(row=0, column=50)
        self.nlab = Label(self, text='Job Number', font=f)
        self.nlab.grid(row=1, column=4)
        self.n = Entry(self, borderwidth='8')
        self.n.grid(row=1, column=40)
        self.alab = Label(self, text='Vehicle Registration number', font=f)
        self.alab.grid(row=2, column=4)
        self.a = Entry(self,borderwidth='8')
        self.a.grid(row=2, column=40)
        self.blab = Label(self, text='Vehicle Log date(YYYY-MM-DD)', font=f)
        self.blab.grid(row=3, column=4)
        self.b = Entry(self,borderwidth='8')
        self.b.grid(row=3, column=40)
        self.clab = Label(self, text='Vehicle Owner name', font=f)
        self.clab.grid(row=4, column=4)
        self.c = Entry(self,borderwidth='8')
        self.c.grid(row=4, column=40)
        self.dlab = Label(self, text='Vehicle Owner contact', font=f)
        self.dlab.grid(row=5, column=4)
        self.d = Entry(self,borderwidth='8')
        self.d.grid(row=5, column=40)
        self.elab = Label(self, text='Vehicle Issues', font=f)
        self.elab.grid(row=6, column=4)
        self.e = Entry(self,borderwidth='8')
        self.e.grid(row=6, column=40)
        self.flab = Label(self, text='Vehicle Delivery expected in Days', font=f)
        self.flab.grid(row=7, column=4)
        self.f = Entry(self,borderwidth='8')
        self.f.grid(row=7, column=40)
        self.glab = Label(self, text='Vehicle Service Budget', font=f)
        self.glab.grid(row=8, column=4)
        self.g = Entry(self,borderwidth='8')
        self.g.grid(row=8, column=40)
        self.bu = Button(self, text='Add to Log', command=self.ins, borderwidth='10', fg='blue',bg='pink')
        self.bu.grid(row=9, column=0)
        self.view = Button(self, text="ViewAll", command=self.vw, borderwidth='10', fg='blue', bg='pink')
        self.view.grid(row=9, column=1)
        self.vone=Button(self,text='View One',command=self.one,borderwidth='10',fg='blue',bg='pink')
        self.vone.grid(row=9,column=2)
        self.edit=Button(self,text='Update',command=self.update,borderwidth='10',bg='pink',fg='blue')
        self.edit.grid(row=9,column=3)
        self.delete=Button(self,text='Delete',command=self.erase,borderwidth='10',fg='blue',bg='pink')
        self.delete.grid(row=9,column=4)
        self.bu = Button(self, text='Clear', command=self.clear,borderwidth='10', fg='blue',bg='pink')
        self.bu.grid(row=9, column=5)

    def erase(self):
        con.autocommit(True)
        qry="delete from jobs where number="+self.n.get()
        ack=cur.execute(qry)
        if ack!=0:
            messagebox.showinfo("Info","Deleted ")
            self.clear()
        else:
            messagebox.showinfo("Info","Not Deleted")

    def update(self):
        con.autocommit(True)
        qry="""update jobs set regnum='%s',pick_date='%s',cust_name='%s',cust_contact=%d,issues='%s',expected=%d,exp_bill=%f where number=%d"""\
            %(self.a.get(),self.b.get(),self.c.get(),int(self.d.get()),self.e.get(),int(self.f.get()),float(self.g.get()),int(self.n.get()))
        ack=cur.execute(qry)
        if ack!=0:
            messagebox.showinfo("Info","Updated")
            self.clear()
        else:messagebox.showinfo("Info","Not Updated")

    def one(self):
        job=self.n.get()
        qry="select * from jobs where number="+job
        cur.execute(qry)
        single=cur.fetchone()
        self.clear()
        self.a.insert(0,single[1])
        self.b.insert(0, single[2])
        self.c.insert(0, single[3])
        self.d.insert(0, single[4])
        self.e.insert(0, single[5])
        self.f.insert(0, single[6])
        self.g.insert(0, single[7])

    def vw(self):
        class Vw(Frame):
            def __init__(self, parent):
                Frame.__init__(self, parent)
                self.CreateUI()
                self.LoadTable()
                self.grid(sticky=(N, S, W, E))
                parent.grid_rowconfigure(0, weight=1)
                parent.grid_columnconfigure(0, weight=1)

            def CreateUI(self):
                tv = Treeview(self)
                tv['columns'] = ('Job Number', 'Registration number', 'Picked Date','Customer Name', 'Contact', 'Issues', 'Expected Day','Expected Bill')
                tv.heading('#0', text='Job Number', anchor='center')
                tv.column('#0', anchor='center')
                tv.heading('#1', text='Registration number', anchor='center')
                tv.column('#1', anchor='center')
                tv.heading('#2', text='Picked Date', anchor='center')
                tv.column('#2', anchor='center')
                tv.heading('#3', text='Customer Name', anchor='center')
                tv.column('#3', anchor='center')
                tv.heading('#4', text='Contact', anchor='center')
                tv.column('#4', anchor='center')
                tv.heading('#5', text='Issues', anchor='center')
                tv.column('#5', anchor='center')
                tv.heading('#6', text='Expected Day', anchor='center')
                tv.column('#6', anchor='center')
                tv.heading('#7', text='Expected Bill', anchor='center')
                tv.column('#7', anchor='center')
                tv.grid(sticky=(N, S, W, E))
                self.treeview = tv
                self.grid_rowconfigure(0, weight=1)
                self.grid_columnconfigure(0, weight=1)

            def LoadTable(self):
                Select = "Select * from jobs"
                cur.execute(Select)
                result = cur.fetchall()
                for i in result:
                    self.treeview.insert("", 'end',text=i[0],
                                values=(i[1],i[2],i[3],i[4],i[5],i[6],i[7]))

        root = Tk()
        root.title("Every One's Data")
        root.geometry('1024x700')
        Vw(root)

    def ins(self):
        #con = connect(host='localhost', database='kabilan', user='root', passwd='')
        qry = """insert into jobs(regnum,pick_date,cust_name,cust_contact,issues,expected,exp_bill) values('%s','%s','%s',%d,'%s',%d,%f)""" % \
              (self.a.get(), self.b.get(), self.c.get(), int(self.d.get()), self.e.get(), int(self.f.get()),
               float(self.g.get()))
        #cur = con.cursor()
        ack = cur.execute(qry)
        con.autocommit(True)
        if ack != 0:
            messagebox.showinfo("ack", "vehicle added into logs")
            self.clear()
        else:
            messagebox.showinfo("ack", "vehicle can't added into logs")

    def clear(self):
        self.a.delete(0, 'end')
        self.b.delete(0, 'end')
        self.c.delete(0, 'end')
        self.d.delete(0, 'end')
        self.e.delete(0, 'end')
        self.f.delete(0, 'end')
        self.g.delete(0, 'end')

h=Home()
h.mainloop())