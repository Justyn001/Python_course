from tkinter import *

window = Tk()

# Entrybox - to miejsce do wpisywania przez użytkownika jakis danych, np. swój nick, adres itp.
def submit():
    name = entry.get()                      # Zwraca wartość wpisaną do entryboxa nazwanego "entry"
    print("Hello " + name.capitalize())
    entry.config(state=DISABLED)            # Po kliknięciu przycisku submit wpisanie czegokolwiek staje się zablokowane

def delete():
    entry.delete(0, END)                # Po wciśnięciu przycisku usowa wartość od zerowego indesku do końca(END)


def backspace():
    entry.delete(len(entry.get())-1, END)    # Po naciśnięciu przycisku usuwa ostatnią wartość(literę)

entry = Entry(window,
              font=("calibri",50),
              fg="green",
              bg="black",
              show="*",                      # Wpisywane znaki zostaną zasłoniętę przez *, jak przy wpisywaniu hasła
              )

entry.insert(0, "Wpisz tu swój tekst.")     # Pod indeksem zerowym dodajemy wartość która się pojawi

entry.pack(side=LEFT)       # Po której stronie dodajemy entryboxa

button1 = Button(window,
                 text="submit",
                 command=submit,
                 )
button2 = Button(window,
                 text="delete",
                 command=delete,
                 )
button3 = Button(window,
                 text="backspace",
                 command=backspace,
                 )
button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
window.mainloop()
