# код, написанный для изучения библиотеки tkinter
from tkinter import *
from tkinter.ttk import Combobox


window = Tk()
window.title('Скважина')
window.geometry('1200x650')
window.resizable(False, False)

w_canvas = 700  # ширина листа
h_canvas = 600  # высота листа
x = 150  # координата первой точки по x
y = 50  # координата первой точки по Y
font_size = 10
f = '#000'  # цвет текста
b = '#FFFFE0'  # цвет фона текста
window['bg'] = b  # цвет окна
p_x = 5  # отступ по х
p_y = 5  # отступ по у


def draw(b_dpt):
    b_dpt = float(bore_depth.get())  # глубина скважины
    lr_01_dpt = float(layer_01_depth.get())  # нижняя граница слоя 1
    lr_02_dpt = float(layer_02_depth.get())  # нижняя граница слоя 2
    lr_03_dpt = float(layer_03_depth.get())  # нижняя граница слоя 3
    lr_04_dpt = float(layer_04_depth.get())  # нижняя граница слоя 4
    lr_05_dpt = float(layer_05_depth.get())  # нижняя граница слоя 5
    x_width = 100  # отступ от скважины по х
    y_thick = 30  # коэффициент толщины слоя по у


    # лист
    cv = Canvas(window, width=w_canvas, height=h_canvas, bg='#fff')
    cv.grid(column=2, row=0, rowspan=15, padx=p_x, pady=p_y)

    # скважина
    cv.create_rectangle(x-5,y,  x+5,y+b_dpt*y_thick, outline='#000')

    # 1 слой
    cv.create_rectangle(x - x_width,y,  x + x_width,y + lr_01_dpt * y_thick, outline='#000')

    # 2 слой
    cv.create_rectangle(x - x_width,y,  x + x_width, y + lr_02_dpt * y_thick, outline='#000')

    # 3 слой
    cv.create_rectangle(x - x_width,y,  x + x_width, y + lr_03_dpt * y_thick, outline='#000')

    # 4 слой
    cv.create_rectangle(x - x_width,y,  x + x_width, y + lr_04_dpt * y_thick, outline='#000')

    # 5 слой
    cv.create_rectangle(x - x_width,y,  x + x_width, y + lr_05_dpt * y_thick, outline='#000')

    # текст Номер скважины
    cv.create_text(x, y-40, text='Скважина № '+bore_number.get())

    # текст Отметка скважины
    cv.create_text(x, y - 20, text=bore_abs.get()+' м.')

    # текст Отметка подошвы слоя 1
    cv.create_text(x+20, y+lr_01_dpt*y_thick-10, text=lr_01_dpt)

    # текст Название слоя 1
    cv.create_text(x+x_width+30, y + lr_01_dpt * y_thick*0.5, text=layer_01.get(), justify=LEFT)

    # текст Отметка подошвы слоя 2
    cv.create_text(x + 20, y + lr_02_dpt * y_thick-10, text=lr_02_dpt)

    # текст Название слоя 2
    cv.create_text(x + x_width + 30, y + (lr_01_dpt+(lr_02_dpt-lr_01_dpt)*0.5) * y_thick, text=layer_02.get(), justify=LEFT)

    # текст Отметка подошвы слоя 3
    cv.create_text(x + 20, y + lr_03_dpt * y_thick-10, text=lr_03_dpt)

    # текст Название слоя 3
    cv.create_text(x + x_width + 30, y + (lr_02_dpt+(lr_03_dpt-lr_02_dpt)*0.5) * y_thick, text=layer_03.get(), justify=LEFT)

    # текст Отметка подошвы слоя 4
    cv.create_text(x + 20, y + lr_04_dpt * y_thick-10, text=lr_04_dpt)

    # текст Название слоя 4
    cv.create_text(x + x_width + 30, y + (lr_03_dpt+(lr_04_dpt-lr_03_dpt)*0.5) * y_thick, text=layer_04.get(), justify=LEFT)

    # текст Отметка подошвы слоя 5
    cv.create_text(x + 20, y + lr_05_dpt * y_thick-10, text=lr_05_dpt)

    # текст Название слоя 5
    cv.create_text(x + x_width + 30, y + (lr_04_dpt+(lr_05_dpt-lr_04_dpt)*0.5) * y_thick, text=layer_05.get(), justify=LEFT)


# номер скважины
lbl = Label(window, text='скв. №', font=font_size, fg=f, bg=b)
lbl.grid(column=0, row=0, stick='ens', padx=p_x, pady=p_y)

bore_number = Entry(window, width=20)
bore_number.grid(column=1, row=0)
bore_number.focus()

# отметка устья скважины
lbl = Label(window, text='Абс. отметка', font=font_size, fg=f, bg=b)
lbl.grid(column=0, row=1, stick='ens', padx=p_x, pady=p_y)

bore_abs = Entry(window, width=20)
bore_abs.grid(column=1, row=1)

# глубина скважины
lbl = Label(window, text='Глубина скважины', font=font_size, fg=f, bg=b)
lbl.grid(column=0, row=2, stick='ens', padx=p_x, pady=p_y)

bore_depth = Entry(window, width=20)
bore_depth.grid(column=1, row=2)

# количество слоёв
lbl = Label(window, text='Кол-во ИГЭ', font=font_size, fg=f, bg=b)
lbl.grid(column=0, row=3, stick='e', padx=p_x, pady=p_y)

amount_layers = Spinbox(window, from_=1, to=5, width=19)
amount_layers.grid(column=1, row=3)

# слой 1
lbl = Label(window, text='Первый элемент', font=font_size, fg=f, bg=b)
lbl.grid(column=0, row=4, stick='ens', padx=p_x, pady=p_y)

layer_01 = Entry(window, width=20)
layer_01.grid(column=1, row=4)

lbl = Label(window, text='Подошва первого элемента', font=font_size, fg=f, bg=b, padx=p_x, pady=p_y)
lbl.grid(column=0, row=5, stick='ens', padx=p_x, pady=p_y)

layer_01_depth = Entry(window, width=20)
layer_01_depth.grid(column=1, row=5)

# слой 2
lbl = Label(window, text='Второй элемент', font=font_size, fg=f, bg=b, padx=p_x, pady=p_y)
lbl.grid(column=0, row=6, stick='ens', padx=p_x, pady=p_y)

layer_02 = Entry(window, width=20)
layer_02.grid(column=1, row=6)

lbl = Label(window, text='Подошва второго элемента', font=font_size, fg=f, bg=b, padx=p_x, pady=p_y)
lbl.grid(column=0, row=7, stick='ens', padx=p_x, pady=p_y)

layer_02_depth = Entry(window, width=20)
layer_02_depth.grid(column=1, row=7)

# слой 3
lbl = Label(window, text='Третий элемент', font=font_size, fg=f, bg=b, padx=p_x, pady=p_y)
lbl.grid(column=0, row=8, stick='ens', padx=p_x, pady=p_y)

layer_03 = Entry(window, width=20)
layer_03.grid(column=1, row=8)

lbl = Label(window, text='Подошва третьего элемента', font=font_size, fg=f, bg=b, padx=p_x, pady=p_y)
lbl.grid(column=0, row=9, stick='ens', padx=p_x, pady=p_y)

layer_03_depth = Entry(window, width=20)
layer_03_depth.grid(column=1, row=9)

# слой 4
lbl = Label(window, text='Четвёртый элемент', font=font_size, fg=f, bg=b, padx=p_x, pady=p_y)
lbl.grid(column=0, row=10, stick='ens', padx=p_x, pady=p_y)

layer_04 = Entry(window, width=20)
layer_04.grid(column=1, row=10)

lbl = Label(window, text='Подошва четвёртого элемента', font=font_size, fg=f, bg=b, padx=p_x, pady=p_y)
lbl.grid(column=0, row=11, stick='ens', padx=p_x, pady=p_y)

layer_04_depth = Entry(window, width=20)
layer_04_depth.grid(column=1, row=11)

# слой 5
lbl = Label(window, text='Пятый элемент', font=font_size, fg=f, bg=b, padx=p_x, pady=p_y)
lbl.grid(column=0, row=12, stick='ens', padx=p_x, pady=p_y)

layer_05 = Entry(window, width=20)
layer_05.grid(column=1, row=12)

lbl = Label(window, text='Подошва пятого элемента', font=font_size, fg=f, bg=b, padx=p_x, pady=p_y)
lbl.grid(column=0, row=13, stick='ens', padx=p_x, pady=p_y)

layer_05_depth = Entry(window, width=20)
layer_05_depth.grid(column=1, row=13)


btn = Button(window, text='Чертёж скважины', bg='#DB7093', activebackground='#f0f', fg='#000', command=draw)
btn.bind('<Return>', draw)
btn.grid(column=0, columnspan=2, row=14, stick='ens', padx=p_x, pady=p_y)



window.mainloop()
