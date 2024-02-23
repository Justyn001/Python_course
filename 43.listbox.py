from tkinter import *

window = Tk()
                                            # listbox to okienko z wyborem jednej lub kilku opcji
listbox = Listbox(window,
                  font=('Aldhabi', 30),
                  bg='#fffbe4',
                  width=10,
                  selectmode=MULTIPLE,)     # Dodaje mozliwosc wyboru wiecej niz jednej opcji

listbox.insert(0, 'pizza')  # Dodaje opcje 1
listbox.insert(1, 'burger')  # Dodaje opcje 2
listbox.insert(2, 'pasta')  # Dodaje opcje 3
listbox.insert(3, 'spaghetti')  # Dodaje opcje 4

listbox.config(height=listbox.size())       # Lista będzie takiego rozmiaru ile jest opcji (po prostu dopasuje się do ilości opcji)


def order():
                # Printowanie zamowienia dla tylko jednej wybranej opcji
   # print("You have ordered" + listbox.get(listbox.curselection()))     # Wyprintuje aktualnie wybrana opcje
                # Prinotwanie zamownienia dla kilku opcji
    food = []
    for index in listbox.curselection():                # dla każdej wartości wybranej (index)
        food.append(listbox.get(index))                 # dodaje ją do listy 'food'
    print("You have ordered: ")
    for i in food:                                      # prosta pętla wypisująca
        print(i)


def add():
    listbox.insert(listbox.size(), entrybox.get())     # Doda wpisaną w entryboxie wartość do listy
    listbox.config(height=listbox.size())                       # Ustawi rozmiar listy na aktualną liczbę opcji na liście


def delete():
        # Usuwanie dla jednej wartosci
    #listbox.delete(listbox.curselection())
        # Usuwanie dla kilku wartości
    for index in reversed(listbox.curselection()):      # reversed jest żeby się nie psuło i leciało od końca bo indeksy po usunięciu się zmieniają
        listbox.delete(index)                           # a jak od końca lecimy to nie ma to znaczenia czy się zmieniają
    listbox.config(height=listbox.size())               # Ustawi rozmiar listy na aktualną liczbę opcji na liście


button1 = Button(window, text="order", command=order)   # przycisk order
entrybox = Entry(window)                                # okienko do wpisywania wartosći do dodania
button2 = Button(window, text="add", command=add)        # przycisk add
button3 = Button(window, text='delete', command=delete)  # przycisk delete


listbox.pack()
entrybox.pack()
button2.pack()
button1.pack()
button3.pack()
window.mainloop()
