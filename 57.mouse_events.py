from tkinter import *

window = Tk()


def do_something(event) -> None:
    print("You clicked a button " + str(event.x) + ", " + str(event.y))     # event.x to współrzędne x a event.y to współrzędne y


#window.bind("<Button-1>", do_something)                # Button-1 to lewy przycisk
#window.bind("<Button-2>", do_something)                # Button-2 to scrol
#window.bind("<Button-3>", do_something)                # Button-3 to prawy przycisk
#window.bind("<ButtonRelease>", do_something)           # ButtonRelease zadziała wtedy gdy puszcze przycisk (dowlnie który)
#window.bind("<Enter>", do_something)                   # Enter wykona funkcję dopiero gdy myszka wjedzie na okno(window)
#window.bind("<Leave>",do_something)                    # Leave wykona funkcję dopiero gdy myszka wyjedzie poza okno(window)
window.bind("<Motion>", do_something)                   # Wykonuje cały czas funkcję jak tylko myszka jest w oknie

window.mainloop()
