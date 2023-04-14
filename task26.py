"""Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.
*Пример:*
A = 3; B = 5 -> 243 (3⁵)
    A = 2; B = 3 -> 8 """


def degree(a, b, result):
    result = result*a
    b -= 1
    if b <= 1:
        return result
    return degree(a, b, result)


a = int(input("Введите число: "))
b = int(input("Введите целую степень: "))
print(degree(a, b, a))
