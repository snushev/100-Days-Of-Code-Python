from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    question_text = question['text']
    answers = question['answer']
    new_question = Question(question_text, answers)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
while quiz.still_have_question():
    quiz.next_question()