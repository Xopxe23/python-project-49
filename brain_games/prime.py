import prompt
import random


def prime():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    count = 0
    while count < 3:
        rand_int = random.randint(2, 100)
        right_answer = True
        for x in range(2, rand_int):
            if rand_int % x == 0:
                right_answer = False
        print(f"Question: {rand_int}")
        answer = prompt.string('Your answer: ')
        if answer == 'yes':
            if right_answer is True:
                print('Correct!')
                count += 1
            else:
                print(f"{answer} is wrong answer ;(. Correct answer was 'yes'.")
                print(f"Let's try again, {name}!")
                break
        elif answer == 'no':
            if right_answer is False:
                print('Correct!')
                count += 1
            else:
                print(f"'{answer}' is wrong answer ;(. Correct answer was 'no'.")
                print(f"Let's try again, {name}!")
                break
    if count == 3:
        print(f'Congratulations, {name}!')
