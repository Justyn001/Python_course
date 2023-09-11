def welcome(**kwargs):
    #print("Hello, " + kwargs['first'] +" " + kwargs['last'] +" "+ kwargs['secound'])
    print("Hello,",end=" ")
    for key,values in kwargs.items():
        print(values.capitalize(),end=" ")           #To jest to samo co args tylko że dodaje rzeczy do słownika

welcome(last='kurdziel',first='maciek',secound='janusz')
print("")

animal = "cow"
item = "moon"

print("The {1} jumped over the {0}".format("cow","moon"))
print("The {} jumped over the {}".format(animal, item))         #Wszystko działa tak samo
print("The {animal} jumped over the {item}".format(animal = "cow",item = "moon"))

name = "maciek"

print("Hello, my name is {}".format(name))
print("Hello, my name is {:15}. Nice to meet you.".format(name))
print("Hello, my name is {:<15}. Nice to meet you.".format(name))
print("Hello, my name is {:>15}. Nice to meet you.".format(name))     #Odpal kod to zobaczysz co to robi
print("Hello, my name is {:^15}. Nice to meet you.".format(name))     #Centruje generalnie

number = 3.14159
number_ = 1000

print("The number pi is {:.2f}.".format(number))        #Zaokrągla do dwóch miejsc po przecinku
print("The number is {:,}.".format(number_))            #Dodaje przecinek do dużych liczb np: 1,000
print("The number is {:b}.".format(number_))            #Binarnie zapisuje liczbe
print("The number is {:o}.".format(number_))            #Zapisuje jako octal number
print("The number is {:h}.".format(number_))            #Zapisuje liczbe jako hexadecimal
print("The number is {:H}.".format(number_))            #Zapisuje liczbe jako hexadecimal
print("The number is {:E}.".format(number_))            #Zapisuje liczbe jako scientific notation