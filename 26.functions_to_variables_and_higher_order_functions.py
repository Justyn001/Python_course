def hello():
    print("Hello")

print(hello)
hi = hello

cout = print
cout("Now its like in C++.")

#Funckje higher order są w 2 postaciach 1 kiedy funkcja przyjmuję funkcję jako argumeny i w 2 zwraca funkcje

#Postac 1
def louder(words):
    return words.upper()

def lower(words):
    return words.lower()

def hello(func,words):
    text = func(words)
    print(text)

hello(louder,"Hello")

#Postac 2

def first(x):               #przypisujemy do zmiennej first funkcje first z argumentem 5 nastepnie funkcja ta zwraca
    def secound(y):         #funckje secound (czyli przypisuje ją do zmiennej first) następnie printujemy funckje first
        return x/y          #czyli przypisaną funkcje secound z argumentem 10 i zwarcamy dzielenie x/y
    return secound          #No troche pojebane ale ma sense

first = first(5)
print(first(10))

def first(x):
    def secound(y):
        def third(z):
            return (x/y)*z              #Tutaj to samo dla trzech funkcji
        return third
    return secound

first = first(100)
first = first(10)
print(first(20))