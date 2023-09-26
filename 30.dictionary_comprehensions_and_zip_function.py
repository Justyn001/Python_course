# dictionary = {key: expression for (key, value) in iterable}    1
# dictionary = {key: expresion for key,value in iterable if condition}   2
# dictionary = { key:"warunek" if value >= 50 else "cos" for key,value in dictionary.items()}    3
# dictionary = {key: funkcja(value) for (key, value) in dictionary.items()}     4

weather = {"bydgoszcz": 12,
           "katowice": 15,
           "warszawa": 22,
           "gliwice": -12,
           }

to_f = {key: round((value * 5/9)+ 32) for key, value in weather.items()}                    # 1
print(to_f)

words = {key: (value) for key,value in weather.items() if value >= 0}                        # 2
print(words)

condiotions = {key:"hot" if value >= 15 else "cold" for key,value in weather.items()}       # 3
print(condiotions)

def funct(val):
    if val >= 20:
        return "cieplo"
    elif 20 > val >= 10:
        return "chłodno"
    else:
        return "zimno"


with_function = {key: funct(value) for (key,value) in weather.items()}                         # 4
print(with_function)




login = ["maciek", "guest", "wiktor"]
password = ["kurdziel", "guest", "milusia123"]              #zip to taka troche para tylko mozna wiecej niz 2 rzeczy
                                                            #połaczyc
user = zip(login, password)
for i in user:
    print(i)

login_data = ["25/09/2023", "22/09/2023", "21/09/2023"]

user = list(zip(login,password,login_data))
print(user[0][0])





