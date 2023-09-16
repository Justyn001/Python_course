def read_questions():
    questions = []
    response = []
    with open("Questions.txt", "r") as q:
        y = 0
        for line in q:
            if y % 2:
                response.append(line.strip())                      #Nie wiem dlaczego python traktuje 1 jako podzielną
                y += 1                                             #przez 2
            else:
                questions.append(line.strip())
                y += 1
    q.close()
    question_dictionary = {}
    for x in range(len(questions)):
        question_dictionary.update({questions[x]: response[x]})
    return question_dictionary

def read_answers(dictionary):
    with open("Answers.txt", "r") as a:
        answers2d = []
        while len(answers2d) != len(dictionary):
            answers = []
            x = 0
            while x != 4:
                answers.append(a.readline().strip())
                x += 1
                if x == 4:
                    answers2d.append(answers)
    a.close()
    return answers2d

def start_game(dictionary,answers):
    x = 0
    while x != 1:
        for keys, values in dictionary.items():
            print(keys)
            for i in range(4):
                print(answers[x][i])
            x += 1

i = read_questions()
j = read_answers(i)
start_game(i,j)
