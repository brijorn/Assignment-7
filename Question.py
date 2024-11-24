class TriviaQuestion:

    def __init__(self, question, answer1, answer2, answer3, answer4, correct_answer_num):
        self.question = question
        self.answer1 = answer1
        self.answer2 = answer2
        self.answer3 = answer3
        self.answer4 = answer4
        self.correct_answer_num = correct_answer_num

    def __str__(self):
        return f'{self.question}\n1. {self.answer1}\n2. {self.answer2}\n3. {self.answer3}\n4. {self.answer4}'