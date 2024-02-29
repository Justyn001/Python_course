# (Windows Defender may prevent you from running)
# (make sure pip and pyinstaller are installed/updated)
#
# 1. cd to directory that contains your .py file
#
# 2. pyinstaller -F -w -i icon.ico clock.py
#
#   -F   (all in 1 file)
#   -w   (removes terminal window) jesli program potrzebuje terminala to nie dodawaj -w
#   -i icon.ico  (adds custom icon to .exe)     ikona musi byc w formacie ico -> https://icoconvert.com/
#   clock.py  (name of your main python file)
#
# 3. exe is located in the dist folder
#
