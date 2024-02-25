from tkinter import *
from tkinter.ttk import *
import time

window = Tk()


def download() -> None:
    gb: int = 100
    speed: int = 1
    download_: int = 0
    while download_ != 100:
        time.sleep(0.05)
        bar['value'] += (speed/gb)*100                                  # bar['value'] to progres paska jego wartość maksymalna to 100
        download_ += speed
        percent.set(str(int((download_/gb)*100)) + "%")                 # Wyświetla tekst ile procent się już pobrało i generalnie jak nie dam tu inta po stringiem to się strasznie psuje nie wiem czemu
        text.set(str(download_) + "/" + str(gb) + " GB completed.")     # Wyświetla tekst ile gb się już pobrało
        window.update_idletasks()                                       # Updejtuje okienko tzn. pasek progresu i napisy


percent = StringVar()                       # StringVar -Jest to zmienna kiedy wartość tej zmiennej zostanie zmieniona, widżety, z którymi jest powiązana
text = StringVar()                          # automatycznie odświeżają się, aby odzwierciedlić tę zmianę. Czyli po prostu updejtują się.

bar = Progressbar(window, orient=HORIZONTAL, length=300)
bar.pack(pady=10, padx=5)

Label(window, textvariable=percent).pack()
Label(window, textvariable=text).pack()

Button(window, text="download", command=download).pack()

window.mainloop()
