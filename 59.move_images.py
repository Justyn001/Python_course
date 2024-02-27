from tkinter import *

# window = Tk()
#                                                         # Ruszanie obiektami "on window"
# race_car = PhotoImage(file="race_car.png")
# label = Label(image=race_car)
#
#
# def move_forward(event) -> None:
#     label.place(x=label.winfo_x() + 100, y=label.winfo_y())           # label.winfo_x() to akutalna pozycja samochodziku
#                                                                       # dodajemy 100 i zmienia położenie o 100 w prawo
#
# def move_left(event) -> None:
#     label.place(x=label.winfo_x() - 4, y=label.winfo_y())             # adekwatnie wszystkie tutaj pod tym
#
#
# def move_up(event) -> None:
#     label.place(x=label.winfo_x(), y=label.winfo_y() - 4)
#
#
# def move_down(event) -> None:
#     label.place(x=label.winfo_x(), y=label.winfo_y() + 4)
#
#
# window.bind("<d>", move_forward)
# window.bind("<a>", move_left)
# window.bind("<w>", move_up)
# window.bind("<s>", move_down)
# window.bind("<Right>", move_forward)
# window.bind("<Left>", move_left)
# window.bind("<Up>", move_up)
# window.bind("<Down>", move_down)
#
# label.place(x=0, y=0)
# window.mainloop()

                                                            # Ruszanie obiektami "on canvas"

window = Tk()

canvas = Canvas(window, height=500, width=500)
race_car = PhotoImage(file="race_car.png")


def move_up(event) -> None:
    canvas.move(my_image, 0, -10)


def move_down(event) -> None:
    canvas.move(my_image, 0, 10)


def move_left(event) -> None:
    canvas.move(my_image, -10, 0)


def move_right(event) -> None:
    canvas.move(my_image, 10, 0)                        # canvas.move to po prostu przesunięcie podanego zdjęcia(my image) o 10 na osi x i 0 na osi y


window.bind("<w>", move_up)
window.bind("<s>", move_down)
window.bind("<a>", move_left)
window.bind("<d>", move_right)

my_image = canvas.create_image(0, 0, image=race_car, anchor=NW)      # canvas.create_image to po prostu dodanie zdjęcia na pozycji 0,0
canvas.pack()                                                              # anchor = NW (North West) to żeby zdjęcia nie ucieło to dopasowuje do
window.mainloop()                                                          # północno zachodznie granicy tego okienka
