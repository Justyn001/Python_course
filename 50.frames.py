from tkinter import *

window = Tk()

                                            # frame - to taka ramka do której możesz dodać przyciski (pewnie inne rzeczy tez)
                                            # i zamiast ustawiać każdy przycisk po koleji to pakujesz to do frame i z framem robisz .pack(side=TOP/LEFT..)

frame = Frame(window, bg="pink", bd=5, relief=SUNKEN)                                # bd i relief to tabelka wokół frame
frame.place(x=0, y=0)                                                                # mozna tez uzyc .pack ale place tez jest git

Button(frame, text="W", font=("arial", 30), width=5).pack(side=TOP)                  # .pack(side=TOP) to ustawiam na miejscu TOP przycisk W w ramce(frame)
Button(frame, text="A", font=("arial", 30), width=5).pack(side=LEFT)
Button(frame, text="S", font=("arial", 30), width=5).pack(side=LEFT)
Button(frame, text="D", font=("arial", 30), width=5).pack(side=LEFT)

window.mainloop()
