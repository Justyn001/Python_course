from tkinter import *
import time
import random

HEIGHT = 500                                            # Dużymi literami w pythonie definuje się zmienne const
WIDTH = 500
xSpeed = 3
ySpeed = 2


window = Tk()

canvas = Canvas(window, height=HEIGHT, width=WIDTH)     # Tworzy canvas(płótno o podanych rozmiarach)

background = PhotoImage(file="background.png")
ufo_image = PhotoImage(file="ufo.png")

image_width = ufo_image.width()                         # Zwraca długość ufo_image
image_height = ufo_image.height()                       # Zwraca wysokość ufo_image

background_ = canvas.create_image(0, 0, image=background, anchor=NW)        # Dodaje zdjęcie(background) w miejscu 0,0
ufo_image_ = canvas.create_image(0, 0, image=ufo_image, anchor=NW)          # anchor = NW to dopasowanie do north west krawędzi "płótna"

canvas.pack()

while True:
    coordinates = canvas.coords(ufo_image_)                                   # canvas.coords(ufo_infor) zwraca listę w której argument 0 to pozycja na osi x a 1 to na osi y
    if coordinates[0] >= HEIGHT - image_width or coordinates[0] < 0:          # pierwszy if - żeby ufo nie przekroczyło granicy "płótna" w prawo a drugi if - żeby nie przekroczyło w lewo
        xSpeed = -xSpeed                                                      # Gdy przekroczy tą granicę to zmienia kierunke (idzie w drugą stronę)
    if coordinates[1] >= WIDTH - image_height or coordinates[1] < 0:          # Adekwatnie wszyko dla osi y
        ySpeed = -ySpeed
    canvas.move(ufo_image_, xSpeed, ySpeed)                             # Rusza ufo o Xspeed pixeli na osi x i ySpeed na osi y
    window.update()                                                           # Odświeża okno
    time.sleep(0.02)


window.mainloop()
