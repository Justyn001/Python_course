from tkinter import *

window = Tk()

label = Label(window, width=18, height=8, bg="red")
label2 = Label(window, width=18, height=8, bg="green")


def start_function(event):                      # gdyby tej linijki na dole nie było to pozsałe dwie by wyglądały tak: label.pozycja_klikn..._x = event.x
    widget = event.widget                       # ta linijka jest po to żeby ta funckja mogła wywoływać się z kazdym labelem a nie tylko jednym konkretnym
    widget.pozycja_klikniecia_x = event.x       # Zbiera pozycje kliknięcia (czyli który obiekt klikneliśmy) a potem przypisuje ją do zmiennej widget.pozycja_klikn...
    widget.pozycja_klikniecia_y = event.y       # Adekwatnie tylko dla y


def move_function(event):
    widget = event.widget
    x = widget.winfo_x() - widget.pozycja_klikniecia_x + event.x        # widget.winfo_x() to współrzędne labela w lewym górnym rogu
    y = widget.winfo_y() - widget.pozycja_klikniecia_y + event.y        # widget.pozycja_klikniecia to współrzędne gdzie kliknelismy
    widget.place(x=x, y=y)                                              # a event.y to chyba gdzie opuściliśmy ten label


label.bind("<Button-1>", start_function)        # label to pierwszy obiekt
label.bind("<B1-Motion>", move_function)        # B1-Motion wywołuje funkcję po tym jak ruszę kolcek dopiero

label2.bind("<Button-1>", start_function)       # label 2 to drugi obiekt
label2.bind("<B1-Motion>", move_function)

label.place(x=0, y=0)
label2.place(x=100, y=200)
window.mainloop()
