import math
def function(number):
    square = math.sqrt(number)
    print(square)

def hello(name):
    print("Hello, " + name.capitalize())
    print("Hava a nice day " + name.capitalize())

def name(f_name, l_name,age):
    print("Hello, " + f_name.capitalize() + " " + l_name.capitalize() + ".")
    print("You'r " + str(age) + " years old.")

for x in range(3):
    function(8)

hello("maciek")

name_ = "maciek"
surname = "kurdziel"
age_ = 14

name(name_, surname,age_)

def multiply(number1, number2):
    return number1 * number2

number = multiply(2,3)

print(number)
