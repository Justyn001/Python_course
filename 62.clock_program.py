from tkinter import *
import time

window = Tk()
                                            # To mój clock program a ten w pliku 62.5 to z poradnika(czyli gorszy)

def clock_program() -> None:

    time_object = time.localtime()

    clock = Label(window,
                  text=time.strftime("%H:%M:%S", time_object),    # https://docs.python.org/3.2/library/time.html
                  font=("Arial", 90),                                    # Tu jest link do tych wszystkich %H, %A itp
                  fg="green",                                            # Opisane tam są co które robią
                  bg="black",
                  )
    clock.grid(row=0, column=0)

    day = Label(window,
                text=time.strftime("%A", time_object),
                font=("Traditional Arabic", 35),
                )
    day.grid(row=1, column=0)

    data = Label(window,
                 text=time.strftime("%d %B %Y", time_object),
                 font=("Arial", 30),
                 )
    data.grid(row=2, column=0)

    window.update()


while True:
    clock_program()
    time.sleep(1)

window.mainloop()
