import tkinter as tk
from tkinter import ttk

class Main(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.init_main()
    def init_main(self):
        toolbar = tk.Frame(bg='#FFE4C4')
        toolbar.pack(side=tk.LEFT, fill=tk.Y)
        btn_open_dialog = tk.Button(toolbar, text='Открыть журнал', command=self.open_dialog, bg='#F4A460',
                                    activebackground='#A52A2A', bd=0)
        btn_open_dialog.pack(side=tk.LEFT)
        self.tree = ttk.Treeview(self, columns=('ID', 'layer_base', 'layer_description','sample_type', 'sample_depth'),
                                height=15, show='headings')
        self.tree.column('ID', width=30, anchor=tk.CENTER)
        self.tree.column('layer_base', width=30, anchor=tk.CENTER)
        self.tree.column('layer_description', width=30, anchor=tk.CENTER)
        self.tree.column('sample_type', width=30, anchor=tk.CENTER)
        self.tree.column('sample_depth', width=30, anchor=tk.CENTER)

        self.tree.heading('ID', text='ID')
        self.tree.heading('layer_base', text='Подошва элемента')
        self.tree.heading('layer_description', text='Описание')
        self.tree.heading('sample_type', text='Вид образца')
        self.tree.heading('sample_depth', text='Глубина образца')

        self.tree.pack()

    def open_dialog(self):
        Child()

class Child(tk.Toplevel):
    def __init__(self):
        super().__init__(root)
        self.init_child()

    def init_child(self):
        self.title('Журнал')
        self.geometry('1000x700+20+20')
        self.resizable(False, False)


        label_layer_base = tk.Label(self, text='Подошва элемента')
        label_layer_base.place(x=5, y=5)
        label_layer_description = tk.Label(self, text='Описание элемента')
        label_layer_description.place(x=5, y=35)
        label_sample_type = tk.Label(self, text='Вид образца')
        label_sample_type.place(x=5, y=65)
        label_layer_description = tk.Label(self, text='Глубина образца')
        label_layer_description.place(x=5, y=95)

        self.entry_layer_base = ttk.Entry(self)
        self.entry_layer_base.place(x=150, y=5)

        self.entry_layer_description = ttk.Entry(self)
        self.entry_layer_description.place(x=150, y=35)

        self.combobox = ttk.Combobox(self, values=[u'Монолит', u'Нарушенный'])
        self.combobox.current(0)
        self.combobox.place(x=150, y=65)

        self.entry_sample_depth = ttk.Entry(self)
        self.entry_sample_depth.place(x=150, y=95)

        btn_ok = ttk.Button(self, text='Добавить')
        btn_ok.bind('<Return>')
        btn_ok.place(x=50, y=130)


        btn_cancel = ttk.Button(self, text='Закрыть журнал', command=self.destroy)
        btn_cancel.place(x=50, y=170)


        self.grab_set()
        self.focus_set()


if __name__=='__main__':
    root = tk.Tk()
    app = Main(root)
    # app.pack()
    root.title('Геология')
    root.geometry('1000x700+20+20')
    # window.config(bg='#F4A460')
    root.resizable(False, False)
    root.mainloop()
