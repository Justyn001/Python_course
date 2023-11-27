import time

print(time.ctime(0))        #Modyfikuje wartosc czasu (od poczatku istnienia dla twojego komputera) na zmienna którą da się przeczytać

print(time.time())          #Wyswietli ilosc sekund od poczatku czasu dla twojego komputera

print(time.ctime(time.time()))      #Wyswietli aktualna date(time.time() zrobi to co wyzej a time.ctime zmodyfikuje to na wartosc którą da się przeczytac

time_object = time.localtime()      #time.localtime to struktura zawierające wszystkie dane z aktualnej daty w formie
print(time_object)                  #struktury(dzien, miesiac, rok, godzina itp)

local_time = time.strftime("%d %m %Y %H:%M:%S", time_object)    #strftime wyswietla tylko te wartosci ktore umiescimy w "format"
print(local_time)                                                      #z zmiennej time_object (%d to wyswietlenie dnia, %H to godzina itp)

time_string = "12 February 2012"
time_object1 = time.strptime(time_string,"%d %B %Y")            #time.strptime robi odwrotnosc time.strftime po protstu zamienia podaną datę,
print(time_object1)                                                    #(nazwy muszą być poprawnie po angielsku) na strukturę z datą(taką jak w time.local)

#(year, month, day, hours, minutes, secs, #day of the weak, #day of the year, dst)
time_touple = (2009, 12, 18, 7, 41, 34, 2, 0, 0)
time_string1 = time.asctime(time_touple)                #time.asctime - zamienia podaną listę(musi być w odpowedniej kolejności takie jak wypisana powyżej)
print(time_string1)                                     #na nornalnie wypisaną datę

time_touple = (2009, 12, 18, 7, 41, 34, 2, 0, 0)
time_string2 = time.mktime(time_touple)                 #time.mktime To wyświetla liczbę sekund które minęły od podanej w liście daty
print(time_string2)