from tkinter import *
from tkinter import messagebox
win=Tk()
win.title("messagebox")
win.geometry("2000x2000")


def info():
    messagebox.showinfo("message","info")

def error():
    messagebox.showerror("show error","error")

def warning():
    messagebox.showwarning("show warning","warning")

def question():
    messagebox.askquestion("question","question")



info=Button(win,text="show info",pady=10,padx=10,bg="yellow",fg="black",width=20,font=("times",15,"bold"),command=info)
info.pack(pady=5)

info=Button(win,text="show error",pady=10,padx=10,bg="yellow",fg="black",font=("times",15,"bold"),command=error)
info.pack(pady=5)

info=Button(win,text="show warning",pady=10,padx=10,bg="yellow",fg="black",font=("times",15,"bold"),command=warning)
info.pack(pady=5)

info=Button(win,text="show question",pady=10,padx=10,bg="yellow",fg="black",font=("times",15,"bold"),command=question)
info.pack(pady=5)

info=Button(win,text="show error",pady=10,padx=10,bg="yellow",fg="black",font=("times",15,"bold"),command=error)
info.pack(pady=5)

win.mainloop()