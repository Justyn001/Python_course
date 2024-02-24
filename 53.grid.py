from tkinter import *

                                    # grid to tabelka zaczynająca się od 0,0 row to wiersz a column to kolumna

window = Tk()

Label(window, text="First name: ", bg="red").grid(row=1, column=0)            # Dodaje label w 0 wierszu i 0 kolumnie
Entry(window).grid(row=1, column=1)                                           # Dodaje entry(pole do wpisywania) w 0 wierszu i 1 kolumnie

Label(window, text="Last name: ").grid(row=2, column=0)
Entry(window).grid(row=2, column=1)

Label(window, text="Email", width=20, bg="pink").grid(row=3, column=0)
Entry(window).grid(row=3, column=1)

Button(window, text="Submit").grid(row=4, column=0, columnspan=2)       # columnspan - ustawia po środku 2 kolumn(zaczynąc od ustawionej kolumny w tym przypadku zerowej)

Label(window, text="Enter your info ", font=("arial", 30)).grid(row=0, column=0, columnspan=2)

window.mainloop()
                        # No i kolumny i wiersze ustawiają swój rozmiar na podstawie największej kolumny lub wiersza