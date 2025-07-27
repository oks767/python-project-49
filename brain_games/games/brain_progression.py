import random
from .core import play_game

def generate_arithmetic_progression(start, step, length):
    return [start + step * i for i in range(length)]

def hide_element(sequence):
    hidden_index = random.randint(0, len(sequence) - 1)
    hidden_value = sequence[hidden_index]
    sequence[hidden_index] = '..'
    return sequence, hidden_value

def get_question_and_answer():
    start = random.randint(1, 10)
    step = random.randint(1, 5)
    length = random.randint(5, 10)
    progression = generate_arithmetic_progression(start, step, length)
    modified_sequence, hidden_value = hide_element(progression[:])
    question = " ".join(map(str, modified_sequence))
    return question, str(hidden_value)

def main():
    play_game(
        'What number is missing in the progression?',
        get_question_and_answer
    )