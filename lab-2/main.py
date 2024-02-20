import random


def discrete_random_variable(p):
    r = random.uniform(0, 1)
    if r == 0 or r == 1:
        return discrete_random_variable(p)
    cumulative_probability = 0
    for i, probability in enumerate(p):
        cumulative_probability += probability
        if r <= cumulative_probability:
            return i + 1


def play_game(N):
    probabilities = [0, 1 / 36, 2 / 36, 3 / 36, 4 / 36, 5 / 36, 6 / 36, 5 / 36, 4 / 36, 3 / 36, 2 / 36, 1 / 36]

    player1_wins = 0

    for i in range(N):
        summa = discrete_random_variable(probabilities)
        if summa == 7 or summa == 11:
            player1_wins += 1
        elif summa == 2 or summa == 3 or summa == 12:
            player1_wins -= 1

    return player1_wins / N


def roll_dice():
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    return dice1 + dice2


def play_game_with_dices(N):
    player1_wins2 = 0
    for i in range(N):
        summa = roll_dice()
        if summa == 7 or summa == 11:
            player1_wins2 += 1
        elif summa == 2 or summa == 3 or summa == 12:
            player1_wins2 -= 1

    return player1_wins2 / N


if __name__ == "__main__":
    rounds = int(input("Enter N: "))  # Количество игр

    average_winning_player1 = play_game(rounds)
    print(f"Средний выигрыш первого игрока после {rounds} игр через вероятности: {average_winning_player1}")

    aver = play_game_with_dices(rounds)
    print(f"Средний выигрыш первого игрока после {rounds} игр через 2 броска: {aver}")
