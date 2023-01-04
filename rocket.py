# код, написанный для изучения библиотеки tkinter
from tkinter import *


window = Tk()
window.title('Ракета')
window.geometry('700x700')

w_canvas = 400  # ширина листа
h_canvas = 600  # высота листа
x = 200  # координата первой точки по x
y = 50  # координата первой точки по Y
font_size = 14

def rocket():
    h0 = int(hh0.get())  # высота конуса
    w0 = int(ww0.get())   # ширина конуса
    h1 = int(hh1.get())   # высота первой ступени
    h2 = int(hh2.get())   # высота второй ступени
    h_jet = int(hh_jet.get())   # высота сопла

    # конус
    cv.create_polygon(x, y, x + 0.5 * w0, y + h0, x - 0.5 * w0, y + h0, fill=color_rocket, width=1, outline='#000')

    # первая ступень
    cv.create_rectangle(x - 0.5 * w0, y + h0, x + 0.5 * w0, y + h0 + h1, fill=color_rocket, width=1, outline='#000')

    # иллюминатор
    cv.create_oval(x - 0.1 * w0, y + h0 + 0.3 * h1, x + 0.1 * w0, y + h0 + 0.3 * h1 + 0.2 * w0, fill=color_space,
                   width=1, outline='#000')

    # вторая ступень
    cv.create_polygon(x - 0.5 * w0, y + h0 + h1, x + 0.5 * w0, y + h0 + h1, x + 0.7 * w0, y + h0 + h1 + h2,
                      x - 0.7 * w0, y + h0 + h1 + h2,
                      fill=color_rocket, width=1, outline='#000')

    # сопла задние
    cv.create_polygon(x - 0.7 * w0, y + h0 + h1 + h2, x + 0.7 * w0, y + h0 + h1 + h2, x + 0.9 * w0,
                      y + h0 + h1 + h2 + h_jet, x - 0.9 * w0, y + h0 + h1 + h2 + h_jet,
                      fill=color_rocket, width=1, outline='#000')

    # сопло переднее
    cv.create_polygon(x - 0.25 * w0, y + h0 + h1 + h2, x + 0.25 * w0, y + h0 + h1 + h2, x + 0.4 * w0,
                      y + h0 + h1 + h2 + 1.05 * h_jet,
                      x - 0.4 * w0, y + h0 + h1 + h2 + 1.05 * h_jet, fill=color_rocket, width=1, outline='#000')



color_rocket = '#FFF8DC'
color_space = '#002'
f = color_rocket
b = color_space
window['bg'] = color_space

lbl = Label(window, font=font_size, fg=f, bg=b)
lbl.configure(text='  Давайте нарисуем ракету!  ')
lbl.grid(column=0, row=0)

# высота конуса
lbl = Label(window, font=font_size, fg=f, bg=b)
lbl.configure(text='Высота конуса')
lbl.grid(column=0, row=1)

hh0 = Entry(window, width=10)
hh0.grid(column=0, row=2)

# ширина конуса
lbl = Label(window, font=font_size, fg=f, bg=b)
lbl.configure(text='Ширина конуса')
lbl.grid(column=0, row=3)

ww0 = Entry(window, width=10)
ww0.grid(column=0, row=4)

# высота 1 ступени
lbl = Label(window, font=font_size, fg=f, bg=b)
lbl.configure(text='Высота первой ступени')
lbl.grid(column=0, row=5)

hh1 = Entry(window, width=10)
hh1.grid(column=0, row=6)

# высота 2 ступени
lbl = Label(window, font=font_size, fg=f, bg=b)
lbl.configure(text='Высота второй ступени')
lbl.grid(column=0, row=7)

hh2 = Entry(window, width=10)
hh2.grid(column=0, row=8)

# высота сопла
lbl = Label(window, font=font_size, fg=f, bg=b)
lbl.configure(text='Высота сопла')
lbl.grid(column=0, row=9)

hh_jet = Entry(window, width=10)
hh_jet.grid(column=0, row=10)

# # цвет ракеты
# lbl = Label(window, font=font_size, fg=f, bg=b)
# lbl.configure(text='Цвет ракеты')
# lbl.grid(column=0, row=1)
#
# color_rocket = Entry(window, width=10)
# color_rocket.grid(column=0, row=12)
#
# #цвет космоса
# lbl = Label(window, font=font_size, fg=f, bg=b)
# lbl.configure(text='Цвет космоса')
# lbl.grid(column=0, row=13)
#
# color_space = Entry(window, width=10)
# color_space.grid(column=0, row=14)
#
#
btn = Button(window, text='Рисуем ракету', bg='#f0f', fg='#000', command=rocket)
btn.grid(column=0, row=11)

cv = Canvas(window, width=w_canvas, height=h_canvas, bg=color_space)  # лист
cv.grid(column=1, row=0, rowspan=12)



window.mainloop()
