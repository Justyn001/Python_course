import random
import time

def fileread():
    path = "scores.txt"
    try:
        with open(path) as file:
            userscore = file.readline()
            computerscore = file.readline()
    except FileNotFoundError:
        print("FileNotFoundError.")
    tuple = [userscore,computerscore]
    print(f"Hey, welcome on rock, paper, scissors game!\nYou're score vs Computer score: {userscore} - {computerscore}\n"
          "Let's start!")
    return tuple

def start():
    print("\nChoose wisely!")
    choose = int(input("1.Rock\n2.Paper\n3.Scissors\nType your lucky number: "))
    return choose

def computerchoice():
    choice = random.randint(1,3)
    return choice

def game(userchoice,computerchoice,score):
    uscore = int(score[0])
    cscore = int(score[1])
    winmessage = "You win :)\nLet's play again!"
    losemessage = "You lose ;(\nLet's play again!"
    drawmessage = "It's a draw!\nLet's play again!"

    if userchoice == 1:
        if computerchoice == 1:
            print("Computer choosing",end="")
            for secounds in range(3):
                time.sleep(1)
                print(".", end="")
            print(" The computer chose: ROCK!\n" +drawmessage)
            uscore += 1
            cscore += 1

        elif computerchoice == 2:
            print("Computer choosing", end="")
            for secounds in range(3):
                time.sleep(1)
                print(".", end="")
            print(" The computer chose: PAPER!\n" + losemessage)
            cscore += 1

        else:
            print("Computer choosing", end="")
            for secounds in range(3):
                time.sleep(1)
                print(".", end="")
            print(" The computer chose: SCISSORS!\n" + winmessage)
            uscore += 1

    elif userchoice == 2:
        if computerchoice == 1:
            print("Computer choosing", end="")
            for secounds in range(3):
                time.sleep(1)
                print(".", end="")
            print(" The computer chose: ROCK!\n" + winmessage)
            uscore += 1

        elif computerchoice == 2:
            print("Computer choosing", end="")
            for secounds in range(3):
                time.sleep(1)
                print(".", end="")
            print(" The computer chose: ROCK!\n" + drawmessage)
            uscore += 1
            cscore += 1

        else:
            print("Computer choosing", end="")
            for secounds in range(3):
                time.sleep(1)
                print(".", end="")
            print(" The computer chose: ROCK!\n" + losemessage)
            cscore += 1

    elif userchoice == 3:
        if computerchoice == 1:
            print("Computer choosing", end="")
            for secounds in range(3):
                time.sleep(1)
                print(".", end="")
            print(" The computer chose: ROCK!\n" + losemessage)
            cscore +=1

        elif computerchoice == 2:
            print("Computer choosing", end="")
            for secounds in range(3):
                time.sleep(1)
                print(".", end="")
            print(" The computer chose: ROCK!\n" + winmessage)
            uscore += 1

        else:
            print("Computer choosing", end="")
            for secounds in range(3):
                time.sleep(1)
                print(".", end="")
            print(" The computer chose: ROCK!\n" + drawmessage)
            uscore += 1
            cscore += 1

    stuple = [uscore,cscore]
    return stuple

def savetofile(score):
    path = "scores.txt"

    with open(path,"w") as file:
         file.write(f"{score[0]}\n{score[1]}")
