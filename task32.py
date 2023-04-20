"""Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)"""

from random import randint


def createArray(size):
    list_1 = [randint(-5, 9) for _ in range(size)]
    return list_1


def index(my_list):
    min_elem = int(input("Введите с какого значения искать: "))
    max_elem = int(input("Введите по какое значение искать: "))
    print([i for i in range(len(my_list)) if min_elem <= my_list[i] <= max_elem])


num_size = int(input("Введите длину массива: "))
my_list = createArray(num_size)
print(my_list)
index(my_list)
