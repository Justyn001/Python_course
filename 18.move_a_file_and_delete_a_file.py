import os

#source = 'test.txt'
#destiantion = 'D:\\test.txt'

#try:
 #   if os.path.exists(destiantion):
  #      print('There is already a file there.')
  #  else:
   #     os.replace(source,destiantion)
#except FileNotFoundError:
 #   print(source+" file not found.")


import shutil

path = 'full_folder'

try:
    os.remove(path)         #Do usuwania zwyłych plików
    #os.rmdir(path)          #Do usuwania pustych foledrów
    #os.rmtree(path)         #Do usuwania pełnych folderów
except FileNotFoundError:
    print(path+" file was not found.")
except PermissionError:
    print("You dont have permision to remove "+path)
except OSError:
    print("You can't delete that "+path+" using that function.")
finally:
    print(path+" was successfully removed.")