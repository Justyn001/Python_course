import time

# name = ""
#
# while len(name) == 0:
#     name = input("Jak sie nazywasz: ")
# print("Hello " + name.capitalize())

for number in range(10):
    print(number + 1)

for number in range(50,101):
    print(number)

for number in range(50,101,2):
    print(number)

for secounds in range(10,0,-1):
    print(secounds)
    time.sleep(1)
print("BOOM")