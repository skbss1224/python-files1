import os
from tkinter import *
from tkinter import ttk,filedialog,messagebox
import pandas as pd

win=Tk()
win.geometry("1000x500")
win.title("import and export file")

def Field_Dialogue():
    filename=filedialog.askopenfilename(initialdir="C:/Users/srihojith",title="select a file",filetype=(("xlsx files","*.xlsx"),("csv Files","*.csv"),("All Files","*.*")))
    lbl["text"]=filename
    return None

def Load_Excel_Data():
    global df
    file_path=lbl["text"]

    try:
        excel_filename=r"{}".format(file_path)
        filename,fileextension=os.path.splitext(excel_filename)
        if fileextension==".xlsx":
            df=pd.read_excel(excel_filename)
        elif fileextension==".csv":
            df=pd.read_csv(excel_filename)

    except ValueError:
        messagebox.showinfo("message","the file is invalid")
        return None
    except FileNotFoundError:
        messagebox.showinfo(("message",f"no such file as{file_path}"))
        return None

    treeview["column"]=list(df.columns)
    treeview["show"]="headings"
    for column in treeview["column"]:
        treeview.heading(column,text=column)

    DataFrameRows=df.to_numpy().tolist()
    for row in DataFrameRows:
        treeview.insert("","end",values=row)
    return None

def exportexceldata():
    if len(treeview.get_children())<1:
        messagebox.showinfo("nodata","data available to export data")
        return False
    file=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="name is defined")

myframeexcel=LabelFrame(win,text="Import Excel")
myframeexcel.pack(fill=BOTH,expand=TRUE,padx=10,pady=30)

myframbtn=LabelFrame(win,text="open field dialogue")
myframbtn.pack(fill=BOTH,expand=TRUE,padx=10)

lbl=Label(myframbtn,text="No file selected",font=("times",15,"bold"),fg="blue")
lbl.grid(row=0,column=0,padx=10,pady=10)


treeview=ttk.Treeview(myframeexcel)
treeview.place(relheight=1,relwidth=1)

btnbrowse=Button(myframbtn,text="Browse file",bg="#1289A7",width=10,fg="white",font=("times",15,"bold"),command=Field_Dialogue)
btnbrowse.grid(row=1,column=0,padx=10,pady=20)

btnimport=Button(myframbtn,text="import",bg="pink",width=10,fg="white",font=("times",15,"bold"),command=Load_Excel_Data)
btnimport.grid(row=1,column=1,padx=10,pady=20)

btnexport=Button(myframbtn,text="export",bg="green",width=10,fg="white",font=("times",15,"bold"),command=exportexceldata)
btnexport.grid(row=1,column=2,padx=10,pady=20)

win.mainloop()
