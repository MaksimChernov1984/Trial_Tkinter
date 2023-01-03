# код, написанный для изучения библиотеки tkinter
from tkinter import *


# окно
window = Tk()
window.title('Пропорция выгоды')
window.geometry('600x400')
window['bg'] = '#2F4F4F'

x = 10  # отступ по х
y = 10  # отступ по у


# вычисление пропорции выгоды
def clicked():
    p1 = int(price1.get())
    p2 = int(price2.get())
    m1 = int(mass1.get())
    m2 = int(mass2.get())
    if p1 / m1 < p2 / m2:
        res = 'Первый товар выгоднее.'
    elif p1 / m1 > p2 / m2:
        res = 'Второй товар выгоднее.'
    else:
        res = 'Без разницы.'
    resume.config(text=res)


# Заголовок
lbl = Label(window, text='   Какой товар выгоднее?', font=16, fg='#fff', bg='#2F4F4F')
lbl.grid(columnspan=1+2, row=0, padx=x, pady=y)

# надпись Цена товара №1
lbl = Label(window, text=' Цена товара №1 ', font=16, fg='#fff', bg='#2F4F4F')
lbl.grid(column=0, row=1, padx=x, pady=y)

# надпись Цена товара №2
lbl = Label(window, text=' Цена товара №2 ', font=16, fg='#fff', bg='#2F4F4F')
lbl.grid(column=1, row=1, padx=x, pady=y)

# ввод текста Цена товара №1
price1 = Entry(window, width=30)
price1.grid(column=0, row=2, padx=x, pady=y)
price1.focus()

# ввод текста Цена товара №2
price2 = Entry(window, width=30)
price2.grid(column=1, row=2, padx=x, pady=y)

# надпись Масса товара №1
lbl = Label(window, text=' Масса товара №1 ', font=16, fg='#fff', bg='#2F4F4F')
lbl.grid(column=0, row=3, padx=x, pady=y)

# надпись Масса товара №2
lbl = Label(window, text=' Масса товара №2 ', font=16, fg='#fff', bg='#2F4F4F')
lbl.grid(column=1, row=3, padx=x, pady=y)

# ввод текста Масса товара №1
mass1 = Entry(window, width=30)
mass1.grid(column=0, row=4, padx=x, pady=y)

# ввод текста Масса товара №2
mass2 = Entry(window, width=30)
mass2.grid(column=1, row=4, padx=x, pady=y)

# кнопка Проверить
btn_check = Button(window, text='Проверить', bg='#CD5C5C', fg='#fff', command=clicked)
btn_check.grid(columnspan=1+2, row=5, padx=x, pady=y)

# вывод по пропорции
resume = Label(window)
resume.configure(text='Выгоднее купить товар номер...', font='16', fg='#fff', bg='#2F4F4F')
resume.grid(column=0, row=6, padx=x, pady=y)

# кнопка Выход
btn_exit = Button(window, text="Выход", command=window.destroy)
btn_exit.grid(columnspan=1+2, row=7, padx=x, pady=y)

window.mainloop()
