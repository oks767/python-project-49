from brain_games.cli import welcome_user
from brain_games.games.brain_prime import is_prime
import random


def main():
	print('Welcome to the Brain Games!')
	welcome_user()
	is_prime(random.randint(1, 100))
