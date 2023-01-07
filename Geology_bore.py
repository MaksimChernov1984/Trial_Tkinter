import tkinter as tk
from tkinter import ttk
import sqlite3

class Main(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.init_main()
        self.db = db
        self.view_records()  # при открытии в первый раз выполнять

    def init_main(self):
        toolbar = tk.Frame(bg='#FFE4C4')
        toolbar.pack(side=tk.TOP, fill=tk.Y)
        btn_open_log = tk.Button(toolbar, text='Журнал', command=self.open_log, bg='#F4A460',
                                    activebackground='#A52A2A', bd=0)
        btn_open_log.pack(side=tk.LEFT)


# кнопка Открыть чертёж
        btn_open_draw = tk.Button(toolbar, text='Чертёж', command=self.open_draw, bg='#F4A460',
                                    activebackground='#A52A2A', bd=0)
        btn_open_draw.pack(side=tk.LEFT)


        self.tree = ttk.Treeview(self, columns=('ID', 'layer_base', 'layer_description','sample_type', 'sample_depth'),
                                height=15, show='headings')
        self.tree.column('ID', width=50, anchor=tk.CENTER)
        self.tree.column('layer_base', width=100, anchor=tk.CENTER)
        self.tree.column('layer_description', width=500, anchor=tk.W)
        self.tree.column('sample_type', width=100, anchor=tk.CENTER)
        self.tree.column('sample_depth', width=100, anchor=tk.CENTER)

        self.tree.heading('ID', text='ID')
        self.tree.heading('layer_base', text='Подошва элемента')
        self.tree.heading('layer_description', text='Описание')
        self.tree.heading('sample_type', text='Вид образца')
        self.tree.heading('sample_depth', text='Глубина образца')

        self.tree.pack()

    def records(self, layer_base, layer_description, sample_type, sample_depth):
        self.db.insert_data(layer_base, layer_description, sample_type, sample_depth)
        self.view_records()  # после каждого добавления поля опять выполнить новую функцию отображения

    def view_records(self):
        self.db.c.execute('''SELECT * FROM engineering_geology''')
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.c.fetchall()]

# открыть журнал
    def open_log(self):
        Log()

# открыть чертёж
    def open_draw(self):
        Draw()

class Log(tk.Toplevel):
    def __init__(self):
        super().__init__(root)
        self.init_log()
        self.view = app

    def init_log(self):
        self.title('Журнал')
        self.geometry('1100x700+20+20')
        self.resizable(False, False)


        label_layer_base = tk.Label(self, text='Подошва элемента').place(x=5, y=5)
        label_layer_description = tk.Label(self, text='Описание элемента').place(x=5, y=35)
        label_sample_type = tk.Label(self, text='Вид образца').place(x=5, y=65)
        label_layer_description = tk.Label(self, text='Глубина образца').place(x=5, y=95)

        self.entry_layer_base = ttk.Entry(self)
        self.entry_layer_base.place(x=150, y=5)

        self.entry_layer_description = ttk.Entry(self)
        self.entry_layer_description.place(x=150, y=35)

        self.combobox_sample_type = ttk.Combobox(self, values=[u'Монолит', u'Нарушенный'])
        self.combobox_sample_type.place(x=150, y=65)
        self.combobox_sample_type.current(0)

        self.entry_sample_depth = ttk.Entry(self)
        self.entry_sample_depth.place(x=150, y=95)


        btn_ok = ttk.Button(self, text='Добавить')
        btn_ok.bind('<Button-1>', lambda event: self.view.records(self.entry_layer_base.get(),
                                                                  self.entry_layer_description.get(),
                                                                  self.combobox_sample_type.get(),
                                                                  self.entry_sample_depth.get()))
        btn_ok.place(x=50, y=130)


        btn_cancel = ttk.Button(self, text='Закрыть журнал', command=self.destroy)
        btn_cancel.place(x=50, y=170)

        self.grab_set()
        self.focus_set()


class DB:
    def __init__(self):
        self.conn = sqlite3.connect('engineering_geology.db')
        self.c = self.conn.cursor()
        self.c.execute(
            '''CREATE TABLE IF NOT EXISTS engineering_geology 
            (id integer primary key, layer_base real, layer_description text, sample_type text, sample_depth real)'''
        )
        self.conn.commit()

    def insert_data(self, layer_base, layer_description, sample_type, sample_depth):
        self.c.execute('''INSERT INTO engineering_geology (layer_base, layer_description, sample_type, sample_depth) 
         VALUES (?, ?, ?, ?)''', (layer_base, layer_description, sample_type, sample_depth))
        self.conn.commit()

# окно с чертежём
class Draw(tk.Toplevel):
    def __init__(self):
        super().__init__(root)
        self.init_draw()
        self.view = app

    def init_draw(self):
        self.title('Чертёж')
        self.geometry('1100x600+20+20')
        self.resizable(False, False)


if __name__=='__main__':
    root = tk.Tk()
    db = DB()
    app = Main(root)
    app.pack()
    root.title('Геология')
    root.geometry('1100x700+20+20')
    root.resizable(False, False)
    root.mainloop()
