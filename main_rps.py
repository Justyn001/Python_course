import rock_paper_scissors_game as rps

j = rps.fileread()
x = 4
while x != 0:
    x = rps.start()
    y = rps.computerchoice()
    z = rps.game(x,y,j)
rps.savetofile(z)