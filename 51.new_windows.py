from tkinter import *

window = Tk()


def make_window() -> None:
    new_window = Toplevel()         # Toplevel() - otwiera nowe okno ale gdy stare zostanie zamkniętę to również się zamyka
    #new_window = Tk()               # Tk() - otiwera nowe okno ale gdy stare zostanie zamknięte to pozostaje same(nie zamyka się)


Button(window, text="New window", command=make_window).pack()
window.mainloop()
