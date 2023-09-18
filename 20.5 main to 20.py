#from object_oriented_programming_and_class_variables import Car

car_1 = Car("alfa romeo",159,2007,"black")
car_2 = Car("renault","clio",2005,"blue")

print(car_1.brand)
print(car_1.model)
print(car_1.year)
print(car_1.colour)

car_1.drive()
car_1.stop()

print(car_1.wheels)
print(Car.wheels)

car_1.wheels = 2
print(car_1.wheels)
print(car_2.wheels)
print(Car.wheels)

Car.wheels = 1
print(car_1.wheels)
print(car_2.wheels)
print(Car.wheels)