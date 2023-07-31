age = int(input("Ile masz lat: "))

if age == 100:
    print("Jesteś już seniorem!")
elif age >= 18:
    print("Jesteś dorosły.")
elif age < 18:
    print("Jesteś dzieckiem.")
else:
    print(f"Wiek {age} nie istnieje.")


temp = int(input("Ile stopni jest na dworze: "))

if not(temp >= 0 and temp <= 30):
    print("Zbyt ekstrementalna temperatura.\nZostań w domu!")
if not(temp < 0 or temp > 30):
    print("Temperatura spoko.\nWyjdz z domu!")
