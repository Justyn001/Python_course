
double = lambda x : x * x
multiplay = lambda x,y : x * y
name = lambda f_name, s_name: f_name.capitalize() + " " + s_name.capitalize()
age = lambda age : True if age >= 18 else False

print(double(5))
print(multiplay(5,2))
print(name("maciek","kurdziel"))
print(age(21))


students = [('maciek',2,22),
            ('rafal',3,21),
            ('euzebiusz',6,20),
            ('gerwazy',4,19)]

grade = lambda grade:grade[1]                               #Sortuje tą tablice po indeksie krotki w tym przypadku po ocenach
#students.sort(key=grade,reverse=True)
sorted_students = sorted(students,key=grade,reverse=True)

for i in sorted_students:
    print(i)