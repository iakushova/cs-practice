
import numpy as np

# Задание 1

hours = np.arange(0, 24, 3)
line = np.linspace(0, 1, 5)
zeros = np.zeros(6, dtype=int)
unknown_table = np.full((2, 3), -1)
identity = np.eye(3)

print('hours:', hours)
print('shape:', hours.shape)
print('ndim:', hours.ndim)
print('size:', hours.size)
print('dtype:', hours.dtype)

print('line:', line)
print('zeros:', zeros)
print('unknown_table:')
print(unknown_table)
print('identity:')
print(identity)

# Задание 2

print('Третий элемент:', hours[2])
print('Последний элемент:', hours[-1])
print('Элементы с индексами 2-5:', hours[2:6])
print('Каждый второй элемент:', hours[::2])
print('В обратном порядке:', hours[::-1])

# Задание 3

temperatures = np.array([
    [12, 14, 13, 15],
    [11, 13, 16, 17],
    [10, 12, 15, 18]
])

print('Форма:', temperatures.shape)
print('Измерения:', temperatures.ndim)
print('Количество элементов:', temperatures.size)

print('Вторая строка, третий столбец:', temperatures[1, 2])
print('Первая строка:', temperatures[0])
print('Последний столбец:', temperatures[:, -1])
print('Первые две строки без первого столбца:')
print(temperatures[:2, 1:])

print('Центральный фрагмент:')
print(temperatures[:2, 1:3])

# Задание 4

matrix = np.arange(1, 26).reshape(5, 5)

print('Исходная матрица:')
print(matrix)

print('Первые три строки:')
print(matrix[:3, :])
print('Форма:', matrix[:3, :].shape)

print('Последние две строки:')
print(matrix[3:, :])
print('Форма:', matrix[3:, :].shape)

print('Первые два столбца:')
print(matrix[:, :2])
print('Форма:', matrix[:, :2].shape)

print('Фрагмент:')
print(matrix[1:4, 2:5])
print('Форма:', matrix[1:4, 2:5].shape)

print('Правый нижний блок 2x2:')
print(matrix[3:5, 3:5])
print('Форма:', matrix[3:5, 3:5].shape)

# Задание 5

vector = np.array([10, 20, 30, 40, 50])
vector[1:4] = 0
print('Измененный вектор:', vector)

small_matrix = np.arange(1, 10).reshape(3, 3)
small_matrix[0, :] = -1
small_matrix[1:, 1:] = 9
print('Измененная матрица:')
print(small_matrix)

changed_hours = hours.copy()
changed_hours[2:5] = 99
changed_hours[::2] = -1

print('Измененный hours:', changed_hours)
print('Исходный hours:', hours)

# copy() нужна, чтобы изменения не затронули исходный массив

changed_matrix = matrix.copy()
changed_matrix[1, :] = 0
changed_matrix[:, -1] = -1
changed_matrix[1:4, 1:4] = 100

print('Измененная матрица:')
print(changed_matrix)

print('Исходная матрица:')
print(matrix)

# Задание 6

numbers = np.arange(12)

table = numbers.reshape(3, 4)

transposed = table.T

print('Исходный массив:')
print(numbers)

print('Таблица:')
print(table)

print('Транспонированная таблица:')
print(transposed)

print('Форма numbers:', numbers.shape)
print('Форма table:', table.shape)
print('Форма transposed:', transposed.shape)

# reshape(3, 4) работает, потому что 3 * 4 = 12.
# reshape(5, 3) вызовет ошибку, потому что 5 * 3 = 15,
# а в массиве только 12 элементов.
