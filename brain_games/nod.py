import prompt
import random
import math


def gcd():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Find the greatest common divisor of given numbers.')
    count = 0
    while count < 3:
        number_1 = random.randint(1, 10)
        number_2 = random.randint(1, 30)
        print(f"Question: {number_1} {number_2}")
        answer = prompt.integer('Your answer: ')
        if answer == math.gcd(number_1, number_2):
            count += 1
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{math.gcd(number_1, number_2)}'.")
            print(f"Let's try again, {name}!")
            break
        if count == 3:
            print(f'Congratulations, {name}!')
