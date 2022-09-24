import prompt
import random


def calc():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('What is the result of the expression? ')
    count = 0
    operands = ['+', '-', '*']
    for operand in operands:
        number_1 = random.randint(1, 10)
        number_2 = random.randint(1, 30)
        print(f'Question: {number_1} {operand} {number_2}')
        answer = prompt.string('Your answer: ')
        if operand == '+':
            if int(answer) == number_1 + number_2:
                count += 1
                print('Correct!')
            else:
                print(f'{answer}  is wrong answer ;(. Correct answer was {number_1 + number_2}')
                print(f"Let's try again, {name}!")
                break
        elif operand == '-':
            if int(answer) == number_1 - number_2:
                count += 1
                print('Correct!')
            else:
                print(f'{answer}  is wrong answer ;(. Correct answer was {number_1 - number_2}')
                print(f"Let's try again, {name}!")
                break
        elif operand == '*':
            if int(answer) == number_1 * number_2:
                count += 1
                print('Correct!')
            else:
                print(f'{answer}  is wrong answer ;(. Correct answer was {number_1 * number_2}')
                print(f"Let's try again, {name}!")
                break
    if count == 3:
        print(f'Congratulations, {name}!')
