import random
import math
from .core import play_game
from constants import RANDOM_MIN_NUMBER, RANDOM_MAX_NUMBER

def get_question_and_answer():
    num1 = random.randint(RANDOM_MIN_NUMBER, RANDOM_MAX_NUMBER)
    num2 = random.randint(RANDOM_MIN_NUMBER, RANDOM_MAX_NUMBER)
    question = f"{num1} {num2}"
    correct_answer = str(math.gcd(num1, num2))
    return question, correct_answer

def main():
    play_game(
        'Find the greatest common divisor of given numbers.',
        get_question_and_answer
    )