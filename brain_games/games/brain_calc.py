import random
import prompt
from brain_games.cli import welcome_user
def play_game():
    name = welcome_user()
    print('What is the result of the expression?')
    correct_answers = 0
    operations = ['+', '-', '*']

    while correct_answers < 3:
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
        operation = random.choice(operations)
        print(f'Question: {num1} {operation} {num2}')
        if operation == '+':
            correct_answer = num1 + num2
        elif operation == '-':
            correct_answer = num1 - num2
        else:
            correct_answer = num1 * num2
        user_answer = prompt.string('Your answer: ')

        if user_answer == str(correct_answer):
            print('Correct!')
            correct_answers += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return
    print(f'Congratulations, {name}!')
