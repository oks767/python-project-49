import random
from .core import play_game

def get_question_and_answer():
    number = random.randint(1, 100)
    question = str(number)
    correct_answer = 'yes' if number % 2 == 0 else 'no'
    return question, correct_answer

def main():
    play_game(
        'Answer "yes" if the number is even, otherwise answer "no".',
        get_question_and_answer
    )