from tkinter import *
from time import *


def update() -> None:
    clock_: str = strftime("%H:%M:%S")
    clock_label.config(text=clock_)

    day_: str = strftime("%A")
    day.config(text=day_)

    data_: str = strftime("%d %B %Y")
    data.config(text=data_)

    window.after(1000, update)      # Funckja after po 1000 mili sekund wykona funkcje po przecinku


window = Tk()
clock_label = Label(window,
                    font=("Arial", 90),
                    fg="green",
                    bg="black",
                    )
clock_label.pack()

day = Label(window,
            font=("Traditional Arabic", 35),
            )
day.pack()

data = Label(window,
             font=("Arial", 30),
             )
data.pack()

update()
window.mainloop()
