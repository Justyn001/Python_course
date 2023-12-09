from tkinter import *

window = Tk()
                                # Skala to taki suwak na którym wybierasz z określonych wartości
scale = Scale(window,
              from_=100,
              to=0,
              length=500,           # Długoś suwaka
              orient=VERTICAL,      # Czy suwak jest poprzeczny czy poziomy( tak: | - VERTICAL czy tak: -- HORIZNOTAL)
              font = ("Arial",30),
              tickinterval=10,      # Podziałak po lewej stronie(co 10)
              showvalue=True,       # Jeśli True to pokazuje akturalnie wybraną wartość jeśli False to nie pokazuje
              resolution=5,         # Co ile można wybrać wartość
              troughcolor="blue",   # Kolor suwaka
              fg="red",
              bg="black",
              )

scale.set((scale["from"] - scale["to"])/2 + scale["to"])        # Ustawia na jakiej wartości ma się pojawić początkowo suwak a funkcja w środku to
                                                                # po prostu matematyczna funckja na wartość środkową

coldimage = PhotoImage(file='cold.png')
coldlabel = Label(image=coldimage)

hotimage = PhotoImage(file='hot.png')
hotlabel = Label(image=hotimage)

def action():
    print("The temperature is {} degrees C".format(scale.get()))

button = Button(window,text='submit',command=action,)

hotlabel.pack()         # Najpierw dodaje ikonke u góry
scale.pack()            # Potem skale
coldlabel.pack()        # potem ikonkę na dole
button.pack()           # i przycisk
window.mainloop()       # Wyświetli się to dokładnie w takiej kolejności