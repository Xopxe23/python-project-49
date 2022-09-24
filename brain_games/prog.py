import prompt
import random


def progression_numbers(number, number_2):
    progression = []
    new_list = []
    for _ in range(number, number + 30, number_2):
        progression.append(_)
    a = progression[random.randint(0, len(progression) - 1)]
    for _ in progression:
        if _ == a:
            new_list.append('..')
        else:
            new_list.append(_)
    return progression, new_list, a


def prog():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    count = 0
    while count < 3:
        number = random.randint(1, 20)
        number_2 = random.randint(2, 5)
        progression, new_list, a = progression_numbers(number, number_2)
        print(f"Question: {' '.join(str(x) for x in new_list)}")
        answer = prompt.integer('Your answer: ')
        if answer == a:
            count += 1
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{a}'.")
            print(f"Let's try again, {name}!")
            break
    if count == 3:
        print(f'Congratulations, {name}!')
