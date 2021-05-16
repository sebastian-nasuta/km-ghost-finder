from model.question import Question

# keyWords = ['who', 'what', 'which', 'why', 'where', 'when', 'how', 'and']
keyWords = ['if']
alphabet = 'abcdefghijklmnopqrstuvwxyz'

def transform(input: str, shift: int) -> str:
    if shift == 0:
        return input

    positiveShift: bool = shift > 0
    shift = abs(shift)
    charList = list(input.casefold())

    for charListIndex, char in enumerate(charList):
        if(alphabet.find(char) >= 0):
            for i in range(shift):
                if positiveShift:
                    if alphabet.find(charList[charListIndex]) == len(alphabet) - 1:
                        charList[charListIndex] = alphabet[0]
                    else:
                        charList[charListIndex] = alphabet[alphabet.find(charList[charListIndex]) + 1]
                if not positiveShift:
                    if alphabet.find(charList[charListIndex]) == 0:
                        charList[charListIndex] = alphabet[len(alphabet) - 1]
                    else:
                        charList[charListIndex] = alphabet[alphabet.find(charList[charListIndex]) - 1]
    return ''.join(charList)

def runCaesar(questions: 'list[Question]'):
    for shiftNumber in range(-50, 50):

        for i, question in enumerate(questions):
            transformedCipher: str = transform(question.cipher, shiftNumber)
            if transformedCipher == question.cipher:
                continue

            for word in keyWords:
                if(transformedCipher.casefold().find(word.casefold()) >= 0):
                    print('Shift: ' + str(shiftNumber) + ' | ' + str(question.number) + ' | ' + transformedCipher)