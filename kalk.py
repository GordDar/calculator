


def say_hello(): #функция для первой кнопки, создать текст в консоли
    print('hello')
def add_label(): #функция для второй кнопки, создать текст в окне
    label=tk.Label(win, text='new')
    label.pack()

count = 0 #для кнопки "счетчик"
def counter():
    global count
    count +=1
    btn4['text'] =f'Счетчик: {count}'
import tkinter as tk
from tkinter import PhotoImage

win = tk.Tk() #создание окна
# photo = tk.PhotoImage(file='py2.jpg')
# win.iconphoto(False, photo) #настройка иконки приложения в окне
win.config(bg='#EED8D8') #rgb название цвета, bg=background
win.title('Мое первое графическое приложение') #название поля сверху
win.geometry('500x500+400+100') #размеры, расположение+ от верхнего левого угла
win.minsize(300,400) #min размер окна
win.maxsize(700,800) #max размер окна
win.resizable(True, True) #возможность поменять размер окна(ширина, высота)
'''btn1 = tk.Button(win, text='Hello', command=say_hello)
btn2 = tk.Button(win, text='Add new label', command=add_label)
btn3 = tk.Button(win, text='Add new label lambda',
                 command=lambda: tk.Label(win, text='new lambda').pack()) #аналогично кнопке 2
btn4 = tk.Button(win, text=f'Счетчик: {count}',
                 command=counter, bg='blue', activebackground='red'
                 ) #state=tk.DISABLED - кнопка не активна
btn1.pack()
btn2.pack()
btn3.pack()
btn4.pack()
label1 = tk.Label(win, text='Hello!', bg='red', fg='white', font=('Arial',20, 'bold'),
                  padx=20, pady=20, width=10, height=10, anchor='ne', relief=tk.RAISED, bd=10, justify=tk.RIGHT)
#текст, fg цвет текста, padx отступ от краев по x, width по количеству знаков, anchor привязка текста к north-east
#relief - граница лейбла, bd - ширина границы, justify -выравнивание текста по стороне
label1.pack()'''
'''btn5 = tk.Button(win, text='Hello 1')
btn6 = tk.Button(win, text='Hello 2')
btn7 = tk.Button(win, text='Hello 3')
btn8 = tk.Button(win, text='Hello 4')
btn5.grid(row=0, column=0) #создание таблицы, ряд, колонка
btn6.grid(row=0, column=1)
btn7.grid(row=1, column=0, columnspan=2, stick='we') #кнопка на 2 места, stick - растянуть на west-east
btn8.grid(row=0, column=2, rowspan=2, stick='ns') #объединить По ряду, растянуть на north-south
win.grid_columnconfigure(0, minsize=100) #колонка 0, мин ширина 100'''
'''for i in range(5):
    for j in range(2):
        tk.Button(win, text=f'Hello {i+1} {j}').grid(row=i, column=j, stick='we')
        #создать таблицу 2*5 cо значениями, чтобы i начиналось от 1'''
'''def get_entry(): #получить то, что ввели
    value = name.get()
    if value:
        print(value)
    else:
        print("Empty Entry")
def delete_entry(): #удалить то, что ввели с 0го символа до N либо tk.End, 'end'
    name.delete(0, 'end')
def submit():
    print(name.get()) #получить данные, которые ввели в окне
    print(password.get())
    delete_entry() #вызвали функцию
    password.delete(0, tk.END) #удалить в окне то, что было введено
name = tk.Entry(win)
name.grid(row=0, column=1)
tk.Label(win, text='Имя').grid(row=0, column=0, stick='we')
tk.Button(win, text='get', command=get_entry).grid(row=2, column=0, stick='we')
tk.Button(win, text='delete', command=delete_entry).grid(row=2, column=1, stick='we')
tk.Button(win, text='submit', command=submit).grid(row=3, column=0, stick='we')
tk.Button(win, text='insert', command=lambda: name.insert(0, "hello"))\
    .grid(row=2, column=2, stick='we')
win.grid_columnconfigure(0, minsize=100)
win.grid_columnconfigure(1, minsize=100)
tk.Label(win, text='Пароль').grid(row=1, column=0, stick='we')
password = tk.Entry(win, show='*') #показывать символы, а не то, что вводишь
password.grid(row=1, column=1)'''
'''def select_all(): #команда для кнопки "выбрать все флажки"
    for check in [over_18, commercial, follow]:
        check.select()
def deselect_all(): #команда для кнопки "убрать все флажки"
    for check in [over_18, commercial, follow]:
        check.deselect()
def switch_all(): #команда для кнопки "поменять флажки на обратное значение"
    for check in [over_18, commercial, follow]:
        check.toggle()
def show(): #получить значение по флажку
    print('флажок 18', over_18_value.get())
    print('реклама', commercial_value.get())
over_18_value = tk.StringVar()
over_18_value.set('no') #если не сделать, то при запуске флажок будет сразу отмечен
commercial_value = tk.IntVar() #в значение переменной можно занести только целое число
over_18 = tk.Checkbutton(win, text='Вам исполнилось 18?',
                         variable=over_18_value,
                         offvalue='no',
                         onvalue='yes') #textvariable - связываем значение флажка с переменной
commercial = tk.Checkbutton(win, text='Хотите ли вы подписаться на рекламу?',
                            variable=commercial_value, offvalue=0,
                            onvalue=1)
follow = tk.Checkbutton(win, text='Хотите подписать на канал?',
                        indicatoron=0) #indicatoron - смена варианта флажка
over_18.pack()
commercial.pack()
follow.pack()
tk.Button(win, text='select all', command=select_all).pack()
tk.Button(win, text='deselect all', command=deselect_all).pack()
tk.Button(win, text='switch', command=switch_all).pack()
tk.Button(win, text='show', command=show).pack()'''

from tkinter import ttk
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return f'Point {self.x} {self.y}'

def set_day():
    combo.set('Friday') #или любое значение
def show_day():
    print(combo.get())
weekDays = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Wednesday")
combo = ttk.Combobox(win, values = weekDays) #значения сохраняются в строковом виде
combo.current(0) #по умолчанию в окне выбора сразу стоит значение с индексом 0 - Monday
combo.pack()
combo_point = ttk.Combobox(win, values = [Point(2,5), Point(1,1)])
combo_point.pack()

ttk.Button(win, text="show_day", command=show_day).pack()
ttk.Button(win, text="set_day", command=set_day).pack()


win.mainloop() #запуск окна