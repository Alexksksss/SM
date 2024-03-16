import random
from math import log


def generate_random_number():
    number = random.uniform(0, 1)
    if number == 1 or number == 0:
        return generate_random_number()
    else:
        return number


def generate_poisson(lmbda):
    return -1 / lmbda * log(generate_random_number())


def algorithm(lmbda, mu, T):
    t1 = 0  # момент наступления текущего события
    t2 = 0  # момент окончания обработки последнего принятого события
    size = 0
    size_drop = 0
    while True:
        t1 += generate_poisson(lmbda)  # время поступления последней заявки + время,
        # затраченное на создание новой заявки
        if t1 > T:
            break
        size += 1
        if t1 <= t2:  # если заявка поступила до окончания обработки предыдущей
            size_drop += 1
            continue
        t2 = t1 + generate_poisson(mu)
    return size, size_drop


def check_solution(lmbda, mu):
    return lmbda / (lmbda + mu)


if __name__ == "__main__":
    lmbda = 2
    mu = 1
    T = 100000  # Время окончания моделирования

    # Оценка параметра потока
    count, count_drop = algorithm(lmbda, mu, T)
    theoretical_prob = check_solution(lmbda,mu)
    print(f'Вероятность потери заявки:{count_drop / count}')
    print(f'Теоретическая вероятность: {theoretical_prob}')
    print(f'Разница между теоретической и эмпирической {abs(theoretical_prob-count_drop/count)/theoretical_prob*100}%')
