import tkinter as tk

class Main(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.init_main()
    def init_main(self):
        toolbar = tk.Frame(bg='#FFE4C4')
        toolbar.pack(side=tk.LEFT, fill=tk.Y)
        btn_open_dialog = tk.Button(toolbar, text='Открыть журнал', command=self.open_dialog, bg='#F4A460',
                                    activebackground='#A52A2A', bd=0)
        btn_open_dialog.grid(column=0, row=1)

    def open_dialog(self):
        Child()

class Child(tk.Toplevel):
    def __init__(self):
        super().__init__(root)
        self.init_child()

    def init_child(self):
        self.title('Журнал')
        self.geometry('400x220+400+300')
        self.resizable(False, False)

        self.grab_set()
        self.focus_set()


if __name__=='__main__':
    root = tk.Tk()
    app = Main(root)
    app.pack()
    root.title('Геология')
    root.geometry('650x450+300+200')
    root.resizable(False, False)
    root.mainloop()
