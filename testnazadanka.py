contacts = [("James", 42),
            ("Amy", 24),
            ("John", 31),
            ("Amanda", 63),
            ("Bob", 18)]
flag = True
i = str(input("Name: "))
for j in range(len(contacts)):
    if i.capitalize() == contacts[j][0]:
        print(contacts[j][0] + " is " + str(contacts[j][1]))
        flag = False
if flag:
    print("Not Found")
