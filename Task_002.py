# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

line_n = input('Введите ряд чисел через пробел: ').split()
line_mult = []

for i in range(len(line_n) // 2):
    j = int(line_n[i]) * int(line_n[-1 - i])
    line_mult.append(j)
    i += 1
if len(line_n) % 2 != 0:
    j = int(line_n[i]) ** 2
    line_mult.append(j)
print(f'{line_n} => {line_mult}')
