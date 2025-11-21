import random
from .core import play_game
from constants import RANDOM_MIN_NUMBER, RANDOM_MAX_NUMBER

def get_question_and_answer():
    number = random.randint(RANDOM_MIN_NUMBER, RANDOM_MAX_NUMBER)
    question = str(number)
    correct_answer = 'yes' if number % 2 == 0 else 'no'
    return question, correct_answer

def main():
    play_game(
        'Answer "yes" if the number is even, otherwise answer "no".',
        get_question_and_answer
    )