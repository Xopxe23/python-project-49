import prompt
import random


def prog():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('What number is missing in the progression?')
    count = 0
    while count < 3:
        number = random.randint(1, 20)
        number_2 = random. randint(2, 5)
        progression = []
        for _ in range(number, number + 30, number_2):
            progression.append(_)
        a = progression[random.randint(0, len(progression)-1)]
        new_list = []
        for _ in progression:
            if _ == a:
                new_list.append('..')
            else:
                new_list.append(_)
        print(f"Question: {' '.join(str(x) for x in new_list)}")
        answer = prompt.integer('Your answer: ')
        if answer == a:
            count += 1
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{a}'.")
            break
    if count == 3:
        print(f'Congratulations, {name}!')
