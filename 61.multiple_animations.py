from tkinter import *
import time


class Ball:
    def __init__(self, canvas_, x, y, diameter, x_speed, y_speed, color):               # <- To jest konstruktor
        self.canvas_ = canvas_
        self.make_ball = canvas_.create_oval(x, y, diameter, diameter, fill=color)      # <- W konstruktorze tworzymy obiekt(koło) o współrzędnych początkowych
        self.x_speed = x_speed                                                          #  x,y,diameter,diamter(diameter to średnica więc wzdłuż i wszerz będzie
        self.y_speed = y_speed                                                          # taka sama

    def move(self):
        coordination = self.canvas_.coords(self.make_ball)      # Zwraca listę 4 argumentową argument 0 - to pozycja(najbardziej wysunięta na lewo części koła
        print(coordination)                                    # 1 - to górnej częsci koła 2 - to prawej a 3 - to dolnej
        if coordination[0] < 0 or coordination[2] > self.canvas_.winfo_width():     # sprawdza czy nie dotyka granic półtna po lewej ani po prawej
            self.x_speed = -self.x_speed                                            # jesli dotyka to zmiania kierunku
        if coordination[1] < 0 or coordination[3] > self.canvas_.winfo_height():    # adekwatnie tutaj dla y
            self.y_speed = -self.y_speed
        window.update()
        self.canvas_.move(self.make_ball, self.x_speed, self.y_speed)               # rusza obiektem make_ball o x_speed pixeli na osi x i y_speed pixexli
                                                                                    # na osi y
HEIGHT = 500
WIDTH = 500

window = Tk()

canvas = Canvas(window, height=HEIGHT, width=WIDTH)
canvas.pack()

oval1 = Ball(canvas, 0, 0, 100, 1, 1, "black")          # Tworzenie różnych kół
oval2 = Ball(canvas, 0, 0, 50, 4, 3, "white")
oval3 = Ball(canvas, 0, 0, 125, 8, 7, "yellow")
oval4 = Ball(canvas, 0, 0, 75, 2, 1, "brown")
while True:                                                                             # Nieskończona pętla żeby obiekty się poruszały
    oval1.move()
    oval2.move()
    oval3.move()
    oval4.move()
    time.sleep(0.01)

window.mainloop()
