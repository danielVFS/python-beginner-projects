import random


def user_guess(x):
    random_number = random.randint(1, x)
    guess_number = 0
    while guess_number != random_number:
        guess_number = int(input(f'Guess a number between 1 and {x} \n'))
        if guess_number < random_number:
            print('Sorry, guess again, too low.')
        elif guess_number > random_number:
            print('Sorry, guess again, too high.')

    print(f"Congrats, you guesses the number {guess_number} correct!")


def computer_guess(x):
    guess_number = 0
    low = 1
    high = x
    feedback = ''
    while feedback != 'c' and low != high:
        guess_number = random.randint(low, high)

        feedback = input(f'Is {guess_number} too high(h), too low(l) or correct(c)? \n').lower()
        if feedback == 'h':
            high = guess_number - 1
        elif feedback == 'l':
            low = guess_number + 1

    print(f"Congrats, you guesses the number {guess_number} correct!")


# user_guess(20)
computer_guess(1000)

