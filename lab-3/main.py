import random
from math import tan, pi


def generate_random_number():
    number = random.uniform(0, 1)
    if number == 1 or number == 0:
        return generate_random_number()
    else:
        return number


def generate_random_sequence(size):
    return [(2 * tan(pi * generate_random_number() / 2)) ** (1 / 2) for _ in range(size)]


def calculate_M_D(F):
    m, d = 0, 0
    for i in range(len(F)):
        m += F[i]
    M = 1 / len(F) * m
    for i in range(len(F)):
        d += (F[i] - M) ** 2
    D = d/(len(F)-1)
    return M, D

if __name__ == '__main__':
    N = int(input("Введите N:"))
    F_1 = generate_random_sequence(N)
    math_expectation, dispersion = calculate_M_D(F_1)
    print("Теоретическое матожидание = 2, Теоретическая дисперсия - расходится")
    print(f"Выборочное среднее: {math_expectation}", f"Несмещенная дисперсия: {dispersion}")
    print(f'Разница матожиданий: {abs(2 - math_expectation) / 2 * 100}%')

