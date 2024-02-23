from tkinter import *
from tkinter import messagebox

window = Tk()

# messagebox to takie okienka co wyskakują np przy kopiowaniu pliku z folderu do folderu.
def click():
    #messagebox.showinfo(title="info", message="This is information.")           # Pokazuje okienko informacyjne
    #messagebox.showwarning(title="warning", message="This is warning.")         # Pokazuje okienko ostrzegawcze
    #messagebox.showerror(title="error", message="This is error.")               # Pokazuje okienko z errorem

   # if messagebox.askokcancel(title="question", message="Do you like coding?"): # Pojawi się okienko z opcjami ok i cancel
   #     print("You like coding.")                                               # to wyświetli się po wciśnięciu ok
 #   else:
  #      print("You dont like coding.")                                          # a to po cancel


    # if messagebox.askretrycancel(title="question", message="Do you like coding?"):  # Pojawi się okienko z opcjami retry i cancel
    #     print("good good")
    # else:
    #     print("bad bad")

    #if messagebox.askyesno(title="question", message="Do you like coding?"):        # Pojawi się okienko z opcjami yes i no
      #print("good good")                                                            # Zwraca wartość true i false
    #else:
        #print("bad bad")

    #if messagebox.askquestion(title="question", message="Do you like coding?"):      # Pojawi się okienko z opcjami yes i no
        #print("good")                                                                # Zwraca wartość jako string 'yes' i 'no'
    #else:
        #print("bad")

    answer = messagebox.askyesnocancel(title="question", message="Do you like coding?") # Pojawi się okienko z opcjami yes i no i cancel
    if answer == True:                                                                  # Zwraca wartość jako True, False i None
        print("you click 'tak'.")
    elif answer == False:
        print("you click 'nie'.")
    else:
         print("you click 'anuluj'")

messagebo = Button(window,
                   command=click,           # po naciśnięciu przycisku wyświetli się wyskakujące okienko
                   text="click me")

messagebo.pack()
window.mainloop()
