from tkinter import *
from buttons import btns
from calculate import calcu


# Settings
window = Tk()
window.title("CALCUMATE v.1.0.0")
window.resizable(width=FALSE, height=FALSE)

# Window Border
windowCover = Frame(window, bd=15, pady=2, bg='light green', relief=RIDGE)
windowCover.grid()
windowCoverMid = Frame(windowCover, bd=10, pady=2, bg='green', relief=RIDGE)
windowCoverMid.grid()
windowCoverInner = Frame(windowCoverMid, bd=10, pady=2, relief=RIDGE)
windowCoverInner.grid()

# LED Display
display = StringVar()
OutputTray = Entry(windowCoverInner, textvariable=display, font=('century gothic', 32, 'bold'),
                   bg='light yellow', fg='black', bd=15, width=17, justify='right')
OutputTray.grid(row=0, column=0, columnspan=4, pady=1)
display.set('0')

# Keypad and Commands
n = OutputTray.get()
numpad = '789456123'
x = 0
nb = []
for y in range(3, 6):
    for z in range(3):
        nb.append(btns().numbuttons(windowCoverInner, 'light green', 'black', 1, numpad[x]))
        nb[x].grid(row=y, column=z, pady=1)
        nb[x]['command'] = lambda i=numpad[x]: display.set(i)
        x += 1
n0 = btns().numbuttons(windowCoverInner, 'light green', 'black', 1, 0).grid(row=6, column=1, pady=1)
dotBtn = btns().numbuttons(windowCoverInner, 'light green', 'black', 1, '.').grid(row=6, column=0, pady=1)
eqlsBtn = btns().numbuttons(windowCoverInner, 'cyan', 'black', 1, '=').grid(row=6, column=2, pady=1)
clearBtn = btns().numbuttons(windowCoverInner, 'white', 'black', 1, 'C').grid(row=1, column=1, pady=1)
clearAllBtn = btns().numbuttons(windowCoverInner, 'black', 'white', 1, 'CE').grid(row=1, column=0, pady=1)
delBtn = btns().numbuttons(windowCoverInner, 'yellow', 'black', 1, '').grid(row=1, column=2, pady=1)
plusBtn = btns().numbuttons(windowCoverInner, 'red', 'white', 3, '+').grid(row=5, column=3, rowspan=2, pady=1)
minusBtn = btns().numbuttons(windowCoverInner, 'green', 'black', 1, '-').grid(row=4, column=3, pady=1)
timesBtn = btns().numbuttons(windowCoverInner, 'green', 'black', 1, 'x').grid(row=3, column=3, pady=1)
divideBtn = btns().numbuttons(windowCoverInner, 'green', 'black', 1, '/').grid(row=1, column=3, pady=1)

window.mainloop()
