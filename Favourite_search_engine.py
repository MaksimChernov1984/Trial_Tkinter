# код, написанный для изучения библиотеки tkinter
from tkinter import *
from tkinter.ttk import Combobox  # выпадающий список
from tkinter import messagebox  # всплывающее окно


# окно
window = Tk()
window.title('Любимый поисковик')
window.geometry('600x400')
window['bg'] = '#2F4F4F'

x = 10 # отступ по х
y = 10 # отступ по у

# всплывающее окно с вопросом
def clicked_ask(answ):
    answ = messagebox.askquestion('Вопрос', 'Вы любите искать информацию в интернете?')
    if answ == 'yes':
        messagebox.showinfo('Если да', 'Расскажите о своём любимом поисковике!')
    elif answ == 'no':
        messagebox.showinfo('Если нет', 'Наверное, Вы чаще пользуетесь книгами!')

# кнопка Вопрос
btn_ask = Button(window, text="Вопрос", bg='#CD5C5C', fg='#fff', command=clicked_ask)
btn_ask.grid(column=0, row=0, padx=x, pady=y)

# начало текста
lbl = Label(window, text='   Назовите любимый поисковик ', font=16, fg='#fff', bg='#2F4F4F')
lbl.grid(column=0, row=1, padx=x, pady=y)

# выпадающий список
combo = Combobox(window)
combo['values'] = ('(выберите)', 'Google', 'Яндекс', 'Mail.ru', 'Yahoo!', 'Web.de', 'Рамблер')
combo.current(0)
combo.grid(column=1, row=1, padx=x, pady=y)

# надпись
lbl = Label(window, text='   Назовите причину ', font=16, fg='#fff', bg='#2F4F4F')
lbl.grid(column=0, row=2, padx=x, pady=y)

# ввод текста
txt = Entry(window, width=30)
txt.grid(column=1, row=2, padx=x, pady=y)
txt.focus()

# надпись сколько баллов
lbl = Label(window, text='Сколько баллов из 5', font=16, fg='#fff', bg='#2F4F4F')
lbl.grid(column=0, row=3, padx=x, pady=y)

# количество баллов
spin = Spinbox(window, from_=1, to=5, width=5)
spin.grid(column=1, row=3, padx=x, pady=y)

# появляется надпись при клике, и это должно быть перед кнопкой
def clicked(res):
    res = 'Моя любимая поисковая система - ' + combo.get() + ', \nпотому ' \
        'что ' + txt.get() + '. \nКоличество баллов, которые я бы ему дал - ' + spin.get() + '.'
    lbl.configure(text=res, font='16', fg='#fff', bg='#2F4F4F')
    lbl.grid(columnspan=1+2, row=5)

# кнопка Проверить
btn_check = Button(window, text='Проверить', bg='#CD5C5C', fg='#fff', command=clicked)
btn_check.grid(column=0, row=4, padx=x, pady=y)
btn_check.bind('<Return>', clicked)

# кнопка Выход
btn_exit = Button(window, text="Выход", command=window.destroy)
btn_exit.grid(column=0, row=6, padx=x, pady=y)

window.mainloop()