import random
import prompt

from brain_games.cli import welcome_user
from brain_games.games.brain_progression import (
    generate_arithmetic_progression,
    hide_element,
)

def main():
    name = welcome_user()
    print('What number is missing in the progression?')
    correct_answers = 0

    while correct_answers < 3:
        start = random.randint(1, 10)
        step = random.randint(1, 5)
        length = random.randint(5, 10)
        progression = generate_arithmetic_progression(start, step, length)
        modified_sequence, hidden_value, hidden_index = hide_element(progression[:])

        print("Question:", " ".join(map(str, modified_sequence)))
        user_answer = prompt.string("Your answer: ")

        if user_answer == str(hidden_value):
            print("Correct!")
            correct_answers += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{hidden_value}'.")
            print(f"Let's try again, {name}!")
            return
    print(f"Congratulations, {name}!")