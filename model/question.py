class Question(object):
    def __init__(self, dictQuestion: dict):
        self.number: int = dictQuestion['number']
        self.title: str = dictQuestion['title']
        self.cipher: str = dictQuestion['cipher']
        if 'answer' in dictQuestion:
            self.answer: str = dictQuestion['answer']
        else:
            self.answer: str = ''