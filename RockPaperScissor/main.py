import random


def play():
    user = input("'r' for rock, 'p' for paper or 's' for scissor \n")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return "It's a Tie game"

    if you_win(user, computer):
        return f'You Won!! You play {user} and the machine plays {computer}'

    return f'You Lost!! You play {user} and the machine plays {computer}'


def you_win(player, computer) -> bool:
    if (player == 'r' and computer == 's') or (player == 's' and computer == 'p') or (
            player == 'p' and computer == 'r'):
        return True


print(play())
