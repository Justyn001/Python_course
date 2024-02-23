from tkinter import *


                            # textarea to dosłownie notatnik, użytkownik może wpisywać cokolwiek

window = Tk()

def click():
    input = textarea.get("1.0", END)            # Po naciśnięciu przycisku do zmiennej input zostaje przypisana wartość od początku do końca
    print(input)                                       # początek musi być oznaczony jak "1.0" a koniec jako END
textarea = Text(window,
                width=30,
                height=9,
                font=("Ink Free", 25),
                bg="#e6de97",
                padx=10,
                pady=10,)
button = Button(window, command=click, text="click me")


textarea.pack()
button.pack()
window.mainloop()