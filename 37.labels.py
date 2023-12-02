from tkinter import *

# label - to obszar w którym wyświetla się tekst i/lub obraz

window = Tk()

photo = PhotoImage(file="mammon.png")                   # W file= można też wpisać tak D:\\Repozytoria\\PycharmProjects\\mammon.png
                                                        #ale nie trzeba, wystarczy dodać to do folderu gdzie mam kod. Wtedy wystarczy file="mammon.png"
label = Label(window,
              text="Niewygodnie mi się siedzi.",              # Tekst wyświetlany na ekranie
              font=("Arial", 100, "bold", "italic"),    # Czcionka, rozmiar, pogrubienie, kursywa
              fg="#ddfdf4",                             # Kolor czcionki
              bg="#d0996a",                             # Kolor tła
              relief=RAISED,                            # Dodaje to ramke wokół tekstu(można też wpisać SUNKEN to będzie trochę inna ramka)
              bd=10,                                    # Rozmiar ramki
              padx=10,                                  # Odstęp na osi x na początku i na końcu
              pady=10,                                  # Odstęp na osi y na górze i na dole
              image=photo,                              # Dodaje zdjęcie do labela
              compound="bottom",                        # Gdzie ma się to zdjęcie pojawić(top,bottom,left,right)
              )

label.pack()                                            # Dodaje label do okna(do window u mnie)
#label.place(x=20, y=120)                               # To też dodaje label do okna ale możesz wybrać kordynaty gdzie będzie ten napis

window.mainloop()
