# x = 1
# y = 2.0
# z = "3"
#
# x = float(x)
# y = float(y)
# z = float(z)
# print(x*y*z)
# z = str(z)
# print(z*3)

name = input("Jak masz na imie: ")
age = float(input("Ile masz lat: "))
age += 1
print("Dzień dobry, " + name.capitalize() + ". Masz " + str(age) + " lat.")