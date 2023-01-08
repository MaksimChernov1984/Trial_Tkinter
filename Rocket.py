# код, написанный для изучения библиотеки tkinter
from tkinter import *


window = Tk()
window.title('Ракета')
window.geometry('1000x800')

w_canvas = 500  # ширина листа
h_canvas = 690  # высота листа
x = 250  # координата первой точки по x
y = 50  # координата первой точки по Y
font_size = 10
p_y = 2  # промежуток по у

def rocket(h0):
    h0 = int(hh0.get())  # высота конуса
    w0 = int(ww0.get())   # ширина конуса
    h3 = int(hh3.get())  # высота ступени 3
    h2 = int(hh2.get())   # высота ступени 2
    h1 = int(hh1.get())  # высота ступени 1
    h_jet0 = int(hh_jet0.get())   # высота сопла
    h_jet1 = int(hh_jet1.get())  # высота боковых ускорителей
    w_jet1 = int(ww_jet1.get())  # ширина боковых ускорителей
    cr = str(c_rocket.get())
    color_rocket = '#' + cr + ''
    cs = str(c_space.get())
    color_space = '#' + cs + ''

    # лист
    cv = Canvas(window, width=w_canvas, height=h_canvas, bg=color_space)
    cv.place(x=400, y=0)

# конус
    cv.create_polygon(x, y,
                      x + 0.5 * w0, y + h0,
                      x - 0.5 * w0, y + h0,
                      fill=color_rocket, width=1, outline='#000')

# иллюминатор
    cv.create_oval(x - 0.05 * w0, y + 0.6*h0,
                   x + 0.05*w0, y + 0.6*h0 + 0.1*w0,
                   fill=color_space, width=1, outline='#000')

# ступень 3
    cv.create_polygon(x + 0.5 * w0, y + h0,
                      x + 0.5 * w0, y + h0+0.3*h3,
                      x + 0.6 * w0, y + h0 + 0.4 * h3,
                      x + 0.6 * w0, y + h0 + 0.5 * h3,
                      x + 0.5 * w0, y + h0 + 0.5 * h3,
                      x + 0.5 * w0, y + h0 + h3,
                      x - 0.5 * w0, y + h0 + h3,
                      x - 0.5 * w0, y + h0 + 0.5 * h3,
                      x - 0.6 * w0, y + h0 + 0.5 * h3,
                      x - 0.6 * w0, y + h0 + 0.4 * h3,
                      x - 0.5 * w0, y + h0 + 0.3 * h3,
                      x - 0.5 * w0, y + h0,
                      x - 0.5 * w0, y + h0,
                      fill=color_rocket, width=1, outline='#000')

# ступень 2
    cv.create_polygon(x - 0.5 * w0, y + h0 + h3,
                      x + 0.5 * w0, y + h0 + h3,
                      x+0.6*w0, y+h0+h3+0.1*h2,
                      x + 0.6 * w0, y + h0 + h3 + h2,
                      x - 0.6 * w0, y + h0 + h3 + h2,
                      x-0.6*w0, y+h0+h3+0.1*h2,
                      fill=color_rocket, width=1, outline='#000')

# ступень 1
    cv.create_polygon(x - 0.6 * w0, y + h0 + h3 + h2,
                        x + 0.6 * w0, y + h0 + h3 + h2,
                        x + 0.7 * w0, y + h0 + h3 + h2 + 0.1 * h1,
                        x + 0.7 * w0, y + h0 + h3 + h2 + h1,
                        x - 0.7 * w0, y + h0 + h3 + h2 + h1,
                        x - 0.7 * w0, y + h0 + h3 + h2 + 0.1 * h1,
                        fill=color_rocket, width=1, outline='#000')

# основное сопло
    cv.create_polygon(x - 0.7 * w0, y + h0 + h3 + h2+h1,
                      x + 0.7 * w0, y + h0 + h3 + h2 +h1,
                      x + 0.8 * w0, y + h0 + h3 + h2 + h1+0.1*h_jet0,
                      x + 0.8 * w0, y + h0 + h3 + h2 + h1+h_jet0,
                      x - 0.8 * w0, y + h0 + h3 + h2 + h1 + h_jet0,
                      x - 0.8 * w0, y + h0 + h3 + h2 + h1+0.1*h_jet0,
                      fill=color_rocket, width=1, outline='#000')

# боковой ускоритель левый
    cv.create_polygon(x - 0.8 * w0-0.5*w_jet1, y+h0+h3+h2+h1+h_jet0-h_jet1,
                      x - 0.8 * w0,y+h0+h3+h2+h1+h_jet0-h_jet1+0.5*w_jet1,
                      x - 0.8 * w0,y+h0+h3+h2+h1+h_jet0,
                      x - 0.8 * w0 -w_jet1,y+h0+h3+h2+h1+h_jet0,
                      x - 0.8 * w0 - w_jet1,y+h0+h3+h2+h1+h_jet0-h_jet1+0.5*w_jet1,
                      fill=color_rocket, width=1, outline='#000')

# боковой ускоритель правый
    cv.create_polygon(x + 0.8 * w0 + 0.5 * w_jet1, y + h0 + h3 + h2 + h1 + h_jet0 - h_jet1,
                      x + 0.8 * w0, y + h0 + h3 + h2 + h1 + h_jet0 - h_jet1 + 0.5*w_jet1,
                      x + 0.8 * w0, y + h0 + h3 + h2 + h1 + h_jet0,
                      x + 0.8 * w0 + w_jet1, y + h0 + h3 + h2 + h1 + h_jet0,
                      x + 0.8 * w0 + w_jet1, y + h0 + h3 + h2 + h1 + h_jet0 - h_jet1 + 0.5*w_jet1,
                      fill=color_rocket, width=1, outline='#000')

    cv.create_text(x,y+h0+0.5*h3, text=rocket_text.get(), fill=color_space)




f = '#fff'  # цвет текста
b = '#002'  # цвет фона текста
window['bg'] = b  # цвет окна


lbl = Label(window, font=font_size, fg=f, bg=b, pady=p_y)
lbl.configure(text='Давайте нарисуем ракету!')
lbl.place(x=50, y=10)

# высота конуса
lbl = Label(window, font=font_size, fg=f, bg=b, pady=p_y)
lbl.configure(text='Высота конуса')
lbl.place(x=10, y=40)

hh0 = Entry(window, width=10)
hh0.place(x=300, y=40)
hh0.focus()

# ширина конуса
lbl = Label(window, font=font_size, fg=f, bg=b, pady=p_y)
lbl.configure(text='Ширина конуса')
lbl.place(x=10, y=70)

ww0 = Entry(window, width=10)
ww0.place(x=300, y=70)

# высота ступени 3
lbl = Label(window, font=font_size, fg=f, bg=b, pady=p_y)
lbl.configure(text='Высота третьей ступени')
lbl.place(x=10, y=100)

hh3 = Entry(window, width=10)
hh3.place(x=300, y=100)

# высота ступени 2
lbl = Label(window, font=font_size, fg=f, bg=b, pady=p_y)
lbl.configure(text='Высота второй ступени')
lbl.place(x=10, y=130)

hh2 = Entry(window, width=10)
hh2.place(x=300, y=130)

# высота ступени 1
lbl = Label(window, font=font_size, fg=f, bg=b, pady=p_y)
lbl.configure(text='Высота первой ступени')
lbl.place(x=10, y=160)

hh1 = Entry(window, width=10)
hh1.place(x=300, y=160)

# высота основного сопла
lbl = Label(window, font=font_size, fg=f, bg=b, pady=p_y)
lbl.configure(text='Высота основного сопла')
lbl.place(x=10, y=190)

hh_jet0 = Entry(window, width=10)
hh_jet0.place(x=300, y=190)

# высота боковых ускорителей
lbl = Label(window, font=font_size, fg=f, bg=b, pady=p_y)
lbl.configure(text='Высота боковых ускорителей')
lbl.place(x=10, y=220)

hh_jet1 = Entry(window, width=10)
hh_jet1.place(x=300, y=220)

# ширина боковых ускорителей
lbl = Label(window, font=font_size, fg=f, bg=b, pady=p_y)
lbl.configure(text='Ширина боковых ускорителей')
lbl.place(x=10, y=250)

ww_jet1 = Entry(window, width=10)
ww_jet1.place(x=300, y=250)

# цвет ракеты
lbl = Label(window, font=font_size, fg=f, bg=b, pady=p_y)
lbl.configure(text='Цвет ракеты')
lbl.place(x=10, y=280)

c_rocket = Entry(window, width=10)
c_rocket.place(x=300, y=280)

#цвет космоса
lbl = Label(window, font=font_size, fg=f, bg=b, pady=p_y)
lbl.configure(text='Цвет космоса')
lbl.place(x=10, y=310)

c_space = Entry(window, width=10)
c_space.place(x=300, y=310)

# надпись
lbl = Label(window, font=font_size, fg=f, bg=b, pady=p_y)
lbl.configure(text='Бортовая надпись')
lbl.place(x=10, y=340)

rocket_text = Entry(window, width=10)
rocket_text.place(x=300, y=340)


btn = Button(window, text='Рисуем ракету', bg='#DB7093', activebackground='#f0f', fg='#000', command=rocket)
btn.place(x=100, y=380)
btn.bind('<Return>', rocket)





window.mainloop()
