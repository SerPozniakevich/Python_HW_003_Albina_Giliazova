#Задайте список из вещественных чисел. Напишите программу, 
# которая найдёт разницу между максимальным и минимальным 
# значением дробной части элементов.
#Пример:
#[1.1, 1.2, 3.1, 5, 10.01] => 0.19

import copy
import random
from random import uniform

# list1 = [1.1, 1.2, 3.1, 5, 10.01]
# print(list1)
# list_fract = []
# f = 2                              # количество знаков после запятой. 
# j = 0

# for i in range(len(list1)):    # создаём список состоящий из дробной части
#     if list1[i] % 1 != 0:       # исключаем целые числа
#         j = round(list1[i] % 1, f)
#         list_fract.append(j)
# print(list_fract)

# max_num = max(list_fract)
# min_num = min(list_fract)
# print(f'{list1}, => {max_num - min_num}')

# Var random float list

# for i in range(number):
#     list1.append(round(random.uniform(100, 1000), 2))

# Var 2 random float list
n = 5
list1 = [round(random.uniform(0.0, 11.0), 2) for i in range(n)]
list2 = [0] * n
print(list1)
print(list2)