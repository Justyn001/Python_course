while True:
    rows = int(input("Na jaka szerokosc: "))
    lenght = int(input("Na jaka dlugosc: "))
    symbol = input("Jaki chcesz symbol: ")
    if (rows == 0 or lenght == 0):
        break
    for u in range(0,lenght):
        for i in range(0,rows):
            print(symbol,end="")
        print("\n",end="")

phone_number = "794-721-251"

for number in phone_number:
    if number == "-":
        continue
    else:
        print(number,end="")

for number in range(1,21):
    if number == 13:
        pass
    else:
        print(number)

