class Duck():
    def walking(self):
        print("This duck is walking.")
    def talk(self):
        print("This duck is quacking.")

class Chicken():
    def walking(self):
        print("This chicken is walking.")
    def talk(self):
        print("This chicken is talking.")

class Person():
    def catch(self,animal):               #Przekazujemy tutaj obiekt i jesli istnieja takie same metody wewnatrz tych
        animal.walking()                  #klas to wywołają się normalnie(czyli znaczenie ma metoda(a raczej jej nazwa)
        animal.talk()                     #a nie sama klasa)
        print("You caught a duck.")


duck = Duck()
chicken = Chicken()
person = Person()

person.catch(chicken)


food = list()
while dishes := input("What food do you like: ") != "quit":       #Tu chodzi generalnie o ten znak := i ułatwia to pracę
    food.append(dishes)                                           #cięzko go wytłumaczyć po prostu zobacz co robi
