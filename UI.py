from tkinter import *
from Memory import memory
from Logics import logic

# Settings
window = Tk()
window.title("CALCUMATE v.1.0.0")
window.resizable(width=FALSE, height=FALSE)

# Window Border
windowCover = Frame(window, bd=15, pady=2, bg='green', relief=RIDGE)
windowCover.grid()
windowCoverMid = Frame(windowCover, bd=10, pady=2, bg='light green', relief=RIDGE)
windowCoverMid.grid()
windowCoverInner = Frame(windowCoverMid, bd=10, pady=2, bg='black', relief=RIDGE)
windowCoverInner.grid(row=0, column=0, columnspan=4)

# Display
display1 = StringVar()
display2 = StringVar()
display3 = StringVar()
display = StringVar()
N1 = Label(windowCoverInner, textvariable=display1, font=('century gothic', 32, 'bold'), bg='light yellow', bd=15,
           width=14, anchor=E).grid(row=1, column=0, columnspan=4, pady=1)
N2 = Label(windowCoverInner, textvariable=display2, font=('century gothic', 24, 'bold'), bg='light yellow', bd=15,
           width=15, anchor=E).grid(row=0, column=2, columnspan=3, pady=1)
OP = Label(windowCoverInner, textvariable=display3, font=('century gothic', 24, 'bold'), bg='light yellow', bd=15,
           width=2).grid(row=0, column=0, columnspan=1, pady=1)
display1.set(memory.dis1)
display2.set(memory.n2)
display3.set(memory.operator)


def inputV(x):
    if memory.result is True:
        memory.result = False
        if x == '.':
            display1.set('0' + x)
        else:
            display1.set(x)
    else:
        if x == '.':
            if x in display1.get():
                return
            else:
                y = display1.get() + x
                display1.set(y)
        else:
            if display1.get() == '0':
                display1.set(x)
            else:
                y = display1.get() + x
                display1.set(y)
    memory.input = False


def operation(x):
    if memory.input is False:
        memory.dis1 = display1.get()
        display2.set(memory.dis1)
        display1.set('')
        memory.input = True
    memory.operator = x
    display3.set(memory.operator)


def solving(x):
    memory.n1 = float(memory.dis1)
    memory.n2 = float(display1.get())
    if memory.n2 % 1 == 0:
        display2.set(format(memory.n2, ',g'))
    else:
        display2.set(format(memory.n2, ',g'))
    logic.solve(memory.operator)

    if memory.answer == 'invalid':
        display2.set('invalid')
        display1.set('0')
    else:
        if memory.answer % 1 == 0:
            display1.set(format(memory.answer, ',g'))
        else:
            display1.set(format(memory.answer, ',g'))
    memory.result = True
    memory.input = False


def dlt():
    x = display1.get()
    y = len(x)
    display1.set(x[:y - 1])


def clr():
    display1.set('0')


def clrall():
    logic.ca()
    display1.set(memory.dis1)
    display2.set(memory.n2)
    display3.set(memory.operator)


# Keypad and Commands
b1 = Button(windowCoverMid, width=4, height=1, font=('century gothic', 24, 'bold'), bg='light yellow', bd=10, text='1',
            command=lambda i='1': inputV(i)).grid(row=5, column=0, pady=1)
b2 = Button(windowCoverMid, width=4, height=1, font=('century gothic', 24, 'bold'), bg='light yellow', bd=10, text='2',
            command=lambda i='2': inputV(i)).grid(row=5, column=1, pady=1)
b3 = Button(windowCoverMid, width=4, height=1, font=('century gothic', 24, 'bold'), bg='light yellow', bd=10, text='3',
            command=lambda i='3': inputV(i)).grid(row=5, column=2, pady=1)
b4 = Button(windowCoverMid, width=4, height=1, font=('century gothic', 24, 'bold'), bg='light yellow', bd=10, text='4',
            command=lambda i='4': inputV(i)).grid(row=4, column=0, pady=1)
b5 = Button(windowCoverMid, width=4, height=1, font=('century gothic', 24, 'bold'), bg='light yellow', bd=10, text='5',
            command=lambda i='5': inputV(i)).grid(row=4, column=1, pady=1)
b6 = Button(windowCoverMid, width=4, height=1, font=('century gothic', 24, 'bold'), bg='light yellow', bd=10, text='6',
            command=lambda i='6': inputV(i)).grid(row=4, column=2, pady=1)
b7 = Button(windowCoverMid, width=4, height=1, font=('century gothic', 24, 'bold'), bg='light yellow', bd=10, text='7',
            command=lambda i='7': inputV(i)).grid(row=3, column=0, pady=1)
b8 = Button(windowCoverMid, width=4, height=1, font=('century gothic', 24, 'bold'), bg='light yellow', bd=10, text='8',
            command=lambda i='8': inputV(i)).grid(row=3, column=1, pady=1)
b9 = Button(windowCoverMid, width=4, height=1, font=('century gothic', 24, 'bold'), bg='light yellow', bd=10, text='9',
            command=lambda i='9': inputV(i)).grid(row=3, column=2, pady=1)
n0 = Button(windowCoverMid, width=4, height=1, font=('century gothic', 24, 'bold'), bg='light yellow', bd=10, text='0',
            command=lambda i='0': inputV(i)).grid(row=6, column=1, pady=1)
DotBtn = Button(windowCoverMid, width=4, height=1, font=('century gothic', 24, 'bold'), bg='light yellow', bd=10,
                text='.', command=lambda i='.': inputV(i)).grid(row=6, column=0, pady=1)

# Functions
EqlsBtn = Button(windowCoverMid, width=4, height=1, font=('century gothic', 24, 'bold'), bg='cyan', bd=10,
                 text='=', command=lambda: solving(1)).grid(row=6, column=2, pady=1)
CLearAllBtn = Button(windowCoverMid, width=4, height=1, font=('century gothic', 24, 'bold'), bg='black', fg='white',
                     bd=10, text='CE', command=lambda: clrall()).grid(row=1, column=0, pady=1)
ClearBtn = Button(windowCoverMid, width=4, height=1, font=('century gothic', 24, 'bold'), bd=10, text='C',
                  command=lambda: clr()).grid(row=1, column=1, pady=1)
DelBtn = Button(windowCoverMid, width=4, height=1, font=('century gothic', 24, 'bold'), bg='yellow', bd=10,
                text='', command=lambda: dlt()).grid(row=1, column=2, pady=1)

# Operands
divide = Button(windowCoverMid, width=4, height=1, font=('century gothic', 24, 'bold'), bg='green', fg='white', bd=10,
                text='/', command=lambda i='/': operation(i)).grid(row=1, column=3, pady=1)
multiply = Button(windowCoverMid, width=4, height=1, font=('century gothic', 24, 'bold'), bg='green', fg='white', bd=10,
                  text='x', command=lambda i='x': operation(i)).grid(row=3, column=3, pady=1)
minus = Button(windowCoverMid, width=4, height=1, font=('century gothic', 24, 'bold'), bg='green', fg='white', bd=10,
               text='-', command=lambda i='-': operation(i)).grid(row=4, column=3, pady=1)
plus = Button(windowCoverMid, width=4, height=3, font=('century gothic', 24, 'bold'), bg='red', fg='white', bd=10,
              text='+', command=lambda i='+': operation(i)).grid(row=5, column=3, rowspan=2, pady=1)

window.mainloop()
