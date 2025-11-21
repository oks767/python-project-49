import prompt

def play_game(game_description, get_question_and_answer):
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game_description)
    correct_answers = 0

    for correct_answer in range(3):
        question, correct_answer = get_question_and_answer()
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ').lower()

        if user_answer == str(correct_answer).lower():
            print('Correct!')
            correct_answers += 1
        else:
            print(
                f"'{user_answer}' is wrong answer ;(. "
                f"Correct answer was '{correct_answer}'."
            )
            print(f"Let's try again, {name}!")
            return
    print(f'Congratulations, {name}!')