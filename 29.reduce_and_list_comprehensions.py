import functools

lista = ['h','e','l','l','o',]

hello = functools.reduce(lambda x, y: (x + y), lista)
print(hello)

numbers = (1, 2, 3, 4, 5, 6, 7)

add = functools.reduce(lambda x, y: (x + y),numbers)            #reduce bierze 2 elementy tablicy i wykonuje na nich daną
print(add)                                                      #operacje, dopóki nie zostanie tylko jeden element.

data_from_api = [{'city': 'Kraków', 'province_id': 8, 'current_temp': 3.5},
    {'city': 'Warszawa', 'province_id': 1, 'current_temp': 2.8},
    {'city': 'Suwałki', 'province_id': 9, 'current_temp': -0.5},
    {'city': 'Gdańsk', 'province_id': 3, 'current_temp': -0.1},
    {'city': 'Rzeszów', 'province_id': 7, 'current_temp': 3.9},
    {'city': 'Wrocław', 'province_id': 2, 'current_temp': 5.0},]


average_temp = functools.reduce(lambda x, y: x + y['current_temp'], data_from_api, 0)
print(average_temp)




square = [i*i for i in range(0,11)]
print(square)
                                                        #Wyrażenia listowe(list comprehensions) to taka alternatywa dla
passed_1 = [i for i in square if i >= 50]               #lambdy
print(passed_1)

passed = [i if i >= 50 else "Failed" for i in square]   #Tutaj kod w list comprehensions
print(passed)

lamb = lambda x: x if x >= 50 else "Failed"             #A tutaj w lambdzie
lamb_print = list(map(lamb, square))
print(lamb_print)

