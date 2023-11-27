import time
from multiprocessing import Process, cpu_count

# Multiprocesing jest bardzo podobny do threadingu tylko używa się go wtedy gdy potrzebna jest moc obliczeniowa
# np jak liczenie do biliona


def counter(nums):
    count: int = 0
    while count < nums:
        count += 1


def main():
    print(cpu_count())                                      # Wyswietla liczbe dostepnych rdzeni u mnie to 8
    x = Process(target=counter, args=(125_000_000,))        #Przyporządkowanie pierwszemu rdzeniowi zadania liczenia do 125000000
    y = Process(target=counter, args=(125_000_000,))        #Przyporządkowanie drugiemu rdze........
    z = Process(target=counter, args=(125_000_000,))
    j = Process(target=counter, args=(125_000_000,))
    i = Process(target=counter, args=(125_000_000,))
    h = Process(target=counter, args=(125_000_000,))
    k = Process(target=counter, args=(125_000_000,))
    m = Process(target=counter, args=(125_000_000,))        #no i w sumie daje to bilion a czas wykonaia jest krótszy niż jakbym to na jednym robił

    y.start()
    x.start()
    z.start()
    j.start()
    i.start()
    h.start()
    k.start()
    m.start()

    x.join()
    y.join()
    z.join()
    j.join()
    i.join()
    j.join()
    k.join()
    m.join()

    print("Finished in: ", round(time.perf_counter()), "seconds.")


if __name__ == "__main__":         #To trzeba dodać bo inaczej na windowsie się multiprocessing jebie i nie działa
    main()
