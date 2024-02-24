from tkinter import *

window = Tk()

                                    # menubar to pasek zadań u góry ekranu

menubar = Menu(window)              # Tworzy pasek zadań
window.config(menu=menubar)         # Dodaje stworzony pasek zadań do okna(window)


def open_() -> None:
    print("You open a file.")


def save() -> None:
    print("You save a file.")


def cut() -> None:
    print("You cut something.")


def copy() -> None:
    print("You copy something")


def past() -> None:
    print("You paste something")


photoOne = PhotoImage(file="mammon.png")
photoTwo = PhotoImage(file="cold.png")
photoThree = PhotoImage(file="omegalul.png")

fileMenu = Menu(menubar, tearoff=0, font=("arial", 10))                             # Tworzy pasek zadań w pasku zadań
menubar.add_cascade(label="File", menu=fileMenu)                                    # Tworzy jedną "opcje" w pasku zadań o nazwie "File"
fileMenu.add_command(label="Open", command=open_, image=photoOne, compound="left")  # Dodaje opcje do rozwijającego się paska zdań(opcja "open")
fileMenu.add_command(label="Save", command=save, image=photoTwo, compound="left")   # Dodaje opcje do rozwijającego się paska zdań(opcja "save")
fileMenu.add_separator()                                                            # Dodaje separtator pomiędzy opcjami u góry a tymi na dole
fileMenu.add_command(label="Exit", command=quit, image=photoThree, compound="left") # Dodaje opcje do rozwijającego się paska zdań(opcja "exit")

editMenu = Menu(menubar, tearoff=0, font=("arial", 10))                           # Tworzy drugą "opcje" w pasku zadań o nazwie "File"
menubar.add_cascade(label="Edit", menu=editMenu)
editMenu.add_command(label="Cut", command=cut)
editMenu.add_command(label="Copy", command=copy)
editMenu.add_command(label="Past", command=past)

window.mainloop()
