from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

data_bank = []

for question in question_data:
    q_text = question['question']
    q_answer = question['correct_answer']
    data_bank.append(Question(q_text, q_answer))


quiz = QuizBrain(data_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You have completed the quiz!!!")
print(f"Your final score is {quiz.score}/{len(quiz.question_list)}")
