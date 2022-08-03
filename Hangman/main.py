import random
from words import words
from hangman_visual import lives_visual_dict
import string


def get_valid_word(words) -> str:
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()


def hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    lives = 7

    while len(word_letters) > 0 and lives > 0:
        print(f'\nYou have {lives} lives')
        print('You have used these letters: ', ' '.join(used_letters))

        word_list = [letter if letter in used_letters else '-' for letter in word]
        print(lives_visual_dict[lives])
        print('Current word ', ' '.join(word_list))

        user_letter = input('Guess a letter \n').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives = lives - 1
                print('\nYour letter is not in the word')
        elif user_letter in used_letters:
            print('You already use that word! Please try again')
        else:
            print('Invalid Character. Please try again')

    if lives == 0:
        print(lives_visual_dict[lives])
        print(f'You died, sorry! The correct word was {word}')
    else:
        print(f'Congrats!! You guessed the right word, who that is {word}')


if __name__ == '__main__':
    hangman()
