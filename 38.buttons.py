from tkinter import *

window = Tk()

active: int = 0

def action():
    global active
    active += 1
    print("You clicked the button {} times.".format(active))


photo = PhotoImage(file='mammon.png')

button = Button(window,
                text="click me!",
                command=action,            # Co się dzieje po wciśnięciu(wykonuje funkcje action po wciśnięciu)
                font=("Algerian",30),
                fg="green",
                bg="black",
                activeforeground="black",  # Jaki kolor czionki będzie w trakcie naciskania przycisku
                activebackground="yellow", # Jaki kolor tła będzie podczas naciskania przycisku
                state=ACTIVE,              # Przycisk włączony (lub DISABLED to wyłączony)
                image=photo,               # Dodanie zdjęcia do przycisku
                compound="bottom",         # Gdzie to zdjęcia ma się znajdować(jeśli tego nie będzie to zdjęcie zajmie miejsce tekstu)
                )


button.pack()

window.mainloop()
