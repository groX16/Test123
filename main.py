from tkinter import *
from tkinter import messagebox

# TODO: ponowne wykorzystanie
# TODO: (opcjonalnie) historia kalkulacji
# 1 - dodawanie
# 2 - odejmowanie
# 3 - mnożenie
# 4 - dzielenie
number1s = ''
number2s = ''

global seloperation
seloperation = 0
global operation
operation = 0
global screen
screen = 0

number1 = []
number2 = []


def show():
    global number1s
    global number2s

    if seloperation == 0:
        number1s = ''
        for i in range(len(number1)):
            number1s = number1s + str(number1[i])
        screen = number1s
        lab1.config(text=screen)
    else:
        number2s = ''
        for i in range(len(number2)):
            number2s = number2s + str(number2[i])
        screen = number2s
        lab1.config(text=screen)
    print(number1s, number2s, number1, number2)


def licz():
    # print(number1s)
    # print(number2s)
    global wynik
    # int(number1s)
    # int(number2s)
    if operation == 1:
        wynik = int(number1s) + int(number2s)
        lab1.config(text=wynik)
    elif operation == 2:
        wynik = int(number1s) - int(number2s)
        lab1.config(text=wynik)
    elif operation == 3:
        wynik = int(number1s) * int(number2s)
        lab1.config(text=wynik)
    elif operation == 4:
        wynik = int(number1s) / int(number2s)
        lab1.config(text=wynik)
    else:
        messagebox.showerror('Bląd', 'Na porach roku się nie znasz!!!')

    clear_equal()


def add():
    show()
    global operation
    global seloperation
    if seloperation != 0:
        licz()
        clear_equal()
    operation = 1
    seloperation = 1


def sub():
    show()
    global operation
    global seloperation
    if seloperation != 0:
        licz()
        clear_equal()
    operation = 2
    seloperation = 1


def mul():
    show()
    global operation
    global seloperation
    if seloperation != 0:
        licz()
        clear_equal()
    operation = 3
    seloperation = 1


def div():
    show()
    global operation
    global seloperation
    if seloperation != 0:
        licz()
        clear_equal()
    operation = 4
    seloperation = 1


def Button0():
    if seloperation == 0:
        number1.append(0)
    else:
        number2.append(0)
    show()


def Button1():
    if seloperation == 0:
        number1.append(1)
    else:
        number2.append(1)
    show()


def Button2():
    if seloperation == 0:
        number1.append(2)
    else:
        number2.append(2)
    show()


def Button3():
    if seloperation == 0:
        number1.append(3)
    else:
        number2.append(3)
    show()


def Button4():
    if seloperation == 0:
        number1.append(4)
    else:
        number2.append(4)
    show()


def Button5():
    if seloperation == 0:
        number1.append(5)
    else:
        number2.append(5)
    show()


def Button6():
    if seloperation == 0:
        number1.append(6)
    else:
        number2.append(6)
    show()


def Button7():
    if seloperation == 0:
        number1.append(7)
    else:
        number2.append(7)
    show()


def Button8():
    if seloperation == 0:
        number1.append(8)
    else:
        number2.append(8)
    show()


def Button9():
    if seloperation == 0:
        number1.append(9)
    else:
        number2.append(9)
    show()


def clear():
    global screen
    global seloperation
    global operation
    global number1s
    global number2s

    number1s = ''
    number2s = ''
    screen = 0
    seloperation = 0
    operation = 0
    for i in range(len(number1)):
        del (number1[0])
    for i in range(len(number2)):
        del (number2[0])
    print(number1, number2)
    lab1.config(text=screen)


def clear_equal():
    global screen
    global seloperation
    global operation
    global number1s
    global number2s
    global number1

    number1s = wynik
    number2s = ''
    screen = 0
    seloperation = 1
    operation = 0

    for i in range(len(number2)):
        del (number2[0])


root = Tk()
root.resizable(width=False, height=False)
# root.geometry('600x400')
Title = Label(root, text='Kalkulator', font=30)
Title.grid(row=0, column=0, sticky=N)

frame = Frame(root, borderwidth=4)
frame.grid(row=1, column=0, sticky=N)
frame.config(background='black')

lab1 = Label(frame, text=0, font=30, bg='green', fg='white')
lab1.grid(sticky=N, row=0, column=0, padx=5, pady=5, )
lab1.config(text=str(screen))

frame1 = Frame(root, borderwidth=4)
frame1.grid(row=2, column=0, sticky=N)
frame1.config(background='black')

Button0 = Button(frame1, text='0', font=30, command=Button0)
Button0.grid(row=3, column=0, sticky=N)

Button1 = Button(frame1, text='1', font=30, command=Button1)
Button1.grid(row=2, column=2, sticky=N)

Button2 = Button(frame1, text='2', font=30, command=Button2)
Button2.grid(row=2, column=1, sticky=N)

Button3 = Button(frame1, text='3', font=30, command=Button3)
Button3.grid(row=2, column=0, sticky=N)

Button4 = Button(frame1, text='4', font=30, command=Button4)
Button4.grid(row=1, column=2, sticky=N)

Button5 = Button(frame1, text='5', font=30, command=Button5)
Button5.grid(row=1, column=1, sticky=N)

Button6 = Button(frame1, text='6', font=30, command=Button6)
Button6.grid(row=1, column=0, sticky=N)

Button7 = Button(frame1, text='7', font=30, command=Button7)
Button7.grid(row=0, column=2, sticky=N)

Button8 = Button(frame1, text='8', font=30, command=Button8)
Button8.grid(row=0, column=1, sticky=N)

Button9 = Button(frame1, text='9', font=30, command=Button9)
Button9.grid(row=0, column=0, sticky=N)

Button_Add = Button(frame1, text='+', font=30, command=add)
Button_Add.grid(row=0, column=3, sticky=N)

Button_Sub = Button(frame1, text='-', font=30, command=sub)
Button_Sub.grid(row=1, column=3, sticky=N)

Button_Mul = Button(frame1, text='*', font=30, command=mul)
Button_Mul.grid(row=2, column=3, sticky=N)

Button_Div = Button(frame1, text='/', font=30, command=div)
Button_Div.grid(row=3, column=3, sticky=N)

Button_equal = Button(frame1, text='=', font=30, command=licz)
Button_equal.grid(row=3, column=2, sticky=N)

Button_clear = Button(frame1, text='C', font=30, command=clear)
Button_clear.grid(row=3, column=1, sticky=N)

# root.

root.mainloop()
