from tkinter import *

window = Tk()


def do_something(event) -> None:                            # Funcja musi przyjmować argument event!
    print("You did a thing by pressing: " + event.keysym)   # event.keysym to aktualnie użyty klawisz
    label.config(text=event.keysym)


window.bind("<Key>", do_something)                          # bind daje możliwość podaia "<klawisza>" który będzie coś robił, gdy wpisze Key to dowolny
                                                            # aktywuje funkcje, a gdy Return to tylko enter. Reszta działa normalnie np.w,s,a,d.
label = Label(window, font=("Helvetica", 100), text="")     # To po prostu wyświetla aktualnie użyty klawisz
label.pack()

window.mainloop()
