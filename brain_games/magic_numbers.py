import prompt
import random


def magic_numbers():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    count = 0
    while count < 3:
        number = random.randint(1, 10)
        print(f'Question: {number}')
        answer = prompt.string('Your answer: ')
        if number % 2 == 0 and answer == 'yes' or number % 2 == 1 and answer == 'no':
            print('Correct!')
            count += 1
        elif answer == 'no':
            print(f"'no' is wrong answer ;(. Correct answer was 'yes'.")
            print(f"Let's try again, {name}!")
            break
        else:
            print(f"'yes' is wrong answer ;(. Correct answer was 'no'.")
            print(f"Let's try again, {name}!")
            break
    if count == 3:
        print(f"Congratulations, {name}!")
