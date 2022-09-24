import prompt
import random


def operation(number_1, number_2, operand):
    if operand == '+':
        return number_2 + number_1
    elif operand == '-':
        return number_1 - number_2
    else:
        return number_1 * number_2


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
        answer = prompt.integer('Your answer: ')
        right_answer = operation(number_1, number_2, operand)
        if answer == right_answer:
            count += 1
            print('Correct!')
        elif operand == '+':
            print(f'{answer}  is wrong answer ;(. '
                  f'Correct answer was {right_answer}')
            print(f"Let's try again, {name}!")
            break
        elif operand == '-':
            print(f'{answer}  is wrong answer ;(. '
                  f'Correct answer was {right_answer}')
            print(f"Let's try again, {name}!")
            break
        else:
            print(f'{answer}  is wrong answer ;(. '
                  f'Correct answer was {right_answer}')
            print(f"Let's try again, {name}!")
            break
    if count == 3:
        print(f'Congratulations, {name}!')
