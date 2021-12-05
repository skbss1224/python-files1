from tkinter import *
from tkinter import ttk
from tkinter import messagebox
win=Tk()
win.title("combo box")
win.geometry("2000x2000")

def comboclick(event):
    data=cb.get()
    messagebox.showinfo("message",data)


lbl=Label(win,text="COMBO BOX",bg="pink",fg="black",padx=30,pady=10,font=("tomes",15,"bold"))
lbl.pack(fill=X)
cb=ttk.Combobox(win,width=50,state="readonly")
cb["values"]=("c","c++","python","java")
cb.current(0)
cb.bind("<<ComboboxSelected>>",comboclick)
cb.pack(pady=30)


win.mainloop()