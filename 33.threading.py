import threading
import time

# Threading to przypisywanie poleceń komputerowi żeby wykonywał je równocześnie np. na raz dwie funkcję dzieli się na:
# cpu bound - program/task spends most of it's time waiting for internal events(CPU intensive) Use multiprocessing
# i
# io bound -program/task spends most of it's time waiting for external events(user input) Use multithreading


def eating(food):
    time.sleep(4)
    print(f"You ate the {food}.")
    print(threading.active_count())     # Wypisuje liczbę dziejących się na raz procesów


def drinking():
    time.sleep(3)
    print("You drunk a coffe.")
    print(threading.active_count())


def learning():
    time.sleep(2)
    print("You finished studying.")
    print(threading.active_count())


x = threading.Thread(target=eating, args="b")
y = threading.Thread(target=drinking, args=())
z = threading.Thread(target=learning, args=())

x.start()   # Zaczyna wykonwyanie procesu
y.start()
z.start()

x.join()    # Main Thread poczeka aż x się wykona
y.join()
z.join()

print(threading.active_count())
print(threading.enumerate())          # Zwraca listę aktywnych(dziejących się w tym momencie procesów)
print(time.perf_counter())            # Wypisuje jak długo zajęło głównemu procesowi(Main Thread) dojście do końca(wykoanie wszystkich zadań)
