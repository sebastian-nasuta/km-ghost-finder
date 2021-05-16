from modules import questionsModule as qm, reportModule as rm, caesarCipherModule as ccm

class Main:
    questions = qm.get_questions()

    #ccm.runCaesar([question for question in questions if question.answer == ''])

    rm.print_unresolved(questions)
    #rm.print_resolved(questions)
    #rm.print_results(questions)
    #rm.print_resolved_percent(questions)