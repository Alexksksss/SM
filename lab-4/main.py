import random
from math import log
import matplotlib.pyplot as plt
import numpy as np


def generate_random_number():
    number = random.uniform(0, 1)
    if number == 1 or number == 0:
        return generate_random_number()
    else:
        return number


def generate_normal():
    alpha = generate_random_number()
    if alpha >= 0.5:
        teta = (-2 * log(generate_random_number())) ** 0.5
        F_1 = (2.30753 + 0.27061 * teta) / (1 + 0.99229 * teta + 0.04481 * teta ** 2) - teta
    else:
        teta = (-2 * log(1 - generate_random_number())) ** 0.5
        F_1 = -((2.30753 + 0.27061 * teta) / (1 + 0.99229 * teta + 0.04481 * teta ** 2) - teta)
    return F_1


def generate_random_sequence(size, a, delta):
    return [generate_normal() * delta + a for _ in range(size)]


def draw_hist(F_1):
    data_min = min(F_1)
    data_max = max(F_1)
    num_intervals = int((data_max - data_min) / h)
    f = []
    for i in F_1:
        f.append(i/h)
    plt.hist(F_1, bins=num_intervals, range=(data_min, data_max), edgecolor='red', alpha=0.7, density=True)
    plt.title('Гистограмма')
    plt.xlabel('Значение случайной величины')
    plt.ylabel('Вероятность')
    plt.show()

def draw_hist2(F_1, h):
    start = min(F_1)
    end = max(F_1)
    x = np.arange(start, end + h, h)

    y = [0] * (len(x) - 1)

    for value in F_1:
        for i in range(len(x) - 1):
            if x[i] <= value < x[i + 1]:
                y[i] += 1
                break
    for i in range(len(y)):
        y[i] = y[i]/N/h

    plt.bar(x[:-1], y, width=h, edgecolor='black')
    plt.xlabel('Интервалы')
    plt.ylabel('Вероятности')
    plt.title('Столбчатая диаграмма')
    plt.show()




def three_sigma(F_1, a, delta):
    counter = 0
    for i in range(len(F_1)):
        if F_1[i] >= a + 3 * delta or F_1[i] <= a - 3 * delta:
            counter += 1
    return counter


if __name__ == '__main__':
    a = -2
    delta = 5
    h = 0.05
    N = int(input("Введите N:"))
    F_1 = generate_random_sequence(N, a, delta)

    percentage_3_sigma = (1 - (three_sigma(F_1, a, delta) / N)) * 100

    print(f"Процент значений в пределах трех среднеквадратических отклонений: {percentage_3_sigma}%")
    if percentage_3_sigma >= 99.7:
        print("Распределение соответствует нормальному по правилу трех сигм")

    draw_hist(F_1)

    draw_hist2(F_1, h)
