import random
from brain_games.cli import welcome_user
from brain_games.games.brain_progression import generate_arithmetic_progression, hide_element
import prompt

def main():
    welcome_user()
    # Генерация параметров прогрессии
    start = random.randint(1, 10)  # Первый элемент
    step = random.randint(1, 5)    # Разность прогрессии
    length = random.randint(5, 10) # Длина прогрессии
    
    # Создание прогрессии
    progression = generate_arithmetic_progression(start, step, length)
    
    # Скрытие элемента
    modified_sequence, hidden_value, hidden_index = hide_element(progression[:])
 
    # Получаем ответ от игрока
 
    print('What number is missing in the progression?')
    print(f"Question: ", " ".join(map(str, modified_sequence)))
    user_answer = int(prompt.string("Your answer: "))
    
    # Проверка ответа
    if user_answer == hidden_value:
        print(f"Correct!")
    else:
        print(f"{user_answer} is wrong answer ;(. Correct answer was {hidden_value}")
        print("Let's try again!")
		# Выводим результат