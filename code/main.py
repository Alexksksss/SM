import random
import math
import matplotlib.pyplot as plt
import scipy.stats as stats
import numpy as np


def generate_random_number():
    number = random.uniform(0, 1)
    if number == 1 or number == 0:
        return generate_random_number()
    else:
        return number


def generate_random_sequence(size):
    # Генерируем последовательность случайных чисел
    return [generate_random_number() for _ in range(size)]


def plot_histogram(data, N):
    # Строим гистограмму для визуализации распределения
    plt.hist(data, bins=20, density=True, alpha=0.75, color='b')
    plt.xlabel('Значения БСВ')
    plt.ylabel('Частота')
    plt.title('Гистограмма распределения БСВ')
    #plt.savefig(f"histogram{N}.png")
    plt.show()


def my_chi_test(N, k, data):
    random_numbers = data

    # Разбиение интервала (0, 1) на k равных частей
    intervals = np.linspace(0, 1, k + 1)

    # Определение в какой интервал попадает
    interval_indices = np.floor(k * np.array(random_numbers)).astype(int)

    # Подсчет количества чисел в каждом интервале
    counts = np.histogram(interval_indices, bins=range(k+1))[0]

    # Вычисление статистики χ²
    expected_counts = np.full_like(counts, N / k)
    chi_square_statistic = 0
    for i in range(k):
        chi_square_statistic += ((counts[i] - expected_counts) ** 2) / expected_counts

    degrees_of_freedom = k - 1

    p_value = 1 - stats.chi2.cdf(chi_square_statistic, degrees_of_freedom)

    return chi_square_statistic[0],  p_value[0]


def pearson_chi_squared_test(data, k):
    # Выполняем критерий Пирсона
    observed_frequencies, _ = np.histogram(data, bins=k)
    expected_frequencies = np.ones_like(observed_frequencies) * len(data) / k  # Ожидаемое равномерное распределение (создает массив такого же размера из 1)
    chi_squared_statistic, p_value = stats.chisquare(observed_frequencies, expected_frequencies)

    return chi_squared_statistic, p_value


# Генерируем выборку БСВ
N = int(input("Введите размер выборки: "))
k = int(1 + 3.3 * math.log(N))
random_sequence = generate_random_sequence(N)

print("Готовая функция для вычисление")
result_auto = pearson_chi_squared_test(random_sequence, k)
print(f"Статистика χ²: {result_auto[0]}")
print(f"P-значение: {result_auto[1]}")

print("Вычисление по формуле")
result = my_chi_test(N, k, random_sequence)
print(f"Статистика χ²: {result[0]}")
print(f"P-значение: {result[1]}")

# Строим гистограмму для визуализации распределения
plot_histogram(random_sequence, N)

