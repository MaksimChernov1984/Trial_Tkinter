# код, написанный для изучения библиотеки tkinter
from tkinter import *





window = Tk()
window.title('Аутентификация')
window.geometry('600x600')
window['bg'] = '#2F4F4F'

x = 2  # отступы по х
y = 2  # отступы по у



# Регистрация
lbl = Label(window)
lbl.configure(text='Логин', bg='#2F4F4F', fg='#fff')
lbl.grid(column=0, row=0, padx=x, pady=y)

login0 = Entry(window, width=10)
login0.grid(column=1, row=0, stick='w', padx=x, pady=y)
login0.focus()


lbl = Label(window)
lbl.configure(text='Пароль', bg='#2F4F4F', fg='#fff')
lbl.grid(column=0, row=1, padx=x, pady=y)

password0 = Entry(window, width=10, show='*')
password0.grid(column=1, row=1, stick='w', padx=x, pady=y)


lbl = Label(window)
lbl.configure(text='Повторите пароль', bg='#2F4F4F', fg='#fff')
lbl.grid(column=0, row=2, padx=x, pady=y)

password01 = Entry(window, width=10, show='*')
password01.grid(column=1, row=2, stick='w', padx=x, pady=y)


def log_up():
    if password0.get() != password01.get() or password0.get() == '':
        txt_log_up = 'Пароли не совпадают.'
    else:
        txt_log_up = 'Успешно зарегистрировались!'


    lbl = Label(window)
    lbl.configure(text=txt_log_up, bg='#2F4F4F', fg='#fff')
    lbl.grid(column=1, row=3, stick='w')


btn_log_up = Button(window, text='Зарегистрироваться', bg='#DB7093', activebackground='#f0f', fg='#000', command=log_up)
btn_log_up.grid(column=0, row=3)


# промежуток
lbl = Label(window)
lbl.configure(text='*', bg='#2F4F4F', fg='#fff')
lbl.grid(column=0, row=4, padx=x, pady=4*y)


# Аутентификация
lbl = Label(window)
lbl.configure(text='Логин', bg='#2F4F4F', fg='#fff')
lbl.grid(column=0, row=10, padx=x, pady=y)

login1 = Entry(window, width=10)
login1.grid(column=1, row=10, stick='w', padx=x, pady=y)


lbl = Label(window)
lbl.configure(text='Пароль', bg='#2F4F4F', fg='#fff')
lbl.grid(column=0, row=11, padx=x, pady=y)

password1 = Entry(window, width=10, show='*')
password1.grid(column=1, row=11, stick='w', padx=x, pady=y)


def log_in():
    if login0.get() == login1.get() and password0.get() == password1.get():
        txt_log_in = 'Добро пожаловать!'
    else:
        txt_log_in = 'Логин и/или пароль не совпадают.'


    lbl = Label(window)
    lbl.configure(text=txt_log_in, bg='#2F4F4F', fg='#fff')
    lbl.grid(column=1, row=12, stick='w')

btn_log_up = Button(window, text='Войти', bg='#DB7093', activebackground='#f0f', fg='#000', command=log_in)
btn_log_up.grid(column=0, row=12)


window.mainloop()
