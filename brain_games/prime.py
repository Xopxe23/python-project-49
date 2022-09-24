import prompt
import random


def prime_number(randint):
    for x in range(2, randint):
        if randint % x == 0:
            return False
    else:
        return True


def prime():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    count = 0
    while count < 3:
        rand_int = random.randint(2, 100)
        right_answer = prime_number(rand_int)
        print(f"Question: {rand_int}")
        ans = prompt.string('Your answer: ')
        if ans == 'yes' and right_answer is True\
                or ans == 'no' and right_answer is False:
            print('Correct!')
            count += 1
        elif right_answer:
            print(f"{ans} is wrong answer ;(. Correct answer was 'yes'.")
            print(f"Let's try again, {name}!")
            break
        else:
            print(f"'{ans}' is wrong answer ;(. Correct answer was 'no'.")
            print(f"Let's try again, {name}!")
            break
    if count == 3:
        print(f'Congratulations, {name}!')
