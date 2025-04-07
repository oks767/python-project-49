from brain_games.cli import welcome_user
import random
from brain_games.games.brain_gcd import play_game


def main():
    print('Welcome to the Brain Games!')
    welcome_user()
    play_game(random.randint(1, 100), random.randint(1, 100))