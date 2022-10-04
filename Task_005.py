#Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
#Пример:
#для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

 
n = int(input('Ведите число: '))

list_poz = []
for i in range(0, n + 1): # заполняем положительный ряд 
    list_poz.append(i)

list_poz_fib = []             # Фибонначи для положительного ряда
j = None
for i in range(len(list_poz)):
    if i < 1:
        j = 0
    if i in [1, 2]:
        j = 1
    if i > 2:
        j = list_poz_fib[i - 1] + list_poz_fib[i - 2]
    list_poz_fib.append(j)

list_neg_fib = [] 
g = 0                     # отрицательный ряд это зеркальная копия положительного
for i in range(len(list_poz_fib) - 1):
    if g % 2 == 0:
        g = list_poz_fib[-1 * (i + 1)] * -1   # значение с чётным индексом  - отрицательное 
    else:
        g = list_poz_fib[-1 * (i + 1)]
    list_neg_fib.append(g)

list_fib = list_neg_fib + list_poz_fib # объединяем списки в один
print(list_fib)