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

    print("Congrats, you guesses the correct number!")


user_guess(20)

