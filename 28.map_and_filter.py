store = [("pants", 20.00),
         ("hoodie", 25.00),
         ("boots", 50.00),
         ("hat", 12.50)]

euro1 = lambda items: (items[0],items[1]*0.93)
euro = list(map(euro1,store))

zloty = list(map(lambda items: (items[0],items[1]*4.32),store))
                                                                    #Mapa jest inna niz w c++,
                                                                    #funkcja map() daje nam możliwość wykonania zadanej
                                                                    #funkcji dla każdego elementu kolekcji.
for i in zloty:
    print(i)

for i in euro:
    print(i)



people = [('rafal',21),                                 #Funkcja filter() tworzy nową listę elementów na podstawie
          ('maciek',2),                                 #wejściowej listy elementów, wybierając tylko te wartości,
          ('mozambik',19),                              #dla których funkcja testując zwróci prawdę (True).
          ('kurdziel',12)]

drinking_budies = list(filter(lambda tuple:(tuple[1] >= 18),people))

for i in drinking_budies:
    print(i)

data_from_api = [{'city': 'Kraków', 'province_id': 8, 'current_temp': 3.5},
    {'city': 'Warszawa', 'province_id': 1, 'current_temp': 2.8},
    {'city': 'Suwałki', 'province_id': 9, 'current_temp': -0.5},
    {'city': 'Gdańsk', 'province_id': 3, 'current_temp': -0.1},
    {'city': 'Rzeszów', 'province_id': 7, 'current_temp': 3.9},
    {'city': 'Wrocław', 'province_id': 2, 'current_temp': 5.0},]

work = lambda data:data['current_temp'] >= 0
hot_cities = list(filter(work,data_from_api))

for i in hot_cities:
   print(i)

hot_cities = list(filter(lambda data : data['current_temp'] >= 0,data_from_api))

for i in hot_cities:
    print(i)