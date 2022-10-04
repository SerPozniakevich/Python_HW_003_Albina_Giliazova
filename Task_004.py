#Напишите программу, которая будет преобразовывать десятичное число в двоичное.
#Пример:
#45 -> 101101
#3 -> 11
#2 -> 10

from tkinter import NO


num_dec = int(input('Введите число: '))
num_temp = num_dec
num_bin = ''
 
while num_temp > 0:
    num_bin = str(num_temp % 2) + num_bin
    num_temp = num_temp // 2
 
print(f'{num_dec} -> {num_bin}')