from tkinter import *

# widgets - elementy interfejsu: przyciski, obrazki
# windows - słuzy jako kontener na widgetsy 

window = Tk()       #Tworzy nowe puste okno
window.title("First GUI app.")      #Tytuł okna
window.geometry("420x420")          #Rozdzielczość
window.config(background="blue")    #Kolor tła

icon = PhotoImage(file='icon.png')  #ikona w prawym górnym rogu(chyba musi być w formacie png bo w jpg mi nie działało)
window.iconphoto(True, icon)    #Przypisanie ikony do okna

window.mainloop()       #Wyświetla okno
