import tkinter
import tkinter.ttk
import config

class Find(object):

       def __init__(self, es):
           self.editor_space = es
           self.config = config.config()

       def find(self):
           # Find window and stuff.
           root = tkinter.Tk()
           tkinter.Label(root, text = "Seach for: ").grid(row = 1, column = 0)

           input_ = tkinter.ttk.Entry(root, width = 20)
           input_.grid(row = 1, column = 1)

           self.editor_space.tag_configure("search", background = self.config.matchColor)

           # Search button.
           tkinter.ttk.Button(root, text = "Search", command=lambda: self.search_editor_space(input_.get())).grid(row = 2, column = 1,
                                                                                                              columnspan = 2)

           # On close.
           root.protocol("WM_DELETE_WINDOW", lambda: self.destroy_find_window(root))


       def destroy_find_window(self, root):
           self.editor_space.tag_remove("found", "1.0", tkinter.END)
           root.destroy()

       def search_editor_space(self, searchfor):
           # Actual search.
           # Got from(with small modifications): http://www.java2s.com/Code/Python/GUI-Tk/SearchstringinText.html
           # Thanks.

           self.editor_space.tag_config("found", foreground = self.config.matchColor)
           countVar = tkinter.IntVar()

           item = "1.0"

           while True:
               item = self.editor_space.search(searchfor, item, tkinter.END, count = countVar)

               if not item:
                   break

               lastindex = "{} + {}c".format(item, countVar.get())

               self.editor_space.tag_add("found", item, lastindex)

               item = lastindex