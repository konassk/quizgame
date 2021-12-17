from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    new_question = Question(question["question"],question["correct_answer"])
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
score = True
while score:
    quiz.next_question()
    score = quiz.still_questions_remaining()
print("You've Completed the quiz!\n")
print(f"Your Final Score was : {quiz.score}/{quiz.question_number}")
