class Prey():

    def flee(self):
        print("This animal is running.")

class Predator():
    def hunting(self):
        print("This animal is hunting.")

class Rabbit(Prey):
    pass
class Hawk(Predator):
    pass
class Fish(Prey, Predator):
    pass

rabit = Rabbit()
hawk = Hawk()
fish = Fish()

rabit.flee()
hawk.hunting()
fish.flee()
fish.hunting()

class Animal():
    def eat(self):
        print("This animal is eating.")

class Dog(Animal):
    def eat(self):
        print("This dog is eating my shoe.")

dog = Dog()
dog.eat()