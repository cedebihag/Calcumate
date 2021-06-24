from tkinter import *


class btns:
    @staticmethod
    def numbuttons(source, bg, fg, h, text):
        numb = Button(source, width=4, height=h, font=('century gothic', 24, 'bold'),
                      bg=bg, fg=fg, bd=10, text=text)
        return numb

    pass
