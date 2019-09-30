import tkinter
import tkinter.ttk
import tkinter.filedialog
import tkinter.messagebox
import os

try:
       import config
       import menu
       import syntaxhl
       import findtool

except ImportError as e:
       import sys
       sys.exit("Import error.\nRaw: {}".format(e))

class Editor(object):

       def editor(self):
           self.root = tkinter.Tk()

           self.config = config.config()
           self.syntaxcolor = config.syntaxHighligh()

           self.root.wm_title(self.config.editor_title)
           self.root.attributes("-alpha", self.config.transparency)

           # Scrollbar
           self.scrollbar = tkinter.Scrollbar(self.root)
           self.scrollbar.pack(side = tkinter.RIGHT, fill = tkinter.Y)

           # Editor.
           self.editor_space = tkinter.Text(self.root)
           self.editor_space.config(undo = self.config.undo, width = self.config.width,
                                    height = self.config.height, fg = self.config.foreground,
                                    bg = self.config.background, insertbackground = self.config.cursorColor,
                                    yscrollcommand = self.scrollbar.set,
                                    font = (self.config.font, self.config.font_size))

           self.editor_space.pack(fill = tkinter.X)
           self.scrollbar.config(command = self.editor_space.yview)

           # Find tool
           find = findtool.Find(self.editor_space)

           # Menu.
           # Note: The order of the instances is the order in witch the menus will appear.
           self.mn = tkinter.Menu(self.root)
           self.filemenu = menu.FileMenu(self.mn, self.openFile,
                                         self.saveFile, self.destroy,
                                         self.root)

           self.toolmenu = menu.ToolsMenu(self.mn, self.clear,
                                          self.syntaxHighlight,
                                          find.find)

           self.prefmenu = menu.Settings(self.mn, self.openConfigFile)
           self.helpmenu = menu.HelpMenu(self.mn, self.about)


           # Close event.
           if self.config.askokcancel:
               self.root.protocol("WM_DELETE_WINDOW", self.destroy)

           self.root.config(menu = self.mn)

           self.root.mainloop()

       def openConfigFile(self):
           try:
               with open("config.py") as file:
                   for line in file.readlines():
                       self.editor_space.insert(tkinter.END, line)

           except IOError as e:
               tkinter.messagebox.showerror("Error", "Couldn't open file.")

           except Exception as e:
               tkinter.messagebox.showerror("Error", "Error.\n{}".format(repr(e)))

       def destroy(self):
           ako = tkinter.messagebox.askokcancel("Quit", "Are you sure you want to exit?")
           if ako:
               self.root.quit()

       def clear(self):
           self.editor_space.delete("1.0", tkinter.END)

       def saveFile(self):
           path = tkinter.filedialog.asksaveasfilename(defaultextension = self.config.defext)
           filename = os.path.basename(path)

           try:
               with open(filename, "w") as wf:
                   wf.write(self.editor_space.get("0.0", tkinter.END))

               tkinter.messagebox.showinfo(None, "File saved.")

           except IOError as e:
               tkinter.messagebox.showerror("Error", "Couldn't open file.")

           except Exception as e:
               tkinter.messagebox.showerror("Error", "Error.\n{}".format(repr(e)))

       def openFile(self):
           self.clear()
           file = tkinter.filedialog.askopenfile()
           try:
               for line in file.readlines():
                   self.editor_space.insert(tkinter.END, line)

               self.syntaxHighlight()

           except IOError as e:
               tkinter.messagebox.showerror("Error", "Couldn't open file.")

           except Exception as e:
               tkinter.messagebox.showerror("Error", "Error.\n{}".format(repr(e)))

       def syntaxHighlight(self):
           for keyw, color in getattr(self.syntaxcolor, "colors").items():
               syntaxhl.highlight(self.editor_space, keyw, color)

       def about(self):
                      def new_window(): 
                                       newWindow = Toplevel(root)
                                       display = Label(newWindow, width=200, height=50,bg='RED')
                                       message = Label(newWindow, text="HEEEY",fg='BLACK',bg='GREEN')
                                       message.pack()
                                       display.pack()