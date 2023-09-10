def fullname(fname,sname,lname):
    print("Hello, " + fname + " " + sname + " " + lname + ".")

fullname(fname = "Justyn",lname = "Rojkowski", sname = "Maciej")

while True:
    number = input("Type in a positive number: ")
    if number == "0":
        break
    else:
        #number = float(number)
        #number = round(number)
        #number = abs(number)    #wartosc bezwzględna
        print(abs(round(float(number))))
