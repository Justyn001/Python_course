import time
import threading

# Deamon threads to w zasadzie to samo co threading tylko program aby zakończyć działanie nie czeka aż deamon threding
# się skończy czyli np. masz licznik czasu spędzony w aplikacji i wyjście z programu automatycznie kończy ten threading
def timer():
    count:int = 0
    while True:
        time.sleep(1)
        count += 1
        print("\nYou using this program for: {} secounds".format(count))


x = threading.Thread(target=timer, daemon=True)         #deamon = True tu ustala się deamon threading
x.start()

answer = input("Do you want to exit: ")
