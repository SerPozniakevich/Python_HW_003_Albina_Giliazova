# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

# Var my

# line_n = input('Введите ряд чисел через пробел: ').split()
# line_mult = []

# for i in range(len(line_n) // 2):
#     j = int(line_n[i]) * int(line_n[-1 - i])
#     line_mult.append(j)
#     i += 1
# if len(line_n) % 2 != 0:
#     j = int(line_n[i]) ** 2
#     line_mult.append(j)
# print(f'{line_n} => {line_mult}')

# Var student
import math

# def make_pairs_prodact():
#     try:
#         num_list = input('Введите число без пробелов: ')
#         num_list = [int(i) for i in num_list]           # разбивает число на список из цифр
#         pair_list = []
#         for i in range(math.ceil(len(num_list) / 2)):  # math.ceil - функция округления до целого в большую сторону
#             pair_prodact = num_list[i] * num_list[- 1 * (i + 1)]
#             pair_list.append(pair_prodact)
#         print('\033[36m{}{}{}'.format(num_list, ' -->', pair_list))
#     except ValueError:
#         print('\033[1m\033{}'.format('Вы ввели не число!'))

# make_pairs_prodact()

# Var with Map and List Comprehension

input_list = list(map(int, input("Введите список чисел разделённых пробелом: ").split()))
prod_list = [(input_list[i]) * (input_list[len(input_list) -1 - i]) for i in range(len(input_list) // 2)]
print(input_list, prod_list)