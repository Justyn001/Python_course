country = {
    "Usa": "washington",
    "Russia" : "moscow",
    "Poland" : "warsaw",
}

print(country.get('Germany'))       #Sprawdza czy 'germany' jest w słowniku

print(country.keys())
print(country.values())
print(country.items())

for key, value in country.items():
    print(key, value)

country.update({'Germany':'Berlin',"Usa":'New York'})
country.pop('Russia')
country.clear()