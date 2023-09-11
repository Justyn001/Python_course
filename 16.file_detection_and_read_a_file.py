import os

path = "D:\\Repozytoria\\PycharmProjects"

if os.path.exists(path):
    print("This location exist.")
    if os.path.isfile(path):
        print("It's a file.")
    elif os.path.isdir(path):
        print("It's a directory.")
else:
    print("That location doesn't exist.")


try:
    with open("test.txt") as file:
        print(file.read())
except FileNotFoundError:
    print("File do not exist.")