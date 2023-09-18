import quiz_game as quiz

while True:
    print("")
    i = quiz.read_questions()
    j = quiz.read_answers(i)
    quiz.start_game(i,j)
    pa = input("Do you want to play again (Y/N): ").lower()
    if pa == ("n") or ("no"):
        print("Byeee.")
        break