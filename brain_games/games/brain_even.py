import prompt


def is_even(number):
	print('Answer "yes" if the number is even, otherwise answer "no".')
	print(f'Question: {number}')
	answer = prompt.string('Your answer: ')
	if (
    (number % 2 == 0 and answer.lower() == 'yes') or
    (number % 2 != 0 and answer.lower() == 'no')
):
		print('Correct!')
	else:
		print(f'Wrong! The correct answer was '
    f'{"yes" if number % 2 == 0 else "no"}.')
		print('Let\'s try again!')
		return True
