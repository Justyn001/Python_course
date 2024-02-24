from tkinter import *
from tkinter import filedialog

window = Tk()


def save() -> None:
    file = filedialog.asksaveasfile(initialdir="D:\\",                  # Gdzie się ma otwierać okno zapisu
                                    defaultextension=".txt",            # Podstawowy typ pod jakim będzie zapis
                                    filetypes=[("text file", ".txt"),   # Dostępne formy zaopisu - txt
                                               ("html file", ".html"),  # - html
                                               ("all files", ".*"),     # - wszystkie pliki
                                               ])
    if file is None:
        return
    textfile = str(text.get(1.0, END))                           # Bierzę całą wartość pliku text
    #textfile = input("Say something I guess: ")                        # Mozna zapisywac tez z konosli
    file.write(textfile)                                                # Zapisuje cala warotsc pliku textfile do pliku text
    file.close()


text = Text(window)
text.pack(side=BOTTOM)
button = Button(window, text="save", command=save)
button.pack(side=TOP)
window.mainloop()
