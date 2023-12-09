from tkinter import *

window = Tk()

agree = IntVar()                # Tworzenie zmiennej w która będzie przechowywana wartość( czy check_box jest wciśnięty czy nie)
                                # nie musi to byc int, moze byc string czy bool. Wtedy odpowiednio nazywala by sie stringVar albo BooleanVar
def check():
    if agree.get() == 1:
        print("You agree!")
    else:
        print("You dont agree!")

photo_image = PhotoImage(file='mammon.png')

chec_box = Checkbutton(window,
                       text="I agree to something",
                       font=("Arial", 50),
                       fg="green",
                       bg="black",
                       padx=20,
                       pady=20,
                       activeforeground="green",
                       activebackground="black",
                       image=photo_image,
                       compound=LEFT,
                       variable=agree,                  # Przypisanie zmiennej w ktorej bedzie przechowywane wartosc czy checkbox jest wcisniety czy nie
                       onvalue=1,                       # Jak wartosc przyjmie zmienna 'agree' gdy checkbox jest wcisniety
                       offvalue=0,                      # Jak wartosc przyjmie zmienna 'agree' gdy checkbox jest nie wcisniety
                       command=check,
                       )



chec_box.pack()

window.mainloop()