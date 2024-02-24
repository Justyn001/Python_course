from tkinter import *
from tkinter import ttk

window = Tk()

notebook = ttk.Notebook(window)     # Tworze w oknie(window) nowy notatnik

tab1 = Frame(notebook)              # Tworze w notatniku(notebook) dwa framy(ramki)
tab2 = Frame(notebook)

notebook.add(tab1, text="tab1")     # Dodaje do notatnika te ramki i nazywam je tab1 i tab2
notebook.add(tab2, text="tab2")

notebook.pack(expand=False, fill="both")   # expand zwiększa rozmiar tabelek dostowując je do rozszerzania i zmniejsania ekranu
                                           # fill zajmuje takie samo miejsc na osi x i y(zamiast both mogło być tylko x i tylko y)

                                                                            # label - to obszar w którym wyświetla się tekst i/lub obraz
Label(tab1, text="Welcome, you're on tab1.", width=50, height=20).pack()    # dodaje to tab1 i tab2 label z napisem o rozmiarze 50 na 20
Label(tab2, text="Hello, you're on tab2.", width=50, height=20).pack()
window.mainloop()
