import tkinter
import tkinter.ttk

class FileMenu(object):

       def __init__(self, menubar, openFunc, saveFunc, closeFunc, root):
           self.of = openFunc
           self.sf = saveFunc
           self.cf = closeFunc

           self.menu = tkinter.Menu(menubar)

           filemenu = tkinter.Menu(self.menu)
           filemenu.add_command(label = "Open", command = self.of)
           filemenu.add_command(label = "Save", command = self.sf)
           filemenu.add_separator()
           filemenu.add_command(label = "Exit", command = self.cf)

           menubar.add_cascade(label = "File", menu = filemenu)

class HelpMenu(object):

       def __init__(self, menubar, aboutFunc):
           self.helpmenu = tkinter.Menu(menubar)

           self.helpmenu.add_command(label = "About", command = aboutFunc)

           menubar.add_cascade(label = "Help", menu = self.helpmenu)

class ToolsMenu(object):

       def __init__(self, menubar, clearFunc, syntaxHighL, find):
           self.cf = clearFunc
           self.fd = find
           self.sh = syntaxHighL
           self.toolsmenu = tkinter.Menu(menubar)

           self.toolsmenu.add_command(label = "Clear", command = self.cf)
           self.toolsmenu.add_command(label = "Find", command = self.fd)
           self.toolsmenu.add_command(label = "Syntax highlighting", command = self.sh)

           menubar.add_cascade(label = "Tools", menu = self.toolsmenu)

class Settings(object):

       def __init__(self, menubar, configFile):
           self.prefmenu = tkinter.Menu(menubar)

           self.prefmenu.add_command(label = "Settings", command = configFile)

           menubar.add_cascade(label = "Preferences", menu = self.prefmenu)

class View(object):
      def __init__(self, menubar):
           self.viewses = tkinter.Menu(menubar)

           self.viewses.add_command(label="View", command=None)

           menubar.add_cascade(label="Fullscreen mode", menu = self.viewses)
