from tkinter import *
from tkinter import ttk
from tkinter import messagebox


class ChildWindow(object): #Base class
    def __init__(self, parent, title):
        self.parent = parent
        self.f = Frame(parent)
        top = self.top = Toplevel(self.f)
        top.title(title)
        self.create_controls(self.f)
        self.f.pack(fill=BOTH, expand=Y)

    def create_controls(self, container):
        pass

    def make_modal(self):
        #self.top.wait_visibility() # Python will hang here...
        self.top.grab_set()
        self.top.focus_set()
        self.top.protocol("WM_DELETE_WINDOW", self.cancel)
        self.top.transient(self.parent)
        self.top.wait_window(self.top) # ...or here, if wait_visibility is removed

    def cancel(self):
        self.f.destroy()

class Window(Frame):
    
    def __init__(self,root):
        Frame.__init__(self,root)
        self.root = root

        menu = Menu(self.root)
        self.root.config(menu=menu)

        fileMenu = Menu(menu)
        fileMenu.add_command(label="Item",command=self.openDialog)
        fileMenu.add_command(label="Exit", command=self.exitProgram)
        menu.add_cascade(label="File", menu=fileMenu)

        editMenu = Menu(menu)
        editMenu.add_command(label="Undo")
        editMenu.add_command(label="Redo")
        menu.add_cascade(label="Edit", menu=editMenu)

        # code for creating table
        for i in range(total_rows):
            for j in range(total_columns):

                self.e = Entry(root, width=20, fg='blue',
                            font=('Arial',16,'bold'))

                self.e.grid(row=i, column=j)
                self.e.insert(END, lst[i][j])

    def exitProgram(self):
        exit()
    def openDialog(self):
        child = ChildWindow(self,"child window")
        child.make_modal()

        

if __name__ == "__main__":

    # take the data
    lst = [(1,'Raj','Mumbai',19),
        (2,'Aaryan','Pune',18),
        (3,'Vaishnavi','Mumbai',20),
        (4,'Rachna','Mumbai',21),
        (5,'Shubham','Delhi',21)]
    
    # find total number of rows and
    # columns in list
    total_rows = len(lst)
    total_columns = len(lst[0])

    root = Tk()
    app = Window(root)
    root.wm_title("Table and Window")
    root.mainloop()