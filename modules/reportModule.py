from model.question import Question

def print_results(questions: 'list[Question]'):
    for question in questions:
        number = question.number
        if number < 10:
            number = ' ' + str(number)
        print(str(number) + ' | ' + question.cipher)
        print('R: | ' + question.answer)
        print(200 * '-')

def print_unresolved(questions: 'list[Question]'):
    print_results([question for question in questions if question.answer == ''])

def print_resolved(questions: 'list[Question]'):
    print_results([question for question in questions if question.answer != ''])

def print_resolved_percent(questions: 'list[Question]'):
    print(len([question for question in questions if question.answer != '']) / len(questions))