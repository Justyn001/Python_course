from tkinter import *

window = Tk()
                                                    # Canvas to 'widget' służący do rysowanie kształtów
canvas = Canvas(window, height=500, width=500)      # Tworzy okno do rysowania o rozmiarach 500x500  (0, 0 ,500 ,500) - dwa pierwsze to punkty początkowe(x,y) a dwa kolejne to punkty końcowe
#canvas.create_line(0, 0, 500, 500, fill="blue", width=5)    # Tworzy prostą linie
#canvas.create_line(500, 0, 0, 500, fill="red", width=5)
#canvas.create_rectangle(125, 100, 225, 200, fill="pink", width=10)  # Tworzy kwadrat
#points = [250, 0, 0, 500, 500, 500]                                 # Współżędne można podawać w formie tablicy
#canvas.create_polygon(points, fill="green", outline="black", width=7)   # Tworzy trójkąt z argumentem points
#canvas.create_arc(0, 0, 500, 500, fill="yellow", style=PIESLICE, start=26, width=5, extent=359)     # arc to półksiężyc i 4 pierwsze współrzędne to ilość zarezerowanego
                                                                                                          # miejsca. W style są opcje: PIESCLICE,CHORD i ARC
                                                                                                          # start to odchylnie w stopniach
                                                                                                          # extent rozszerza półksiężyć, też w stopniach
                        # Rysowanie pokeballa
canvas.create_arc(0, 400, 225, 500, extent=359, width=5, fill="red")
canvas.create_arc(275, 400, 500, 500, extent=359, width=5, fill="red")
canvas.create_line(150, 405, 150, 125, width=5)
canvas.create_line(330, 410, 330, 125, width=5)
canvas.create_polygon(145, 125, 333, 125, 239, 30)

canvas.pack()
window.mainloop()
