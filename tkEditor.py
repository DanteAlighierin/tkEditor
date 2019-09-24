#!/usr/bin/env python3
from tkinter import *
from tkinter import messagebox as mb
from tkinter import filedialog as fd
def openr():
    try:
        window=fd.askopenfilename()
        file=open(window)
        s=file.read()
        b.delete(0.0, END)
        b.insert(1.0,s)
        file.close()
    except:
        mb.showerror("Ошибка!", "Ошибка)")
def text_delete():
    delete=mb.askyesno(title="Вы уверены?", message="Вы уверены?")
    if delete==True:
        b.delete(0.0, END)
def save():
    try:
        window=fd.asksaveasfilename()
        file=open(window, "w")
        s=b.get(1.0, END)
        file.write(s)
        file.close()
    except:
        mb.showerror("Ошибка!", "ошибка)")
root=Tk()
root.title("Dante's text editor")
a=Button(text="Выбрать файл", bg="grey", command=openr)
b=Text(width=100,
       height=25,
       bg="grey",
       fg="white",
       wrap=WORD)
c=Button(text="Очистить", bg="grey", command=text_delete)
d=Button(text="Сохранить", bg="grey", command=save)
a.pack()
b.pack()
c.pack()
d.pack()

root.mainloop()