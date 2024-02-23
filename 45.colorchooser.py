from tkinter import *
from tkinter import colorchooser

window = Tk()                           # colorchooser to możliwość wyboru koloru przez użytkownika

def color():
    color = colorchooser.askcolor()                     # otwiera okno wyboru koloru i przypisuje wybrany kolor do zmiennje 'color'
    # print(color)                                      # Wszystkie wartosci koloru
    # print(color[1])                                   # wybrany kolor w wartoci hex
    # window.config(bg=color[1])                        # ustawiamy wybrany kolor jako kolor tła

    window.config(bg=colorchooser.askcolor()[1])        # Można to zrobić w jednej linicje

colorchoose = Button(window,
                     text="click me",
                     command=color)

window.geometry("420x420")
colorchoose.pack()
window.mainloop()
