from tkinter import *
                            # Radio buttons to wybieranie z listy jednej rzeczy
window = Tk()

food = ['pizza', 'hamburger', 'spaghetti']

x = IntVar()

def order():
    if x.get() == 0:
        print("You order pizza.")
    elif x.get() == 1:
        print("You order hamburger.")
    else:
        print("You order spaghetti.")

photo1 = PhotoImage(file='cmonbruh.png')
photo2 = PhotoImage(file='kappa.png')
photo3 = PhotoImage(file='omegalul.png')

photo_list = [photo1, photo2, photo3]

for i in range(len(food)):
    radio_buttons = Radiobutton(window,
                                text=food[i],
                                font=("Arial",40),
                                variable=x,
                                value=i,                # Każda opcja będzie miała inną wartość
                                command=order,
                                padx=20,
                                image=photo_list[i],    # Grafika z listy o odpowiednim indeksie zostanie dodana
                                compound=LEFT,
                                #indicatoron=0,          # Jeśli chce zamiast 'ptaszków' miec przyciski
                                width=900)              # Wyśrodkowywuje i rezerwuje daną ilość miejsca
    radio_buttons.pack()
window.mainloop()
