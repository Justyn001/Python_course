import random

x = random.randint(1,6)
y = random.random()             #Losuje bardzo małą losową liczbę

rps = ['rock','paper','scissors']
aichoice = random.choice(rps)

cards = [1,2,3,4,5,6,7,8,9,10,'J','Q','K','A']
random.shuffle(cards)

print(x)
print(y)
print(aichoice)
print(cards)

while True:
    try:
        numerator = int(input("Entry a number to divide: "))
        denominator = int(input("Entry a number to divide by: "))
        results = numerator/denominator
        print(results)
        break
    except ZeroDivisionError:
        print("You can't divide by 0.\nTry again!")
    except ValueError:
        print("Enter a real number.\nTry again!")
    finally:
        print("Closing a file.")