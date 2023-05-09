# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.

# *Пример:*
# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8 

def exponentiation(a, b):
    if b == 0:
        return 1
    if a == 0:
        return 0
    if b == 1:
        return a
    return a * exponentiation(a, b-1)

number_1 = int(input('Введите число которое хотите возвести в степень: '))
number_2 = int(input('Введите степень: '))
print(exponentiation(number_1, number_2))