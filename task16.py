"""Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X.
5
1 2 3 4 5
3
-> 1"""
from random import randint
n = int(input("Введите длину массива: "))
massiv = []
for i in range(n):
    new_element = randint(1, 10)
    massiv.append(new_element)
    print(new_element, end=' ')
X = int(input("\nВведите искомое число Х: "))
quantity = 0
for i in range(len(massiv)):
    if X == massiv[i]:
        quantity += 1
print("Число", X, "в массиве встречается", quantity, "раз.")
