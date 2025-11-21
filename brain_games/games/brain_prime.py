import random
from .core import play_game
from constants import RANDOM_MIN_NUMBER, RANDOM_MAX_NUMBER

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def get_question_and_answer():
    number = random.randint(RANDOM_MIN_NUMBER, RANDOM_MAX_NUMBER)
    question = str(number)
    correct_answer = 'yes' if is_prime(number) else 'no'
    return question, correct_answer

def main():
    play_game(
        'Answer "yes" if given number is prime. Otherwise answer "no".',
        get_question_and_answer
    )