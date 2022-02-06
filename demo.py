import tkinter
from tkinter.font import BOLD
from pymysql import *
from tkinter import END, messagebox
from tkinter.ttk import Treeview

con = connect(host='localhost',database='aarthi',user='root',password='')
cur=con.cursor()

class Home(tkinter.Tk):
    def __init__(self):
        tkinter.Tk.__init__(self)
        self.title("company")
        self.geometry("1080x700")
        self.company_name=tkinter.Label(self,text="company",font=("times",20,BOLD))
        self.company_name.grid(row=0,column=50)
        self.number=tkinter.Label(self,text="company_org",font=("times",20,BOLD))
        self.number.grid(row=1,column=50)
        self.number_txt=tkinter.Entry(self,font=("times",15,BOLD))
        self.number_txt.grid(row=1,column=100)
        self.company_org=tkinter.Label(self,text="company_org",font=("times",20,BOLD))
        self.company_org.grid(row=2,column=50)
        self.company_org_txt=tkinter.Entry(self,font=("times",15,BOLD))
        self.company_org_txt.grid(row=2,column=100)
        self.company_nature=tkinter.Label(self,text="company_nature",font=("times",20,BOLD))
        self.company_nature.grid(row=3,column=50)
        self.company_nature_txt=tkinter.Entry(self,font=("times",15,BOLD))
        self.company_nature_txt.grid(row=3,column=100)
        self.company_opennings=tkinter.Label(self,text="company_opennings",font=("times",20,BOLD))
        self.company_opennings.grid(row=4,column=50)
        self.company_opennings_txt=tkinter.Entry(self,font=("times",15,BOLD))
        self.company_opennings_txt.grid(row=4,column=100)
        self.company_place=tkinter.Label(self,text="company_place",font=("times",20,BOLD))
        self.company_place.grid(row=5,column=50)
        self.company_place_txt=tkinter.Entry(self,font=("times",15,BOLD))
        self.company_place_txt.grid(row=5,column=100)
        self.company_salary=tkinter.Label(self,text="company_salary",font=("times",20,BOLD))
        self.company_salary.grid(row=6,column=50)
        self.company_salary_txt=tkinter.Entry(self,font=("times",15,BOLD))
        self.company_salary_txt.grid(row=6,column=100)
        self.company_ratting=tkinter.Label(self,text="company_ratting",font=("times",20,BOLD))
        self.company_ratting.grid(row=7,column=50)
        self.company_ratting_txt=tkinter.Entry(self,font=("times",15,BOLD))
        self.company_ratting_txt.grid(row=7,column=100)
        self.company_employee=tkinter.Label(self,text="company_employee",font=("times",20,BOLD))
        self.company_employee.grid(row=8,column=50)
        self.company_employee_txt=tkinter.Entry(self,font=("times",15,BOLD))
        self.company_employee_txt.grid(row=8,column=100)
        
        self.add_bu=tkinter.Button(self,text="add",bg="blue",fg="white",font=("times",15,BOLD),command=self.ins)
        self.add_bu.grid(row=9,column=1)
        self.clr_bu=tkinter.Button(self,text="clear",bg="red",fg="white",font=("times",15,BOLD),command=self.clear)
        self.clr_bu.grid(row=9,column=2)
        self.viewall_bu=tkinter.Button(self,text="viewall",bg="white",fg="black",font=("times",15,BOLD),command=self.vw)
        self.viewall_bu.grid(row=9,column=3)
        self.viewone_bu=tkinter.Button(self,text="viewone",bg="pink",fg="white",font=("times",15,BOLD),command=self.one)
        self.viewone_bu.grid(row=9,column=4)
        self.update_bu=tkinter.Button(self,text="update",bg="yellow",fg="white",font=("times",15,BOLD),command=self.update)
        self.update_bu.grid(row=9,column=5)
        self.delete_bu=tkinter.Button(self,text="delete",bg="red",fg="white",font=("times",15,BOLD),command=self.delete)
        self.delete_bu.grid(row=9,column=6)
    def update(self):
        con.autocommit(True)
        qry="""update comany set org='%s',nature='%s',opennings='%s',place='%s',salary=%f,rattings=%f,employee=%d where number=%d"""\
            %(self.company_org_txt.get(),self.company_nature_txt.get(),self.company_opennings_txt.get(),self.company_place_txt.get(),float(self.company_salary_txt.get()),float(self.company_ratting_txt.get()),int(self.company_employee_txt.get()),int(self.number_txt.get()))
        ack=cur.execute(qry)
        if ack!=0:
            messagebox.showinfo("Info","Updated")
            self.clear()
        else:messagebox.showinfo("Info","Not Updated")
    
    def one (self):
        comany=self.number_txt.get()
        qry="select * from comany where number="+comany
        cur.execute(qry)
        single=cur.fetchone()
        self.clear()
        self.number_txt.insert(0,single[0])
        self.company_org_txt.insert(0, single[1])
        self.company_nature_txt.insert(0, single[2])
        self.company_opennings_txt.insert(0, single[3])
        self.company_place_txt.insert(0, single[4])
        self.company_salary_txt.insert(0, single[5])
        self.company_ratting_txt.insert(0, single[6])
        self.company_employee_txt.insert(0, single[7])
    def delete (self):
        con.autocommit(True)
        qry="delete from comany where number="+self.number_txt.get()
        ack=cur.execute(qry)
        if ack!=0:
            messagebox.showinfo("Info","Deleted ")
            self.clear()
        else:
            messagebox.showinfo("Info","Not Deleted")
    
    def vw(self):
        class Vw(tkinter.Frame):
            def __init__(self, parent):
                tkinter.Frame.__init__(self, parent)
                self.CreateUI()
                self.LoadTable()
                self.grid(sticky=(tkinter.N, tkinter.S, tkinter.W, tkinter.E))
                parent.grid_rowconfigure(0, weight=1)
                parent.grid_columnconfigure(0, weight=1)

            def CreateUI(self):
                tv = Treeview(self)
                tv['columns'] = ('number','org', 'nature','opennings', 'place', 'salary', 'rattings','employee')
                tv.heading('#0', text='number', anchor='center')
                tv.column('#0', anchor='center')
                tv.heading('#1', text='org', anchor='center')
                tv.column('#1', anchor='center')
                tv.heading('#2', text='nature', anchor='center')
                tv.column('#2', anchor='center')
                tv.heading('#3', text='opennings', anchor='center')
                tv.column('#3', anchor='center')
                tv.heading('#4', text='place', anchor='center')
                tv.column('#4', anchor='center')
                tv.heading('#5', text='salary', anchor='center')
                tv.column('#5', anchor='center')
                tv.heading('#6', text='rattings', anchor='center')
                tv.column('#6', anchor='center')
                tv.heading('#7', text='employee', anchor='center')
                tv.column('#7', anchor='center')
               
                tv.grid(sticky=(tkinter.N, tkinter.S, tkinter.W, tkinter.E))
                self.treeview = tv
                self.grid_rowconfigure(0, weight=1)
                self.grid_columnconfigure(0, weight=1)

            def LoadTable(self):
                Select = "Select * from comany"
                cur.execute(Select)
                result = cur.fetchall()
                for i in result:
                    self.treeview.insert("", 'end',text=i[0],
                                values=(i[1],i[2],i[3],i[4],i[5],i[6],i[7]))

        root = tkinter.Tk()
        root.title("Every One's Data")
        root.geometry('1024x700')
        Vw(root)
        
    
    def ins(self):
        qry="""insert into comany(number,org,nature,opennings,place,salary,rattings,employee) values(%d,'%s','%s','%s','%s',%f,%f,%d)""" % \
            (int(self.number_txt.get()),self.company_org_txt.get(),self.company_nature_txt.get(),self.company_opennings_txt.get(),self.company_place_txt.get(),float(self.company_salary_txt.get()),float(self.company_ratting_txt.get()),int(self.company_employee_txt.get()))
        ack=cur.execute(qry)
        con.autocommit(True)
        if ack !=0:
            messagebox.showinfo(" company inserted")
            self.clear()
        else:
            messagebox.showinfo("company can t inserted")
    
    def clear(self):
        self.number_txt.delete(0,END)
        self.company_org_txt.delete(0,END)
        self.company_nature_txt.delete(0,END)
        self.company_opennings_txt.delete(0,END)
        self.company_place_txt.delete(0,END)
        self.company_salary_txt.delete(0,END)
        self.company_ratting_txt.delete(0,END)
        self.company_employee_txt.delete(0,END)
        
               
h=Home()
h.mainloop()
            