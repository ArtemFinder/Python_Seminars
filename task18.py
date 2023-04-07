"""Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
5
1 2 3 4 5
6
-> 5"""
from random import randint
n = int(input("Введите длину массива: "))
X = int(input("\nВведите искомое число Х: "))
nearly = 0                  # искомое число
difference = 100            # разница между чисел
massiv = []
for i in range(n):  # генерация массива
    new_element = randint(1, 100)
    massiv.append(new_element)
    print(new_element, end=' ')

for i in range(len(massiv)):
    if X < massiv[i] and massiv[i]-X < difference:
        difference = massiv[i]-X
        nearly = massiv[i]
    elif X > massiv[i] and X-massiv[i] < difference:
        difference = X-massiv[i]
        nearly = massiv[i]

print("Число", X, "ближе всего в массиве к числу", nearly)
