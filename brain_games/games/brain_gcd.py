import math

import prompt


def play_game(num1, num2):
    """Основная логика игры."""
    print("Find the greatest common divisor of given numbers.")
    print(f"Question:{num1} {num2}")
    correct_answer = str(math.gcd(num1, num2))
    # Запрос ответа пользователя
    user_answer = prompt.string("Your answer: ")
    
    # Проверка ответа
    if user_answer == correct_answer:
        print("Correct!")
    else:
        print(f"{user_answer} is wrong answer ;(. "
    f"Correct answer was {correct_answer}. "
    f"Let's try again!")