import json
from model.question import Question

def get_questions() -> 'list[Question]':
    with open('encrypted-questions/encrypted-questions.json', encoding='utf-8-sig') as file_json:
        dictQuestions: list[dict] = json.load(file_json)
        questions = [] # type: list[Question]

        for x in dictQuestions:
            questions.append(Question(x))

        return questions