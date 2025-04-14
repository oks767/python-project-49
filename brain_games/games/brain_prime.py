import prompt


def is_prime(number):
	print('Answer "yes" if given, otherwise answer "no".')
	print(f'Question: {number}')
	answer = prompt.string('Your answer: ')
	
	if number == 1:
		correct_answer = False
	elif number == 2:
		correct_answer = True
	elif number % 2 == 0:
		correct_answer = False
	else:
		correct_answer = True
		for i in range(3, int(number ** 0.5) + 1, 2):
			if number % i == 0:
				correct_answer = False
				break

	if ((answer.lower() == 'yes' and correct_answer) or
    (answer.lower() == 'no' and not correct_answer)):
		print("Correct!")
	else:
		correct_response = "yes" if correct_answer else "no"
		print(f"Wrong! The correct answer was {correct_response}.")
