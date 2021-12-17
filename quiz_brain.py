class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_questions_remaining(self):

        return len(self.question_list) > self.question_number

    def check_answer(self, ques, current_question):
        if current_question.answer == ques:
            self.score += 1
            print(f"You'r Right : Your Score is {self.score}/{self.question_number}")
        else:
            print(f"You'r Wrong  : Your Score is {self.score}/{self.question_number}")
        print("\n")

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        ques = input(f"Q {self.question_number}:  {current_question.question} (True/False) : ").capitalize()
        self.check_answer(ques, current_question)
