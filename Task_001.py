#   Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
#   Пример:
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# Var my

# line_n = input('Введите ряд чисел через пробел: ').split()
# summ_neg_ind = 0

# for i in range(len(line_n)):
#     if i % 2 != 0:
#         summ_neg_ind += int(line_n[i])
# print(f'{line_n} -> cумма элементов на нечётных позициях равна: {summ_neg_ind}')

# Var tutor

line_n = input('Введите ряд чисел через пробел: ').split()
summ_neg_ind = 0

for i in range(1, len(line_n), 2):
    summ_neg_ind += int(line_n[i])
print(f'{line_n} -> cумма эелментов на нечётных позициях равна: {summ_neg_ind}')