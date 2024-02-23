from tkinter import *
from tkinter import filedialog


window = Tk()


def click() -> None:
    filepath = filedialog.askopenfilename()                         # Otwiera okno z wyborem pliku (jakbyś chciał oddać doxygena na platformie)
    print(filepath)                                                 # Zwraca scieżkę do tego pliku D:/testfile.txt ( jest to string)
    file = open(filepath, "r")                                      # Otwiera plik w trybie r - read
    print(file.read())                                              # Zczytuje cały plik
    file.close()                                                    # Zamyka plik
    #filepath = filedialog.askopenfilename(initialdir="D:\\Repozytoria\\PycharmProjects",    # To działa tak samo jak ta wersja u góry tylko dajemy ścieżkę gdzie ma się otworzyć okno w wyborem pliku
    #                                      title="open file ok?",                             # Tytuł okna ( w lewym górnym rogu)
    #                                      filetypes=(("text files","*.txt"),("all files","*.*")),  # Ramka w prawym dolnym rogu określa jakiego typu pliki mają być widoczne
    #                                      )

button = Button(text="click me", command=click)

button.pack()
window.mainloop()
