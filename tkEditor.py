#!/usr/bin/env python3
from tkinter import *
from tkinter.ttk import *
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
        mb.showerror("Error!", "Error")
def text_delete():
    delete=mb.askokcancel(title="Are you sure?", message="Are you sure?")
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
        mb.showerror("Error", "Error")

strr = ["Dark theme", "Light theme"]











root=Tk()

def full():
  try:
    root.overrideredirect(True)
    root.overrideredirect(False)
    root.attributes('-fullscreen',True)
  except:
    mb.showerror("Error!", "Error")
main_menu = Menu()
"""file works """
file_menu = Menu()
file_menu.add_command(label="New")
file_menu.add_command(label="Save", command = openr)
file_menu.add_command(label="Open")
file_menu.add_separator()
file_menu.add_command(label="Exit")
     

"""Edit menu """
file_edit = Menu()
file_edit.add_command(label="Cut", command = text_delete)


"""View menu """
view_menu = Menu()

view_menu.add_command(label = "Change theme")
view_menu.add_command(label = "Change language")
view_menu.add_command(label = "Change font")
view_menu.add_command(label = "Enter fullscreen mode", command = full)

"""main menu"""
main_menu.add_cascade(label="File", menu=file_menu)
main_menu.add_cascade(label="Edit", menu=file_edit)
main_menu.add_cascade(label="View", menu=view_menu)
 
root.config(menu=main_menu)



root.title("Dante's text editor")


"""a=Button(text="Выбрать файл", bg="grey", command=openr)"""
b=Text(width=250,
       height=10,
       bg="grey",
       fg="white",
       wrap=WORD)
alt=Text(width=250,
         height=10,
         bg="white",
         fg="black",
         wrap=WORD)
"""c=Button(text="Очистить", bg="grey", command=text_delete)
d=Button(text="Сохранить", bg="grey", command=save)
a.pack()"""
b.pack()
alt.pack()
"""c.pack()
d.pack()"""


root.mainloop()