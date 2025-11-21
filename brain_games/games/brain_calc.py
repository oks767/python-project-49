import random
from constants import RANDOM_MIN_NUMBER, RANDOM_MAX_NUMBER

def get_question_and_answer():
    num1 = random.randint(RANDOM_MIN_NUMBER, RANDOM_MAX_NUMBER)
    num2 = random.randint(RANDOM_MIN_NUMBER, RANDOM_MAX_NUMBER)
    operation = random.choice(['+', '-', '*'])
    question = f"{num1} {operation} {num2}"
    if operation == '+':
        correct_answer = num1 + num2
    elif operation == '-':
        correct_answer = num1 - num2
    else:
        correct_answer = num1 * num2
    return question, str(correct_answer)

