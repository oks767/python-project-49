# from brain_games.games.brain_calc import main
from games.core import play_game
from games.brain_calc import get_question_and_answer

def main():
    play_game(
        'What is the result of the expression?',
        get_question_and_answer
    )

# def main_script():
#     print('Welcome to the Brain Games!')
#     main()