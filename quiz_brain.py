import html
from data import question_data
class QuizBrain:

    def __init__(self):
        self.question_number = 0
        self.question_list = question_data
        self.current_question = None

    # def still_has_questions(self):
    #     return self.question_number < len(self.question_list)

    def next_question(self):
        if self.question_number > 9:
            return "Done"
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        current_question = html.unescape(self.current_question["question"])
        print(current_question)
        return str(current_question)
            
