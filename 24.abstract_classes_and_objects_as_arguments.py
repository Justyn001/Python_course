from abc import ABC,abstractmethod
class Vehicles(ABC):
    @abstractmethod                 #klasa abstrakcyjna musi miec "pass" i musi byc nadpisana przez funkcje ktora ja
    def go(self):                   #dziedziczy oraz nie mozna utowrzyc obiektu klasy abstrakcyjnej(vehicle = Vehicules())
        pass                        #                                                                 ( To nie zadziala )

    @abstractmethod
    def stop(self):
        pass
class Car(Vehicles):
    def go(self):
        print("You drive the car.")

    def stop(self):
        print("You stop the car.")
class Motorcycle(Vehicles):
    def go(self):
        print("You drive motorcycle.")

    def stop(self):
        print("You stop the motorcycle.")

#vehicle = Vehicles()
car = Car()
motorcycle = Motorcycle()

#vehicle.go()
car.go()
car.stop()
motorcycle.go()
motorcycle.stop()


class Animal():

    spiece = None

class Human():
    spiece = None

def change_spiece(creature, spiece):
    creature.spiece = spiece

cat = Animal()
dog = Animal()
sparrow = Animal()
human = Human()

print(cat.spiece)
print(dog.spiece)
print(sparrow.spiece)
print(human.spiece)

change_spiece(cat,"cat")
change_spiece(dog,"dog")
change_spiece(sparrow,"sparrow")
change_spiece(human,"white")

print(cat.spiece)
print(dog.spiece)
print(sparrow.spiece)
print(human.spiece)