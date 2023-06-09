"""Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой грядке, причем кусты высажены только по окружности. Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод – на i-ом кусте выросло ai ягод.
В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит из управляющего модуля и нескольких собирающих модулей. Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль, находясь перед некоторым кустом заданной во входном файле грядки."""

from random import randint

size = randint(5, 10)
kust = [randint(1, 10) for i in range(size)]
print("Урожайность кустов:", kust)

max_sbor = kust[-2] + kust[-1] + kust[0]
sum_sbor = max_sbor

for i in range(size - 1):
    sum_sbor = kust[i-1] + kust[i] + kust[i+1]
    if sum_sbor > max_sbor:
        max_sbor = sum_sbor
print("Максимальный сбор с трёх кустов:", max_sbor)
