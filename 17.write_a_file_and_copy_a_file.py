
text = "Brooo, let me cook.\n"

with open("test.txt","a") as file:      #"a" do dodawania do pliku, "w" do napisywania pliku jak w c++
    file.write(text)

import shutil

#copyfile()
#copy()             #Wszystkie służą do kopiowania pliku ale generalnie podczas kursu użwyałem tylko copyfile()
#copy2()


shutil.copyfile("test.txt", "copy.txt")      #pierwszy argument to skąd kopiuje w tym przyapdku z
                                                      #pliku test.txt do pliku copy.txt