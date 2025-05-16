import random

from brain_games.cli import welcome_user
from brain_games.games.brain_calc import play_game


def main():
    print('Welcome to the Brain Games!')
    play_game()
