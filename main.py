from model.question import Question
from modules.questionProviderModule import get_questions

questions = [] # type: list[Question]

class Main:
    questions = get_questions()

    for question in questions:
        number = question.number
        if number < 10:
            number = ' ' + str(number)
        print(str(number) + ' | ' + question.cipher)
        print('R: | ' + question.answer)
        print(200 * '-')
