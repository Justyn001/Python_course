class Animal():

    alive = True

    def eat(self):

        print("This animal is eating.")

    def sleep(self):

        print("This animal is sleeping.")

class Rabit(Animal):
    def running(self):
        print("This animal is running.")
class Fish(Animal):
    def swimming(self):
        print("This aniaml is swemming.")
class Hawk(Animal):
    def flying(self):
        print("This animal is flying.")

rabit = Rabit()
fish = Fish()
hawk = Hawk()

print(rabit.alive)
fish.eat()
hawk.sleep()

rabit.running()
fish.swimming()
hawk.flying()

class Organism():

    alive = True

class Animal1(Organism):
    def eating(self):
        print("This animal is eating.")

class Cat(Animal1):
    def mewowing(self):
        print("This cat is meowing.")


cat = Cat()
print(cat.alive)
cat.eating()
cat.mewowing()



