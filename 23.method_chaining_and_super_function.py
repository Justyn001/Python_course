class Car():
    def turn_on(self):
        print("You start the engine.")
        return self
    def drive(self):
        print("You drive the car.")
        return self
    def stop(self):
        print("You stop the car.")
        return self
    def turn_off(self):
        print("You turn off the enigne.")
        return self

car = Car()
car.turn_on()\
    .drive()\
    .stop()\
    .turn_off()

class Square():
    def __init__(self,width,lenght):
        self.width = width
        self.lenght = lenght
    def volume(self):
        return self.width*self.lenght

class Rectangle(Square):
    def __init__(self,width,lenght):
        super().__init__(width,lenght)
    def volume(self):
        return self.width*self.lenght
class Cube(Square):
    def __init__(self,width,lenght,height):
        super().__init__(width,lenght)
        self.height = height
    def volume(self):
        return self.width*self.lenght*self.height

square = Square(3,3)
rectangle = Rectangle(2,3)
cube = Cube(3,4,5)

print(square.volume())
print(rectangle.volume())
print(cube.volume())
