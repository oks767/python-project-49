import random

import prompt


def is_even():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    correct_answers = 0

    while correct_answers < 3:
        number = random.randint(1, 100)
        print(f'Question: {number}')
        answer = prompt.string('Your answer: ').lower()
        correct = 'yes' if number % 2 == 0 else 'no'
        if answer == correct:
            print('Correct!')
            correct_answers += 1
        else:
            print(
                f"'{name}' is wrong answer ;(. "
                f"Correct answer was '{answer}'."
            )
            print(f"Let's try again, {name}!")
            return
    print(f'Congratulations, {name}!')
