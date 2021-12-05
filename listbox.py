from tkinter import *
from tkinter import messagebox
win=Tk()
win.title("listbox")
win.geometry("500x700")

def submit():
    data=txtdata.get()
    lstbox.insert(END,data)

def select():
    data=lstbox.get(ANCHOR)
    messagebox.showinfo("data",data)
def listbind(event):
    id=lstbox.curselection()
    data=lstbox.get(id)
    mdata.set(data)
    #messagebox.showinfo("data",data)

def update():
    if(txtdata.get() !=""):
        uid=lstbox.index(ANCHOR)
        udata=txtdata.get()
        lstbox.delete(ANCHOR)
        lstbox.insert(uid,udata)
        txtdata.delete(0,END)

    else:
        messagebox.showinfo("message","please select any option")

def delete():
    lstbox.delete(ANCHOR)


mdata=StringVar()

txtdata=Entry(win,width=30,textvariable=mdata)
txtdata.pack(pady=10)
lstbox=Listbox(win,width=30,height=15)
lstbox.pack(pady=10)


lstbox.insert(END,"c")
lstbox.insert(END,"c++")
lstbox.insert(END,"java")
lstbox.insert(END,"python")

mydata=["asp.net","VB.net","c#.net"]

for data in mydata:
    lstbox.insert(END,data)

for i in range(10):
    lstbox.insert(END,"python programming languange")

lstbox.bind("<<ListboxSelect>>",listbind)

btnsub=Button(win,text="submit",bg="green",fg="black",padx=10,pady=10,width=10,font=("times",20,"bold"),command=submit)
btnsub.pack(pady=20)

btnselect=Button(win,text="select",bg="blue",fg="black",padx=10,pady=10,width=10,font=("times",20,"bold"),command=select)
btnselect.pack(pady=10)

btnupdate=Button(win,text="update",bg="orange",fg="black",padx=10,pady=10,width=10,font=("times",20,"bold"),command=update)
btnupdate.pack(pady=10)

btndelete=Button(win,text="delete",bg="red",fg="black",padx=10,pady=10,width=10,font=("times",20,"bold"),command=delete)
btndelete.pack(pady=10)


win.mainloop()