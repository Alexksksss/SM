import random
from math import log


def generate_random_number():
    number = random.uniform(0, 1)
    if number == 1 or number == 0:
        return generate_random_number()
    else:
        return number


def generate_poisson(t, lmbda):
    return t.append(t[-1] - 1 / lmbda * log(generate_random_number()))


def generate_poisson_sequence(lmbda, T):
    t = [-1 / lmbda * log(generate_random_number())]
    while t[-1] < T:
        generate_poisson(t, lmbda)
    return t[:-1]  # Выбрасываем последнее значение = T


def estimate_lambda(N, lmbda, T):
    lambda_hat_sum = 0

    for i in range(N):
        t = generate_poisson_sequence(lmbda, T)
        events = len(t)
        lambda_hat_sum += events / T

    lambda_hat = lambda_hat_sum / N

    return lambda_hat


if __name__ == "__main__":
    N = 50000  # Количество экспериментов
    lmbda = 1.3
    T = 15  # Время окончания моделирования

    # Оценка параметра потока
    lambda_hat = estimate_lambda(N, lmbda, T)

    print(f"Оценка параметра потока (lambda_hat): {lambda_hat}")
    print(f"Отношение разности к изначальной lambda: {abs(lambda_hat-lmbda)/lmbda  *100}%")
