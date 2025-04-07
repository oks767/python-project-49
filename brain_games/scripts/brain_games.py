from brain_games.cli import welcome_user
from brain_games.games.brain_even import is_even
import random
from brain_games.games.brain_gcd import play_game


def main():
    print('Welcome to the Brain Games!')
    welcome_user()
    is_even(random.randint(1, 100))
    play_game(random.randint(1, 100), random.randint(1, 100))