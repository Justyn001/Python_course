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

name = "maciek kurdziel?"
if (name[0].islower()):
    print(name.capitalize())

first_name = name[:6].upper()
secound_name = name[7:].upper()
symbol = name[-1]
print(first_name)
print(secound_name)
print(symbol)