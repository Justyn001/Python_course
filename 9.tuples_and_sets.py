student = ("maciek",21,"male")

print(student.count("maciek"))
print(student.index("male"))

for x in student:
    print(x)

if "maciek" in student:
    print("maciek is here!")

print("")

utensils = {"fork","spoon","knife"}      #To taka lista tylko odrazu segreguje jak mapa w c++ i usuwa powtarzające się elementy
dishes = {"bowl","plate","cup","knife"}
utensils.add("napkin")
utensils.remove("fork")
#utensils.clear()
utensils.update(dishes)
table = utensils.union(dishes)

for x in table:
    print(x)
print(utensils.difference(dishes))
print(utensils.intersection(dishes))  #Zwraca te wartośći które są wspólne w obu listach
