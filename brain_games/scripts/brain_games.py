from brain_games.cli import welcome_user
from brain_games.scripts.brain_even import is_even
import random


def main():
    print('Welcome to the Brain Games!')
    welcome_user()
    is_even(random.randint(1, 100))