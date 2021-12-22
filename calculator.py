import tkinter as tk
from tkinter import messagebox


def add_digit(digit):
    value = calc.get()
    if value[0] == '0' and len(value)==1:
        value = value[1:]
    calc.delete(0, tk.END)
    calc.insert(0, value + digit)


def add_operation(operation):
    value = calc.get()
    if value[-1] in '+-*/':
        value = value[:-1]
   #elif '+' in value or '-' in value or '*' in value or '/' in value:
        #calculate()
        #value = calc.get()
    calc.delete(0, tk.END)
    calc.insert(0, value + operation)

def add_scobka(operation):
    value = calc.get()
    if value[0] == '0' and len(value) == 1:
        value = value[1:]
    calc.delete(0, tk.END)
    calc.insert(0, value + operation)

def m_button():
    global m
    m = 0
    value = int(calc.get())
    m = value
    c()

def mr_button():
    value = calc.get()
    if value[-1] in '1234567890':
        calc.delete(0, tk.END)
    calc.insert(len(calc.get()), m)

def make_digit_button(digit):
    return tk.Button(text=digit, bd=5, font=('Arial', 15), command=lambda: add_digit(digit))

def make_m_button(operation):
    return tk.Button(text=operation, bd=5, font=('Arial', 15), command=lambda: m_button())

def make_mr_button(operation):
    return tk.Button(text=operation, bd=5, font=('Arial', 15), command=lambda: mr_button())

def make_operation_button(operation):
    return tk.Button(text=operation, bd=5, font=('Arial', 15), fg='red',
                     command=lambda: add_operation(operation))

def make_scobka_button(operation):
    return tk.Button(text=operation, bd=5, font=('Arial', 15), fg='red',
                     command=lambda: add_scobka(operation))

def calculate():
    value = calc.get()
    if value[-1] in '+-*/':
        operation = value[-1]
        value=value[:-1]+operation+value[:-1]
    calc.delete(0, tk.END)
    try:
        calc.insert(0, eval(value))
    except (NameError, SyntaxError):
        messagebox.showinfo('Внимание', "Нужно вводить только цифры!")
        calc.insert(0,0)
    except ZeroDivisionError:
        messagebox.showinfo("Внимание", "На ноль делить нельзя!")

def make_calc_button(operation):
    return tk.Button(text=operation, bd=5, font=('Arial', 15), fg='red',
                     command=calculate)


def make_c_button(operation):
    return tk.Button(text=operation, bd=5, font=('Arial', 15), fg='red',
                     command=c)


def c():
    calc.delete(0, tk.END)
    calc.insert(0,0)

def press_key(event):
    print(repr(event.char)) #отследить, какая кнопка была нажата
    if event.char.isdigit():
        add_digit(event.char)
    elif event.char in '+-*/':
        add_operation(event.char)
    elif event.char=='\r':
        calculate()

win = tk.Tk()
win.geometry(f'240x340+100+200')
win['bg'] = '#33ffe6'
win.title("Калькулятор")

win.bind('<Key>', press_key)

calc = tk.Entry(win, justify=tk.RIGHT, font=('Arial', 15), width=15)
calc.insert(0, '0')
calc.grid(row=0, column=0, columnspan=4, stick='we', padx=5, pady=5)
make_digit_button('1').grid(row=1, column=0, stick='swen', padx=5, pady=5)  # bd- толщина границы кнопки
make_digit_button('2').grid(row=1, column=1, stick='swen', padx=5, pady=5)
make_digit_button('3').grid(row=1, column=2, stick='swen', padx=5, pady=5)
make_digit_button('4').grid(row=2, column=0, stick='swen', padx=5, pady=5)
make_digit_button('5').grid(row=2, column=1, stick='swen', padx=5, pady=5)
make_digit_button('6').grid(row=2, column=2, stick='swen', padx=5, pady=5)
make_digit_button('7').grid(row=3, column=0, stick='swen', padx=5, pady=5)
make_digit_button('8').grid(row=3, column=1, stick='swen', padx=5, pady=5)
make_digit_button('9').grid(row=3, column=2, stick='swen', padx=5, pady=5)
make_digit_button('0').grid(row=4, column=0, stick='swen', padx=5, pady=5)

win.grid_columnconfigure(0, minsize=60)
win.grid_columnconfigure(1, minsize=60)
win.grid_columnconfigure(2, minsize=60)
win.grid_columnconfigure(3, minsize=60)

win.grid_rowconfigure(1, minsize=60)
win.grid_rowconfigure(2, minsize=60)
win.grid_rowconfigure(3, minsize=60)
win.grid_rowconfigure(4, minsize=60)

make_operation_button('+').grid(row=1, column=3, stick='swen', padx=5, pady=5)
make_operation_button('-').grid(row=2, column=3, stick='swen', padx=5, pady=5)
make_operation_button('*').grid(row=3, column=3, stick='swen', padx=5, pady=5)
make_operation_button('/').grid(row=4, column=3, stick='swen', padx=5, pady=5)

make_calc_button('=').grid(row=4, column=2, stick='swen', padx=5, pady=5)

make_c_button('c').grid(row=4, column=1, stick='swen', padx=5, pady=5)

make_scobka_button('(').grid(row=5, column=0, stick='swen', padx=5, pady=5)
make_scobka_button(')').grid(row=5, column=1, stick='swen', padx=5, pady=5)
make_m_button('М+').grid(row=5, column=2, stick='swen', padx=5, pady=5)
make_mr_button('М').grid(row=5, column=3, stick='swen', padx=5, pady=5)
'''make_mc_button('М').grid(row=5, column=3, stick='swen', padx=5, pady=5)'''

win.mainloop()
