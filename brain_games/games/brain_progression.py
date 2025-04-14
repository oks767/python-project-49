import random


def generate_arithmetic_progression(start, step, length):
    """Генерирует арифметическую прогрессию."""
    return [start + step * i for i in range(length)]


def hide_element(sequence):
    """Заменяет случайный элемент последовательности на '..'."""
    hidden_index = random.randint(0, len(sequence) - 1)
    hidden_value = sequence[hidden_index]
    sequence[hidden_index] = '..'
    return sequence, hidden_value, hidden_index

