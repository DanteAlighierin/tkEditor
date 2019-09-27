import tkinter

def highlight(editor_space, searchfor, color):
       countVar = tkinter.StringVar()

       pos = "1.0"

       while True:
           pos = editor_space.search(searchfor, pos, tkinter.END, count = countVar)

           if not pos:
               break

           lastindex = "{} + {}c".format(pos, countVar.get())

           editor_space.tag_add("keyword", pos, lastindex)

           pos = lastindex

       editor_space.tag_configure("keyword", foreground = color)