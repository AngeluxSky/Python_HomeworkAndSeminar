# Homework для 1 семинара.

# Задача 2: Найдите сумму цифр трехзначного числа.
# *Пример:*
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |

# num = int(input('Введите трёхзначное число: '))
# a = num // 100
# b = (num // 10) % 10
# c = num % 10
# print(a + b + c)
# print(f'({a} + {b} + {c})')


# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов.
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое
# количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# *Пример:*
# 6 -> 1  4  1
# 24 -> 4  16  4
# 60 -> 10  40  10

# s = int(input())
# print((s//6), ((s//6)*4), (s//6))


# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд
# и получали билет с номером. Счастливым билетом называют такой билет с шестизначным номером,
# где сумма первых трех цифр равна сумме последних трех. Т.е. билет с номером 385916 – счастливый,
# т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.
# *Пример:*
# 385916 -> yes
# 123456 -> no

# numTicket = input('Введите шестизначный номер билета: ')
# sum1 = int(numTicket[0]) + int(numTicket[1]) + int(numTicket[2])
# sum2 = int(numTicket[3]) + int(numTicket[4]) + int(numTicket[5])
# if sum1 == sum2:
#     print('Yes')
# else:
#     print('No')


# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
# если разрешается сделать один разлом по прямой между дольками
# (то есть разломить шоколадку на два прямоугольника).
# *Пример:*
# 3 2 4 -> yes
# 3 2 1 -> no

# n = int(input('Введите длину шоколадки: '))
# m = int(input('Введите ширину шоколадки: '))
# k = int(input('Введите количество долек: '))
# if k < m * n and (k % m == 0 or k % n == 0):
#     print('Yes')
# else:
#     print('No')


# Homework для 2 семинара.


# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой,
# а некоторые – гербом. Определите минимальное число монеток,
# которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть.

# n = int(input('Введите кол-во монеток: '))
# coin_tails = 0  # решка
# coin_heads = 0  # орел
# for i in range(n):
#     a = int(input())
#     if a == 0:
#         coin_tails += 1
#     else:
#         coin_heads += 1
# if coin_heads > coin_tails:
#     print(coin_tails)
# else:
#     print(coin_heads)


# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница.
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000),
# а Катя должна их отгадать. Для этого Петя делает две подсказки.
# Он называет сумму этих чисел S и их произведение P.
# Помогите Кате отгадать задуманные Петей числа.

# x = int(input('Введите задуманную сумму чисел: '))
# y = int(input('Введите задуманное произведение чисел: '))
# for i in range(x):
#     for j in range(y):
#         if x == i + j and y == i * j:
#             print(i, j)


# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k),
# не превосходящие числа N.

# a = int(input())
# i = 0
# while 2 ** i <= a:
#     print(2 ** i)
#     i += 1

