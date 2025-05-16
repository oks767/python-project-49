import math
import random

import prompt

from brain_games.cli import welcome_user


def play_game():
    """Основная логика игры."""
    name = welcome_user()
    print("Find the greatest common divisor of given numbers.")
    correct_answers = 0

    while correct_answers < 3:
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
        print(f"Question: {num1} {num2}")
        correct_answer = str(math.gcd(num1, num2))
        user_answer = prompt.string("Your answer: ")

        if user_answer == correct_answer:
            print("Correct!")
            correct_answers += 1
        else:
            print(
                f"'{user_answer}' is wrong answer ;(. "
                f"Correct answer was '{correct_answer}'."
            )
            print(f"Let's try again, {name}!")
            return
    print(f"Congratulations, {name}!")