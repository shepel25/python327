# num1 = int (input("Введите первое число"))
# num2 = int (input("Введите второе число"))
# num3 = int (input("Введите третье число"))
# num4 = int (input("Введите четвертое число"))
# sum1 = num1 + num2
# sum2 = num3 + num4
# res = sum1 / sum2
# print (round (res))
#
# a = int (input("Введите первую сторону треугольника"))
# b = int (input("Введите вторую сторону треугольника"))
# c = int (input("Введите третью сторону треугольника"))
# if
#
# month = int(input("Введите номер месяца"))
# if 1 <= month <= 2 or month == 12:
#     print("Зима")
#     if 3 <= month <= 5:
#         print("Весна")
#         if 6 <= month <= 8:
#             print("Лето")
#             if 9 <= month <= 11:
#                 print("Осень")
# else:
#     print("Ошибка ввода")
import math
# number = int(input("Введите пятизначное число :"))
# f = number
# e = number % 10
# # print(e)
# number = number // 10
# d = number % 10
# # print(d)
# number = number // 10
# c = number % 10
# # print(c)
# number = number // 10
# b = number % 10
# # print(b)
# a = number // 10
# # print(a)
# summ = a + b + c + d + e
# print("Произведение цифр введенного числа", f, ":", summ)
# res = summ / 5
# print("Среднее арифметическое числа", summ, ":", res)

# num = int(input("Введите число отn 1 до 99 : "))
# if 0 <= num <= 99:
#     if 11 <= num <= 14:
#         print(num, "Копеек")
#     elif (num % 10) == 1:
#         print(num, "Копейка")
#     elif 2 <= (num % 10) <= 4:
#         print(num, "Копейки")
#     else:
#         print(num, "Копеек")
# else:
#     print("Введено неверное значение")

# Занятие 4

# Вложенные циклы

# i = 1
# while i < 5:
#     print("Внешний цикл: i =", i)
#     j = 1
#     while j < 4:
#         print("\tВнутренний цикл: j =", j)
#         j += 1
#     i += 1

# i = 1
# while i < 10:
#     j = 1
#     while j < 10:
#         print(i, "*", j, "=", i * j, end="\t\t")
#         j += 1
#     print()
#     i += 1

# i = 1
# while i <= 5:
#     j = 1
#     while j <= 16:
#         if i % 2 :
#             print("+", end="")
#         else:
#             print("-", end="")
#         j += 1
#     print()
#     i += 1

# i = 1
# while i <= 5:
#     j = 1
#     while j <= 16:
#         if j % 2:
#             print("+", end="")
#         else:
#             print("-", end="")
#         j += 1
#     print()
#     i += 1

# for element in collection:
#  тело цикла

# for i in "Hello":
#     print(i)

# for color in 'red', 'blue', 'green':
#     print(color)

# for element in range(start, stop, step):

# print(range(5))

# for i in range(1, 15, 2):
#     print(i, end="")
# print()
#
# i = 1
# while i < 15:
#     print(i, end="")
#     i += 1
#
# a = int(input("Введите целое число:"))
# for i in range(1, a + 1):
#     if a % i == 0:
#         print(i, end=" ")

# for i in range(1, 100):
#     if i % 10  == i // 10:
#         print(i, end=" ")

# for i in range(3):
#     print(i)
# else:
#     print("Done")
#
# for i in range(3):
#     print(i)
#     if i == 1:
#         break
# else:
#     print("Done")
#
# for i in range(3):
#     print("+++")
#     for j in range(2):
#         print("-----")

# w = int(input("Введите ширину прямоугольника"))
# h = int(input("Введите высоту прямоугольника"))
# for i in range(h):
#     for j in range(w):
#         if i == 0 or j == 0 or i == h - 1 or j == w - 1:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()


# a = [letter * 2 for letter in "Hello"]
# print(a)

# num = [i for i in range(20)]
# print(num)
#
# num = [i for i in range(20) if i % 2 == 0]
# print(num)

# Список (List)

# nums = [8, 3, 4, 1, 9, "Hello", 2.5]
# print(nums)
# print(type(nums))
# print(nums[0])
# print(nums[6])
# print(nums[-1])
# print(nums[3])
# nums[3] = 256
# nums[0] += 108
# print(nums)
#
# print(len(nums)) # len длина списка

# s = []
# print(s)
#
# b = list("Hello")
# print(b)
# print(type(b))

# n = list(range(10))
# print(n)

# a = [0 for i in range(5)]
# print(a)

# a = [i for i in range(5)]
# print(a)
#
# n = 5
# a = [i ** 2 for i in range(n)]
# print(a)
#
# a = [i * 3 for i in "list"]
# print(a)
#
# a = [1, 2, 3]
# b = [4, 5]
# c = a + b
# print(c)
# d = c * 3
# print(d)

# a = [0] * int(input("Кол-во элементов в списке"))
# print(a)
# for i in range(len(a)):
#     a[i] = input("->")
#
# print(a)

# a = [input("->") for i in range(int(input("Кол-во элементов в списке: ")))]
# print(a)

# a = ['один', 'два', 'три', 'четыре', 'пять']
# for i in range(len(a)):
#     print(a[i], end=" ")
# print()

# for el in a:
#     print(el, end=" ")

# a =[int(input('->')) for i in range(int(input("n =")))]
# print(a)
# s = 0
# # for i in range(len(a)):
# #     if a[i] < 0:
# #         s += a[i]
#
# for i in a:
#     if i < 0:
#         s += i
# print("Сумма отрицательных элементов: ", s)

# n = list(range(21, 41))
# print(n)
# k = s = 0
# for i in range(len(n)):
#     if n[i] % 2 == 0:
#         k += 1
#
#     else:
#         s += n[i]
#
# print("Кол-во четных элементов: ", k)
# print("Сумма нечетных элементов: ", s)

# a = [int(input("->")) for i in range(int(input("n = ")))]
# print(a)
# for i in range(1, len(a)):
#     if a[i] > a[i - 1]:
#         print(a[i], end=" ")

# a = [int(input("->")) for i in range(int(input("n = ")))]
# print(a)
# summ = s = 0
# for i in range(len(a)):
#     if a[i] > 0:
#         s += 1
#     summ += a[i]
# arif_mean = summ / s
#
# print ("Среднее арифметическое: ", arif_mean)
# print("Сумма не нулевых элементов: ", summ)
# print("Кол-во элементов: ", s)

# Занятие 5

# Модули

# import math
#
# num1 = math.sqrt(4)
# num2 = math.ceil(3.2)
# num3 = math.floor(3.8)
# num4 = math.pi
# print(num1)
# print(num2)
# print(num3)
# print(num4)

# псевдоним

# import math as m
#
# num2 = m.ceil(3.2)
# num3 = m.floor(3.8)
# print(num2)
# print(num3)

# from math import ceil, floor
#
# num2 = ceil(3.2)
# num3 = floor(3.8)
# print(num2)
# print(num3)

# import time
# import locale

# sec = time.time()
# print(sec)
# local = time.ctime()
# print(local)
# res = time.localtime()
# print(res)
# print(res.tm_year)
# print(res.tm_mon)

# locale.setlocale(locale.LC_ALL, "ru")

# print(time.strftime("Today is %b %d %Y", time.localtime(789878098)))
# print(time.strftime("Today is %b %d %Y"))
# print(time.strftime('%d/%m/%y, %H:%M:%S'))

# print("Программа запустилась...")
# time.sleep(5)# sleep приостанавливает выполнение программы на заданное кол-во секунд
# print("Программа завершилась")
#
# start = time.time()
# time.sleep(5)
# finish = time.time()
# print("Время выполнения программы", finish - start, "секунд"

# start = time.monotonic()
# time.sleep(5)
# finish = time.monotonic()
# print("Время выполнения программы", finish - start, "секунд")

# Срезы: список (start:stop:step)

# s = [5, 9, 3, 7, 1, 8]
# print(s[::-1])
# print(s[0:-1:2])
# print(s[0:6:1])

# s = [1, 2, 3, 4, 5, 6, 7]
# print(s[::-1])
# print(s[::2])
# print(s[1::2])
# print(s[0:1:])
# print(s[6::])
# print(s[-1:])
# print(s[3:4:])
# print(s[3:])
# print(s[4:1:-1])
# print(s[2:5])

# s = [1, 2, 3, 4, 5, 6, 7]
# print(s)
# ...
# s [1:3] = [0, 0, 0, 0]
# print(s)
# s[1:2] = [20]
# print(s)
# s[3:5] = []
# print(s)
# del s[:]
# print(s)

# Методы списков

# s = [1, 2, 3, 4, 5, 6, 7]
# s[6] = 8
# print(s)
# s.append(99) # Добавляет один элемент в конец списка
# s.extend([8, 9, 10]) # Добавляет в список набор элементов
# s.extend("add") # Добавляет строчные элементы побуквенно
# s.insert(0, 100) # Добавляет элемент в заданный индекс со сдвигом элементов
# # Первый параметр индекс второй параметр добавляемый элемент
# print(s)

# s = []
# n = int(input("Кол-во элементов в списке: "))
# for num in range(n):
#     x = int(input("Введите число: "))
#     s.append(x)
# print(s) # [1, 2, 3]

# s = []
# n = int(input("Кол-во элементов в списке: "))
# for num in range(n):
#     x = int(input("Введите число: "))
#     s.insert(0, x)
# print(s) # [3, 2, 1]

# s = []
# n = int(input("Кол-во элементов в списке: "))
# for num in range(n):
#     x = int(input("Введите число: "))
#     if x % 3 == 0:
#         s.append(x)
#     else:
#         print(x, "Данное число не делится на 3 без остатка")
# print(s)

# a = [5, 9, 2, 1, 4, 3]
# b = [4, 2, 1, 3, 7]
# c = []
# for i in a:
#     for j in b:
#         if i in c:
#             continue
#         if i == j:
#             c.append(i)
#             break
# print(c)

# a = [1, 2, 3]
# b = [11, 22, 33]
# c = []
#
# for i in range(len(a)):
#     c.append(a[i])
#     c.append(b[i])
#
# print(c)

# a = [1, 2, 3, 44, 55]
# b = [11, 22, 33]
# c = []
# if len(b) > len(a):
#     for i in range(len(a)):
#         c.append(a[i])
#         c.append(b[i])
#     for i in range(len(a), len(b)):  # range(3,5)
#         c.append(b[i])
# else:
#     for i in range(len(b)):
#         c.append(a[i])
#         c.append(b[i])
#     for i in range(len(b), len(a)):  # range(3,5)
#         c.append(a[i])
# print(c)

# a = [1, 2, 3, 44, 55]
# b = [11, 22, 33]
# c = []
# if len(a) > len(b):
#     a, b = b, a
# for i in range(len(a)):
#     c.append(a[i])
#     c.append(b[i])
# for i in range(len(a), len(b)):  # range(3,5)
#         c.append(b[i])
#
# print(c)

# s = [4, 0, 2, 0, 3, 6, 8, 0, 7]
# s.remove(0) # Удаляет первый найденный элемент из списка по значению
# print(s)
# last = s.pop(-3) # Удаляет последний элемент из списка если не указывать индекс
# print(last)
# print(s)
# s.clear()
# print(s) # Очищает список полностью
#
# a = [int(input("->")) for i in range(int(input("n = ")))]
# print(a)
# print("Введите индекс: ")
# k = int(input("k= "))
# a.pop(k)
# print(a)

# s = [4, 0, 2, 0, 3, 6, 8, 0, 7]
# print(s)
# # num = s.count(5) # Считает кол-во заданных элементов в списке
# # print(num)
# ind = s.index(0, 2) # Возвращает индекс первого найденного элемента по его значению , если значения нет ValueError
# print(ind)

# s = []
# a = [int(input("->")) for i in range(int(input("n = ")))]
#
# print("Список:", a)
#
# for num in a:
#     # print(num)
#     if num > 0:
#         s.append(num)
# print("Список положительных элементов: ", s)
#
# max_num = max(s)
# print("Наибольшее число: ", max_num)


# Занятие 6

# a = [1, 2, 3]
# # b = a
# b = a.copy()
# print("a =", a, id(a))
# print("b =", b, id(b))
# a.append(20)
# print("a =", a, id(a))
# print("b =", b, id(b))
# b.append(30)
# print("a =", a, id(a))
# print("b =", b, id(b))

# a = [1, 2, 3]
# a.reverse() # revers - перестраивает элементы в обратном порядке
# print(a)

# s = [9, 7, 3, 6, 4, 2, 8]
# s.sort() # sort - сортировка (по умолчанию по возрастанию)
# print(s)
# s = [9, 7, 3, 6, 4, 2, 8]
# s.sort(reverse=True) # sort - сортировка по убыванию
# print(s)
# s2 = ["Виталий", "Сергей", "Анна", "Александр"]
# # s2.sort()
# s2.sort(key=len, reverse=True)
# print(s2)

# s = [9, 7, 3, 6, 4, 2, 8]
# s.sort()
# print(s)
#
# s2 = [9, 7, 3, 6, 4, 2, 8]
# s3 = sorted(s2)
# print(s3)
# print(s2)

# Генерация случайных данных

import random
from random import *

# print(random.random())
# print(random.randint(0, 9)) # 0, 9 указанный диапазон , конечное значение включается
# print(random.randrange(1, 9, 2)) # (start , stop , step) 1, 9 диапазон , 2 - каждое второе число
# print(uniform(10.5, 25.5))
# print(round(uniform(10.5, 25.5), 2))

# city = ['Москва', 'Новосибирск', 'Воронеж', 'Сочи', 'Екактеринбург']
# # print(choice(city)) # choise - возращает один элемент
# # print(choices(city)) # choises - вовращает элемент в виде списка
# print(choices(city, k=3))
#
# s = [55, 66, 77, 88, 99, 4, 7, 9, 4, 5, 6, 1, 2, 7, 3]
# # print(choice(s))
# # print(choices(s))
# print(choices(s, k=5))

# a = [randint(50, 100) for i in range(10)]
# print(a)

# lst = [5, 3, 4, 2, 1, 8]
# print(len(lst))
# print(min(lst))
# print(max(lst))
# print(sum(lst))
#
# a = [randint(50, 100) for i in range(10)]
# print(a)
# m = max(a)
# print("Max:", m)
# a.remove(m)
# print(a)
# a.insert(0, m)
# print(a)

# a = [randint(50, 100) for i in range(10)]
# print(a)
# m = min(a)
# print("Min", m)
# ind = a.index(m)
# print(ind)
# del a[:ind]
# print(a)
# b = a[ind:]
# print(b)

# x = list('1a2b3c4d')
# print(x)
# print('a' in x)
# print('i' in x)
# print('a' not in x)
# print('i' not in x)

# lst = []
# # if len(lst) == 0:
# #     print("Список пустой")
#
# if not lst:
#     print("Список пустой")
#
# print(bool(lst))  # False

# n1 = int(input("Ввелите размер первого списка: "))
# n2 = int(input("Ввелите размер второго списка: "))
# a = [randint(0, 10) for i in range(n1)]
# b = [randint(0, 10) for _ in range(n2)]
# print("Первый список: ", a)
# print("Второй список: ", b)
# # c = a + b
# # print("Третий список:", c)
# c = []
# for i in range(len(a)):
#     if a[i] not in c:
#         c.append(a[i])
# for i in range(len(b)):
#     if b[i] not in c:
#         c.append(b[i])
#
# print("Третий список: ", c)
#
# c = []
# for i in range(n1):
#     if a[i] in b and a[i] not in c:
#         c.append(a[i])
#
# print("Третий список: ", c)
#
# c = [min(a), min(b), max(a), max(b)]
# print("Третий список: ", c)

# Вложенные списки

# m = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12]
#
# ]
# print(m)
# print(len(m))
# print(m[1][2])
#
# s = ["Hello", 2]
# print(s[0][1])

# m = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12]
# ]
# print(m)
# print()
# for row in range(len(m)):
#     print(m[row])
#     for cel in range(len(m[row])):
#         print(m[row][cel], end="\t\t")
#     print()
# for row in m:
#     # print(row)
#     for x in row:
#         print(x, end="\t\t")
#     print()

# for x, y in [[1, 2], [3, 4], [5, 6], [7, 8]]:
#     print(x, "+", y, "=", x + y)

# w, h = 5, 4
# matrix = [[randint(1, 30) for x in range(w)] for y in range(h)]
# for row in matrix:
#     for x in row:
#         print(x, end="\t\t")
#     print()

# w, h = 3, 4
# s = 0
# matrix = [[randint(-30, 30) for x in range(w)] for y in range(h)]
# for row in matrix:
#     for x in row:
#         if x < 0:
#             s += 1
#         print(x, end="\t\t")
#     print()
# print(s)


# matrix2 = [randint(0, 10) for i in range(6)]
#
# w, h = 6, 6
#
# matrix = [[randint(0, 10) for x in range(w)] for y in range(h)]
#
# for row in matrix:
#     for x in row:
#
#         print(x, end="\t\t")
#         # print(x, end="\t\t")
#     print()
#
# for i in range(len(matrix)):
#     # print(i)
#     if i % 2 != 0:
#         del (matrix[i])
#         matrix.insert(i, matrix2)
#
# print(matrix2, end="\t\t")
# print()
#
#
# matrix3 = matrix.copy()
#
# for row in matrix:
#     for x in row:
#
#         print(x, end="\t\t")
#
#     print()

#
# lst = [randint(0, 10) for i in range(10)]
# if lst[i] == lst[i]+1:
#
# print(lst)

# Функции

# def hello(): # Принимаемые аргументы
#     print("Hello")
#
#
# hello()


# def hello(name, word):
#     print(("Hello", name, "Say", word))
#
#
# hello("Irina", "hi") # Параметры
# hello("Ivan", "hello")

# def get_sum(a, b):
#     print(a + b)
#
#
# m = 2
# n = 3
# get_sum(m, n)
# c = 5
# d = 6
# get_sum(c, d)
# get_sum(2, 3)
# get_sum("1", "2")

# def symbol(count, a, b):
#     for i in range(count): # i= 0,1,2,3,4,5,6,7
#         if i % 2 == 0:
#             print(a, end="")
#         else:
#             print(b, end="")
#     print()
#
# symbol(9, "+", "-")
# symbol(7, "X", "Y")
#
#
# def get_sum(a, b):
#     return a + b
#
#
# n = 2
# m = 3
# res = get_sum(n, m)
# print(res ** 2)


# def add(x, y):
#     if x > y:
#         return  x - y
#     # else:
#     #     return x + y
#     return x + y # Вариант 2 без else
# a = int(input("a =",))
# b = int(input("b ="))
# m = add(a, b)
# print("результат:", m)


# def cube(a):
#     return a*a*a
# for i in range(1, 11):
#     print(i, "В кубе", cube(i))


# def change(lst):
#     lst[0], lst[-1] = lst[-1], lst[0]
#     return lst
#
#
# print(change([1, 2, 3]))
# print(change([9, 12, 33, 54, 105]))
# print(change(['с', 'л', 'о', 'н']))


# def change(lst):
#     a = lst.pop()
#     b = lst.pop(0)
#     lst.append(b)
#     lst.insert(0, a)
#     return lst
#
# print(change([1, 2, 3]))
# print(change([9, 12, 33, 54, 105]))
# print(change(['с', 'л', 'о', 'н']))


# def func(x, y):
#     if x > y:
#         return True
#     else:
#         return False
#
#
# print(func(5, 10))
# print(func(10, 5))
#
#
# a = 5
# b = 2
# if func(a, b):
#     print("Первое число больше второго")
# else:
#     print("Нет")


# def check_password(password):
#     has_apper = False
#     has_lower = False
#     has_num = False
#
#     for ch in password:
#         if "A" <= ch <= "Z":
#             has_apper = True
#         elif "a" <= ch <= "z":
#             has_lower = True
#         elif "0" <= ch <= "9":
#             has_num = True
#
#     if len(password) >= 8 and has_apper:
#         return True
#     return False
#
#
# p = input("Введите пароль")
# if check_password(p):
#     print("Это надежный пароль")
# else:
#     print("Ненадежный пароль")


# Занятие 7 часть 2

# def get_sum(a, b, c, d):
#     return a + b + c + d
#
#
# print(get_sum(1, 5, 2, 7))
# print(get_sum(1, 5, 2))


# def get_sum(a, b=2, c=0, d=1):
#     return a + b + c + d
#
#
# print(get_sum(1, 5, 2, 7))
# print(get_sum(1, 5, 2))
# print(get_sum(1, d=2))
# print(get_sum(1, d=2, b=5))
# n = 2
# m = 5
# print(get_sum(1, d=n, b=m))

# def set_param(c=20, s="-"):
#     for i in range(c):
#         print(s, end="")
#     print()
#
#
# set_param(10, "+")
# set_param(5, "*")
# set_param(15, "#")
# set_param(7)
# set_param()
# set_param(s="?")

# def digits_sum(n, even=True):
#     s = 0
#     while n > 0:
#         cur_digit = n % 10
#         if even and cur_digit % 2 == 0:
#             s += cur_digit
#         elif not even and cur_digit % 2 != 0:
#             s += cur_digit
#         n //= 10
#     return s
#
#
# print("Сумма четных чифр")
# print(digits_sum(9874023))
# print(digits_sum(38271))
# print(digits_sum(123456789))
# print("Сумма нечетных чифр")
# print(digits_sum(9874023, even=False))
# print(digits_sum(38271, even=False))
# print(digits_sum(123456789, even=False))

# def display_info(name, age):
#     print("Name", name, "\nAge", age)
#
# display_info("Ira", 23)
# display_info(28, "Ira")
# display_info(age=23, name="Ira")
# display_info("Igor", age=23, name="Ira")

# типы переменных (изменяемые и не изменяемые)

# a = 5
# print(a, id(a))
# a = 6
# print(a, id(a))
#
# lst1 = [1, 2, 3]
# print(lst1, id(lst1))
# lst1.extend([4, 5, 6])
# print(lst1, id(lst1))
# lst2 = [4, 5, 6]
# print(lst2, id(lst2))

# a = "Hello"
# b = "Hello"
# print(a == b)
# print(a is b)
# print(id(a))
# print(id(b))
#
# a = [1, 2, 3]
# b = [1, 2, 3]
# print(a == b)
# print(a is b)
# print(id(a))
# print(id(b))
#
# a = 5
# b = 5
# print(a == b)
# print(a is b)
# print(id(a))
# print(id(b))

# Изменяемые типы данных - list
# Неизменяемые типы данных - int, str, float, bull

# st = "Hello"
# print(st[-1])
# st[-1] = 'o' # так изменить не получится

# st = "Hello"
# st = list(st)
# print(st[-1])
# st[-1] = "q"
# print(st)
# try:
#     sq = int(input("Введите номер: 1- прямоугольник, 2- круг, 3- треугольник"))
#     print(sq)
#     if 3 >= sq >= 1:
#         if sq == 1:
#             try:
#                 a = int(input("Введите длину стороны а: "))
#                 b = int(input("Введите длину стороны b: "))
#
#                 def rectangle(c, d):
#                     return a * b
#
#
#                 print(rectangle(a, b))
#
#             except ValueError:
#                 print("Введено неверное значение")
#         if sq == 2:
#             try:
#                 pi = round(math.pi, 2)
#                 r = int(input("Введите радиус: "))
#
#
#                 def circle(j, k):
#                     return pi * (r ** 2)
#
#
#                 print(circle(pi, r))
#             except ValueError:
#                 print("Введено неверное значение")
#         if sq == 3:
#             try:
#                 h = int(input("Введите высоту: "))
#                 w = int(input("Введите длину основания: "))
#
#
#                 def triangle(i, f):
#                     return (h * w) // 2
#
#
#                 print(triangle(h, w))
#             except ValueError:
#                 print("Введено неверное значение")
#     else:
#         print("Введено неверное число")
# except ValueError:
#     print("Введено неверное значение")

# Занятие 8

# Кортеж
#  относится к неизменяемым типам данных

# lst = [10, 20, 30]
# tpl = (10, 20, 30)
# print(type(tpl))
# print(lst.__sizeof__())
# print(tpl.__sizeof__())
a = ()

# print(type(a))
# a = 4, 5, 6, 7
# print(a)
# print(type(a))
# a = tuple("Hello")
# print(a)
# a = tuple((2, 5, 7, 9, 3))
# print(a)
# print(a[-1])
# print(a[1:3])

# s = tuple([input("=>") for i in range(5)])
# print(s)
# s = tuple(input("=>") for i in range(5))
# print(s)

# from random import randint

# s = tuple(randint(0, 10) for i in range(5))
# print(s)

# s = tuple(2 ** i for i in range(1, 13))
# print(s)

# t1 = tuple("Hello")
# t2 = tuple("world")
# t1 = t1 + t2
# print(t1)
# print(t1 * 2)
# print(t1.count('l'))
# print(t1.index('l'))
# print(t1.index('l', 3))
# ch = 'a'
# if ch in t2:
#     print(t2.index(ch))
# else:
#     print("Такого символа нет")
#
# for i in t2:
#     print(i * 2, end=" ")

# def sliser(tpl, el):
#     if el in tpl:
#         if tpl.count(el) > 1:
#             first = tpl.index(el)
#             second = tpl.index(el, first + 1)
#             return tpl[first:second + 1]
#         else:
#             return tpl[tpl.index(el):]
#
#     else:
#         return ()
#
#
# print(sliser((1, 2, 3), 8))
# print(sliser((1, 8, 3, 4, 8, 8, 9, 2), 8))
# print(sliser((1, 2, 8, 5, 1, 2, 9), 8))


# s1 = tuple(randint(0, 5) for i in range(10))
# print(s1)
#
# s2 = tuple(randint(-5, 0) for i in range(10))
# print(s2)

# def ren(a, b):
#     return tuple(randint(a, b) for i in range(10))
#
#
# tpl1 = ren(0, 5)
# tpl2 = ren(-5, 0)
# print(tpl1)
# print(tpl2)
# tpl3 = tpl1 + tpl2
# print(tpl3)
# print("0 =", tpl3.count(0))

# t = (10, 11, [1, 2, 3], [4, 5, 6], ["Hello", "world"])
# print(t, id(t))
# t[4][0] = "new"
# t[4].append("hi")
# print(t, id(t))

# Занятие 8 часть 2

# t = (1, 2, 3)
# # x = t[0]
# # y = t[1]
# # z = t[2]
# # print(x, y, z)
# x, y, z = t  # Распаковка кортежей
# print(x, y, z)

# def get_user():
#     name = "Tom"
#     age = 22
#     is_married = False
#     return name, age, is_married
#
#
# # user = get_user()
# # print(user)
# # print(user[0])
# # print(user[1])
# # print(user[2])
# # n, year, married = user
# n, year, married = get_user() # чуть проще
# print(n, year, married)


# tpl = (10, 20, 30)
# del tpl # Полностью удаляет ссылку на кортеж
# print(tpl)

# tpl = (10, 20, 30)
# lst = list(tpl) # преобразовали кортеж в список
# lst.append(40) # добавили элемент в конец списка
# print(lst)
# tpl = tuple(lst) # преобразовали список обратно в кореж
# print(tpl)

# countries = (
#     ("Германия", 86.2, (("Берлин", 3.226),("Гамбург", 1.718))),
#     ("Франция", 66, (("Париж", 2.2), ("Марсель", 1.6)))
# )
#
# for country in countries:
#     coutry_name, country_population, citties = country
#     print("\nСтрана: ", coutry_name, "Население: ", country_population, sep=" ")
#     for cyti in citties:
#         cyti_name, city_population = cyti
#         print("\nГород: ", cyti_name, "Население: ", city_population, sep=" ")


# Множество (set)

# s = {"banana", "apple", "orange", "banana", "apple"}
# print(s)
# print(type(s))
# for i in s:
#     print(i)

# a = set()
# print(a)
# print(type(a))

# s = {i f'A' + i[1:] if i[0] == 'a' else 'B' + i[1:] for i in s if i[1] == 'c']or i in range(10)} # сгенерировали множество
# print(s)

# s = {i ** 2 for i in range(10)} # сгенерировали множество
# print(s)
# print(64 in s)

# s = ['ab_1', 'ac_2', 'bc_1', 'bc_2']
# # a = {i for i in s if 'a' in i}
# # a = ['A' + i[1:] if i[0] == 'a' else 'B' + i[1:] for i in s]
# a = ['A' + i[1:] if i[0] == 'a' else 'B' + i[1:] for i in s if i[1] == 'c']
# print(a)
# for i in s:  # Расшифровка ['A' + i[1:] if i[0] == 'a' else 'B' + i[1:] for i in s if i[1] == 'c']
#     if i[1] == "c":
#         if i[0] == "a":
#             print("A" + i[1:])
#         else:
#             print("B" + i[1:])

# a = {"Tom", "Bob", "Alice"}
# a.add("Sam")  # Добавление в множество
# print(a)
# a.remove("Tom")  # Удаление элемента
# # a.remove("Ann")  # KeyError
# print(a.pop())
# a.clear()  # Удаляет данные в множестве , множество остается
# print(a)

# a = {0, 1, 2, 3}
# b = {4, 3, 2, 1}
# # c = a.union(b) # => c = a | b оператор сложения только для множества
# # print(c)
# # a |= b
# # print(a)
# a = a & b # возврашает уникальные элементы входящие только в список a
# c = a ^ b # возвращает уникальные  элементы для списков a и b
# # c = a - b # возвращает элементы входящие только в первый список
#
# print(c)

# s1 = {1, 2}
# s2 = {3}
# s3 = {4, 5}
# s4 = {3, 2, 6}
# s5 = {6}
# s6 = {7, 8}
# s7 = {9, 8}
#
# s = s1 | s2 | s3 | s4 | s5 | s6 | s7 # или s = s1.union(s2,s3,s4,s5,s6,s7)
# print(s)
# print(len(s))
# print(min(s))
# print(max(s))

# tpl1 = tuple('253523651')
# print(tpl1)
# lst = []
# for i in tpl1:
#     if i not in lst:
#         lst.append(i)
#         res = tpl1.count(i)
#         print("Количество", i, "=", res)


# Занятие 9

# s = frozenset([1, 2, 3, 4, 5])
# print(s)
# s = frozenset({"Hello", "world"})
# print(s)
# s = frozenset({i ** 2 for i in range(10)})
# print(s)


# Словарь (dict)

# lst = [1, 2, 3]
# d = {'one': 1, 'two': 2, 3: 0}
# print(type(d))
# print(lst[0])
# print(d['one'])
# print(lst[2])
# print(d[3])

# d = {}
# print(d)
# print(type(d))
#
# d1 = dict()
# print(d1)
# print(type(d1))
#
# d2 = dict(one=1, two=2)
# print(d2)
# print(type(d2))

# users = ['a', 'b', 'c', 'd', 'e', 'f']
# print(users)
# d_users = dict(users)
# print(d_users) # так преобразовать не получится , нет ключей и выскочит valueerror

# users = [('a', 'b'), ['c', 'd'], ['e', 'f']]
# print(users)
# d_users = dict(users)
# print(d_users)
#
# lst = list(d_users)
# print(lst) # Преобразует словарь в список , но выведет только список ключей

# d = {i: i ** 2 for i in range(7)}
# print(d)
# print(d[4])
# d[4] = 20
# print(d)

# d = {0: 'text', 'one': 1, (1, 2, 3): 'кортеж', 'список': [2, 3, 7, 4]}
# print(d)
# print(d[(1, 2, 3)])
# print(d['список'][2])
# Ключами не могут быть объекты с изменяемым типом данных
# Ключи одинаковыми быть не могут
# print('one' in d) # True
# print(
# 'one1' in d) # False
# print('text' in d) # False
# del d[0]
# print(d)
# print(d['one1']) # Если элемент не существует то выскочит ошибка keyerror

# d = {'one': 1, 'two': 2, 'three': 3}
# for i in d:
#     print(i) # получим ключи текущих элементов
# print(i, d[i]) # получим ключи и значения

# for key in d:
#     print(key)
#     print(key, d[key])

# key = 'four'
# if key in d:
#     del d[key]
#
# print(d)

# d = {'one': 1, 'two': 2, 'three': 3}
# key = 'four'
# if key in d:
#     del d[key]
#
# print(d)

# d = {'one': 1, 'two': 2, 'three': 3}
# key = 'three'
#
# try:
#     del d[key]
# except KeyError:
#     print("Элемента с ключом", key, "нет в словаре")
# print()

# d = {'x1': 3, 'x2': 7, 'x3': 5, 'x4': -1}
# print(d)
#
# res = 1
# for key in d:
#     res *= d[key]
#
# print(res)

# d = dict()
# d[1] = input("->")
# d[2] = input("->")
# d[3] = input("->")
# d[4] = input("->")
# d = {i: input("->")for i in range(1, 5)}
# print(d)
# dislike = int(input("Какой элемент исключить: "))
# del d[dislike]
# print(d)

# d = {'x1': 3, 'x2': 7, 'x3': 5, 'x4': -1}
# print(d)
# print(len(d))
# print(min(d))

# Занятие 9 часть 2

# goods = {
#     '1': ['Core-i3-4330', 9, 4500],
#     '2': ['core-i5-4670', 3, 8500],
#     '3': ['AMD FX-6300', 6, 3700],
#     '4': ['Pentium G3230', 8, 2100],
#     '5': ['Core-i5-3460', 5, 6800]
# }
#
# for i in goods:
#     print(i, ")", goods[i][0], "-", goods[i][1], " шт. по ", goods[i][2], "руб", sep="")
#
# while True:
#     n = input("№: ")
#     if n != '0':
#         k = int(input("Количество: "))
#         goods[n][1] += k
#     else:
#         break
#
# for i in goods:
#     print(i, ")", goods[i][0], "-", goods[i][1], " шт. по ", goods[i][2], "руб", sep="")

# d = {3: 'x1', 7: 'x2', 5: 'x3', -1: 'x4'}
# print(d)
# # print(d.keys()) #список ключей
# # print(d.values()) #список значений
# # print(d.items()) # список и ключей и значений одновременно в виде кортежа
# for i, j in d.items():
#     print(i, j)
#
# print(list(d.values())) # получим список значений
# print(list(d.items())) # получим список ключей и значений в виде кортежей

# d = {'a': 1, 'b': 2, 'c': 3}
# d2 = d.copy()
#
# d2['b'] = 5
#
# print("D =", d)
# print("D2 =", d2)

# d = {'a': 1, 'b': 2, 'c': 3}
# print(d)
# # d.update({'r': 7, 't': 9}) # update - обновление словаря
# # print(d)
# # d.update({'a': 7, 'f': 4})
# d.update([('b', 5), ('q', 4)])
# print(d)

# x = {'a': 1, 'b': 2}
# y = {'b': 3, 'c': 4}
# z = x.copy()
# print(z)
# z.update(y)
# print(z)
# z = x | y
# print(z)

# x = {'a': 1, 'b': 2}
# print(x)
# # x.clear() # clear - очищает словарь полностью
# # item = x.pop('b') # pop - удаляет ключ и значение по ключу, возвращается значение
# # item = x.pop('e', 'Такого ключа нет')
# item = x.popitem()  # popitem - удаляет последние ключ и значени и возвращает кортеж из удаляемых элементов
# print(item)
# print(x)

# d = {'name': 'Kelly', 'age': 25, 'salary': 8000, 'city': 'Ney York'}
# new_d = dict()
#
# # new_d['name'] = d.pop('name')
# # new_d['salary'] = d.pop('salary')
#
# new_d = {'name': d.pop('name'), 'salary': d.pop('salary')} # вариант 2
#
# print(d)
# print(new_d)

# d = {'name': 'Kelly', 'age': 25, 'salary': 8000, 'city': 'Ney York'}
# d['location'] = d.pop('city') # изменение названия ключа
# print(d)

# a = {
#     'first': {
#         1: 'one',
#         2: 'two',
#         3: 'three'
#     },
#     'second': {
#         4: 'four',
#         5: 'five'
#     }
# }
# print(a)
#
# for x in a:
#     print(x)
#     for y in a[x]:
#         print("\t", y, ":", a[x][y], sep="")
#
# d = {
#     'John': {'N': 3056,
#              'S': 8463,
#              'W': 2694,
#              'E': 8441
#              },
#     'Tom': {'N': 4832,
#             'S': 6786,
#             'W': 3612,
#             'E': 4737
#             },
#     'Anne': {'N': 5239,
#              'S': 4802,
#              'W': 1859,
#              'E': 5820
#              },
#     'Fiona': {'N': 3904,
#               'S': 3645,
#               'W': 2451,
#               'E': 8821
#               }
#
# }
# for x in d:
#     print(x)
#     for y in d[x]:
#         print("\t", y, ":", d[x][y], sep="")
#
# print()
#
# n = input("Введите имя:")
# s = ['John', 'Tom', 'Anne', 'Fiona']
# r = ['N', 'S', 'W', 'E']
# if n in s:
#     k = input("Введите регион продаж значение которого хотите изменить: ")
#
#     if k in r:
#         print(d[n][k])
#         new = int(input("Введите новое значение:"))
#         d[n][k] = new
#         print(d[n])
#
#     else:
#         print("Такого региона нет в списке: ", k)
#
# else:
#     print('Такого имени нет в списке:', n)


# Занятие 10

# a = ['one', 1, 2, 3, 'two', 10, 20, 'three', 15, 36, 60, 'four', -20]
# s = dict()
# n = None
#
# for i in a:
#     if type(i) == str:
#         s[i] = []   # s['one] = []
#         n = i  # n = ['one']
#     else:
#         s[n].append(i) # s['one'] = [1, 2, 3]
#
# print(s)

# # d = zip([1, 2, 3], ['one', 'two', 'three'])
# d = dict(zip([1, 2, 3], ['one', 'two', 'three'])) # {1: 'one', 2: 'two', 3: 'three'}
# s = list(zip([1, 2, 3], ['one', 'two', 'three'])) # [(1, 'one'), (2, 'two'), (3, 'three')]
# print(d)
# print(s)

# a = ['Dec', 'Jan', 'Feb']
# b = [12, 1, 2]
# f = {k: v for k, v in zip(a, b)}
# print(f)

# a = [1, 2, 3]
# c = [4.8, 8.5, 9.4]
# d = ['a', 'b', 'c']
# b = list(zip(a, c, d))
# print(b)

# dict_one = {'name': 'Igor', 'last_name': 'Doe', 'job': 'Consultant'}
# dict_two = {'name': 'Irins', 'last_name': 'Switch', 'job': 'Manager'}
#
# for (k1, v1), (k2, v2)  in zip(dict_one.items(), dict_two.items()):
#     print(k1, '->', v1)
#     print(k2, '->', v2)

# two = [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]
# a, b = zip(*two)
# print(a)
# print(b)

# one = {'appel': 8.4, 'orange': 0.55}
# two = {'paper': 0.4, 'onion': 0.35}
# print({**one, **two}) # ** - распаковка и объединение словарей

# s = ['red', 'blue', 'green']
# j = 1
# for i in s:
#     print(j, ")", i)
#     j += 1

# s = ['red', 'blue', 'green']
# # j = 1
# for j, i in enumerate(s, start=1):
#     print(j, ")", i)
# j +=


# Функции

# def func(args):
#     return args
#
# print(func(5))

# def func(*args): # *- распаковка последовательности, принимает любое кол-во параметров
#     return args
#
# print(func(5, 2, 4))
# print(func())

# def summa(*param):
#     res = 0
#     for i in param:
#         res += i
#     return res
#
#
# print(summa(1, 2, 3, 4, 5, 6, 7, 8))
# print(summa(3, 4, 5))
# print(summa('a', 'b'))  # со строчными значениями не работает


# def ch(*args):
#     avarange = sum(args) / len(args)
#     print("Среднее арифметическое: ", avarange)
#     res = []
#     for num in args:
#         if avarange > num:
#             res.append(num)
#     return res
#
#
# print(ch(1, 2, 3, 4, 5, 6, 7, 8, 9))
# print(ch(3, 6, 1, 9, 5))

# def func(a, *args):
#     return a, args
#
#
# print(func(5))  # (5, ())
# print(func(5, 6, 7, 8, 9, 0, 1))  # (5, (6, 7, 8, 9, 0, 1))

# def print_score(students, *scores):
#     print("Student:", students, end=": ")
#     for score in scores:
#         print(score, end=" ")
#     print()
#
#
# print_score("Jonathan", 100, 95, 80, 92, 99)
# print_score("Rick", 96, 20)

# def func(**kwargs):
#     return kwargs
#
# print(func(a=1, b=2, c=3)) # {'a': 1, 'b': 2, 'c': 3}
# print(func()) # {}

# def info(**kwargs):
#     for k, v in kwargs.items():
#         print(k, "is", v)
#
#
# info(name="Irina", surname="Sharma", age=22, phone=123456789)
# info(name="Igor", surname="Wood", email='fghj@mail', country='Russia', age=22, phone=1234567890)

# Занятие 10 часть 2

# def func(a, *args, d=1, **kwargs):
#     return a, args, kwargs, d
#
#
# print(func(5, 1, 2, 7, 8, 4, 6, d=7, b=2, c=0))

# Области видимости

# локальная и глобальная

# name = "Tom" # Глобальная переменная

# def hi():
#     global name
#     name = "Sam"
#     surname = "Johnatan" # Локальная переменная
#     print("Hello", name)
#
#
# def bye():
#     print("Good bye", name)
#
#
# hi()
# bye()

# i = 5
#
#
# def func(arg=i):
#     print(arg)
#
#
# i = 6
# func() # 5

# def func(a):
#     x = 2
#     return a + x
#
#
# print(func(3))

# x = 6
# def func(a):
#     x = 2
#
#     def inner():
#         x = 4
#         return a + x
#
#     return inner()
#
#
# print(func(3))

# import builtins
#
# names = dir(builtins)
#
# for t in names:
#     print(t)

# Вложенные функции

# def outer(who):
#     who = "Alexandr"
#
#     def inner():
#         print("Hello", who)
#
#     inner()
#
#
# outer("World")

# def fun1():
#     a = 6 # 2
#
#     def fun2(b):
#         a = 4  # 5
#         print("Сумма", a + b) # 6
#
#     print("a =", a) # 3
#     fun2(4) # 4
#
#
# fun1() # 1

# x = 25
#
# t = 0

# def fn():
#     global t
#     a = 30  # 35
#
#     def inner():
#         # nonlocal a # Выводит локальную переменную на уровень выше
#         a = 35
#         print("a", a)
#
#     inner()
#     t = a
#
#
# fn()
# c = x + t
# print(c)


# def fn1():
#     x = 25
#
#     def fn2():
#         x = 33
#
#         def fn3():
#             nonlocal x
#             x = 55
#
#         fn3()
#         print("fn2.x", x)
#
#     fn2()
#     print("fn1.x ", x)
#
#
# fn1()

# def outer(a1, b1, a2, b2):
#     a = 0
#     b = 0
#
#     def inner():
#         nonlocal a, b
#         a = a1 + a2
#         b = b1 + b2
#
#     inner()
#     return [a, b]
#
#
# print(outer(2, 3, -1, 4))

# Вариант 1
# def outer(a, b, c):
#     def inner(j, k):
#         return j * k
#
#     summa = 2 * (inner(a, b) + inner(b, c) + inner(a, c))
#
#     return summa
#
#
# print(outer(5, 8, 2))
#
#
# Вариант 2
# def outer(a, b, c):
#     sq = 1
#
#     def inner():
#         nonlocal sq
#         sq = 2 * ((a * b) + (b * c) + (a * c))
#
#     inner()
#
#     return sq
#
#
# print(outer(2, 4, 6))
#
# Вариант 3
#
# sq = 1
#
#
# def outer(a, b, c):
#     def inner():
#         global sq
#         sq = 2 * ((a * b) + (b * c) + (a * c))
#
#     inner()
#
#
# outer(1, 8, 6)
# print(sq)

#
# Занятие 11. Замыкание
#
# def outer(n):
#     def inner(x):
#         return n + x
#
#     return inner
#
#
# i = outer(5)
# print(i(10))
#
# def func1():
#     a = 1
#     b = "line"
#     c = [1, 2, 3]
#
#     def func2():
#         nonlocal a, b
#         c.append(4)
#         a = a + 1
#         b = b + "new"
#         return a, b, c
#
#     return func2
#
#
# func = func1()
# print(func())
#
# def func(city):
#     s = 0
#
#     def inner():
#         nonlocal s
#         s += 1
#         print(city, s)
#
#
#     return inner
#
#
# res1 = func("Москва")
# res1()
# res2 = func("Сочи")
# res2()
#
# students = {
#     "Alex": 90,
#     "Sergey": 67,
#     "Alexey": 85,
#     "Roman": 75,
#     "Danil": 54,
#     "Amdrey": 35,
#     "Mihail": 69
# }
# def make(lover, upper):
#     def inner(exam):
#         return{k: v for k, v in exam.items() if lover <= v < upper}
#
#     return inner
#
# bal_A = make(80, 100)
# bal_B = make(70, 80)
# bal_C = make(50, 70)
# bal_D = make(0, 50)
# print(bal_A(students))
# print(bal_B(students))
# print(bal_C(students))
# print(bal_D(students))
#
# def func(a, b):
#     def add():
#         return a + b
#
#     def sub():
#         return a - b
#
#     def nul():
#         return a * b
#
#     def replace():
#         print("hello")
#
#     replace.add = add
#     replace.sub = sub
#     replace.nul = nul
#     return replace
#
#
#
# obj1 = func(5, 2)
# print(obj1.add())# сумма
# print(obj1.sub())# разность
# print(obj1.nul())# произведение
#
# анонимные функции (лямбда выражения)
#
# def suma(x, y):
#     return x + y
#
#
# print(suma(1, 2))
#
# print((lambda x, y: x + y)(1, 2))
# print((lambda x=5, y=7: x + y)())
# print((lambda *args: sum(args))(1, 7, 8, 9))

# from math import pow

# print((lambda *args: sum(args))(1, 7, 8, 9))

# lst = [2, 8, 12, 5, 10]
#
# lst = [3, 5, 7, 3, 9, 5, 7, 2]
# print(lst)
# print()
# s = list(map(lambda x: x ** 2, lst))
# print(s)
# s1 = list(map(lambda x: x ** 3, lst))
# print(s1)

# c = (lambda x: x ** 2,  # кортеж из лямбда выражений
#      lambda x: x ** 3)
#
# for t in c:
#     print(t("abc"))


# Занятие 11 часть 2
#
# a = lambda x, y: x + y # так использовать не рекоменжуется
#
# print(a(1, 2))
#
# c = (lambda x: x * 2, # кортеж из лямбда выражений
#      lambda x: x * 3,
#      lambda x: x * 4)
#
# for t in c:
#     print(t("abc "))
#
# def outer(n):
#     def inner(x):
#         return x + n
#
#     return inner
#
#
# f = outer(42)
# print(f(1))
#
# def outer1(n):
#     return lambda x: x + n
#
# f1 = outer1(42)
# print(f1(1))
#
# outer2 = lambda n: lambda x: x + n
#
#
# f2 = outer2(42)
# print(f2(1))
#
# print((lambda n: lambda x: x + n)(42)(1))
#
# print((lambda a: lambda b: lambda c: a + b + c)(2)(4)(6))
#
# d = {"c": 10, "a": 15, "b": 4}
# # d = sorted(d) # этот метод не подходит для словаря
# # print(d)
# q = list(d.items())
# print(q)
# # q.sort(key=lambda i: i[1], reverse=True) #reverse=True делает сортировку по убыванию , без него по возрастанию

# def sort_val(i):
#     return i[1]


# # q.sort(key=sort val,reverse=True) #  сверху функция sort_val
# print(q)
# d1 = dict(q)
# print(d1)
#
#
# players = [
#     {"name": "Антон", "last name": "Бирюков", "rating": 9},
#     {"name": "Алексей", "last name": "Бодня", "rating": 10},
#     {"name": "Федор", "last name": "Сидоров", "rating": 4},
#     {"name": "Михаил", "last name": "Семенов", "rating": 6}
# ]
#
# res = sorted(players, key=lambda item: item["last name"])
# print(res)
#
# res2 = sorted(players, key=lambda item: item["rating"], reverse=True)
# print(res2)
#
# a = [(lambda x, y: x + y), (lambda x, y: x - y), (lambda x, y: x * y), (lambda x, y: x / y)]
# b = a[3](12, 5)
# print(b)
#
# d = {
#     1: lambda: print("Понедельник"),
#     2: lambda: print("Вторник"),
#     3: lambda: print("Среда"),
#     4: lambda: print("Четверг"),
#     5: lambda: print("Пятница"),
#     6: lambda: print("Суббота"),
#     7: lambda: print("Воскресенье")
# }
#
# d[2]()

d = [
    {"name": "Jennifer", "final": 95},
    {"name": "David", "final": 92},
    {"name": "Nicolas", "final": 98}
]

res = sorted(d, key=lambda item: item["final"])
print(res)

res2 = sorted(d, key=lambda item: item["final"], reverse=True)
print(res2)
#
#
# Готовые функции
#
# map (func, iter), filter(func, iter)
#
# def nult(t):
#     return t * 2
#
#
# lst = [2, 8, 12, 5, 10]
#
# a = list(map(nult, lst))
# a = list(map(lambda t: t*2, [2, 8, 12, 5, 10]))
# print(a)

# t = (2.88, -1.75, 100.55)
# t2 = tuple(map(lambda x: int(x), t))
# print(t2)
# t3 = tuple(map(int, t))
# print(t3)
#
# st = ['a', 'b', 'c', 'd', 'e']
# num = [1, 2, 3, 4, 5]
#
# res = list(map(lambda x, y: (x, y), st, num))
# print(res)
#
# l1 = [1, 2, 3]
# l2 = [4, 5, 6]
#
# l3 = list(map(lambda x, y: x + y, l1, l2))
# print(l3)
#
# # filter(func, iter)
#
# t = ('abcd', 'abc', 'cdert', 'def', 'gfi')
# t2 = tuple(filter(lambda s: len(s) == 3, t))
# print(t2)
#
# def args_decorator(fn):
#     def wrap(arg1, arg2):
#         print(arg1, arg2)
#         fn(arg1, arg2)
#
#     return wrap
#
#
# @args_decorator
# def print_full_name(first, last):
#     print("меня зовут", first, last)
#
#
# print_full_name("Ирина", "Резникова")
#
# def argd_decorator(fn):
#     def wrap(*args, **kwargs):
#         print("args", args)
#         print("kwargs", kwargs)
#         fn(*args, **kwargs)
#
#
#     return wrap
#
#
# @argd_decorator
# def print_full_name(a, b, c, study="Python"):
#     print(a, b, c, "изучает", study, "\n")
#
#
# print_full_name("Борис","Елизавета", "Светлана", study="JawaScript")
# print_full_name("Владимир", "Екатерина","Виктор")
# def decor(args1, args2):
#     def args_dec(fn):
#         def wrap(x, y):
#             print(args1, x, args2, y, "=", end="")
#             fn(x, y)
#
#         return wrap
#     return args_dec
#
# @decor("Сумма:", '+')
# def summa(a, b):
#     print(a+b)
#
# @decor("Разность:", '-')
# def sub(a, b):
#     print(a-b)
#
# summa(5, 2)
# sub(5, 2)
#
# Создать декоратор который будет принимать в виде аргумента число которое будет умножаться на число принимаемое функцией
#
# def multiply(arg): #3
#     def outer(func):
#         def wrap(*args, **kwargs):
#             return arg * func(*args, **kwargs)
#
#         return wrap
#     return outer
#
#
# @multiply(3)
# def return_num(num):
#     return num
#
#
# print(return_num(5))
#
# Проверка типов данных
# def typed(*args, **kwargs):
#     def outer(fn):
#         def wrap(*f_args, **f_kwargs):
#             for i in range(len(args)):
#                 if type(f_args[i]) != args[i]:
#                     raise TypeError("Неверный тип данных")
#
#
#             for k in kwargs:
#                 if type(f_kwargs[k]) != kwargs[k]:
#                     raise TypeError("Неверный тип данных", f_kwargs[k])
#             return fn(*f_args, **f_kwargs)
#
#             return fn(*f_args, **f_kwargs)
#         return wrap
#     return outer
#
# @typed(int, int, int)
# def typed_fn(x, y, z):
#     return x * y * z
#
#
# @typed(str, str, str)
# def typed_fn2(x, y, z):
#     return x * y * z
#
#
# @typed(str, str, z=int)
# def typed_fn3(x, y, z="Hello"):
#     return (x * y) * z
#
#
# print(typed_fn(3, 4, 5))
# # print(typed_fn(3, 4, "!"))
#
# print(typed_fn2("Hello", "hello", "!"))
#
# print(typed_fn3("Hello", "hello", z=5))
#
#
# Системы исчислений
#
# print(int("100", 2))
# print(int("100", 8))
# print(int("100", 16))
#
# print(bin(10)) #0b1010
# print(oct(18)) #0o22
# print(hex(18)) #0x12
#
# print(0b1010)
# print(0o22)
# print(0x12)
#
# Префиксы строк
#
# print("C:\folder\file.txt")
# print("C:\\folder\\file.txt") #чтобы отображался надо экранировать
# print(r"C:\folder\file.txt") # можно не экранировать а указать r
#
# print("C:\folder\file.txt\\"[:-1])
# print(r"C:\folder\file.txt"* '\\')
#
#
# name = "Дмитрий"
# age = 28
# print('Меня зовут', name, "мне", age, "лет", sep='')
# print('Меня зовут' + name + "мне" + str(age) + "лет", sep='')
# print(f'Меня зовут {name}. мне {age} лет.')
#
# printprint(f'Число: {round(10/3, 2)}')
#      print(f'Число: {10/3:.2f}')
#
#
# print("Hello Github")
#
# print("Все получилось")
#
# print("Стока созданная в новом репозитории")
#
# Занятие 14
#
# def avg(fn):
#      def wrap(*args):
#          # a = ""
#          # for i in args: # Вариант 1
#          #     a += str(i) + ", "
#          a = ", ".join(map(str, args)) # Вариант 2
#          print("Среднее арифметическое:", a[:-2], "=", fn(*args)/len(args))
#
#      return wrap
#
# @avg
# def summa(*args):
#      a = ""
#      for i in args:
#           a += str(i) + ", " # 2,3,3,4,
#      print("Сумма чисел:", a[:-2], "=", sum(args))
#      return sum(args)
#
#
# summa(2, 3, 3, 4)
#
# print("Строка разделенная пробелами:".split()) # Разбивает стоку на список подстрок
# print("www.python.org.ru".split(".", 2))
# print("www.python.org.ru".rsplit(".", 2))
# print("     ру".lstrip()) # Убирает пробелы слева до первого символа
# print("ру    ".rstrip())# Удаляет пробельные символы справа
# print("    ру   ".strip())
# print("http://www.python.org".lstrip("/:pths"))
# print("http://www.python/.org".lstrip("/:pths").rstrip("org"))
# print("http://www.python/.org".strip("/:pthsorg"))
#
# s = "Я изучаю Nython. Мне нравится Nython. Nython очень интересный язык программирования"
# print(s.replace('Nython', 'Python', 2)) #Поиск и замена
#
# join - Преобразует итерируемый обьект в строку
# s = '_'
# seq = ('a','b','c')
# print(s.join(seq))
#
# print("...".join(['1', '99']))
#
# a = input("->").split()
# print(a)
#
# a = input("Введите ФИО: ").split()
# print(a)
# print(f'{a[0]} {a[1][0]}. {a[2][0]}.')
#
# Занятие 14 часть 2
#
# Регулярные выражения
#
# import re
#
# # s = "Я ищу совпадения в 2023 году. И я их найду в 2 счёта."
# # reg = 'совпадения'
# # print(re.findall(reg, s)) # findall возвращает список всех найденных совпадений
# # print(re.search(reg, s)) # Возвращает первое совпадение с искомым шабдоном
# # print(re.search(reg, s).span())
# # print(re.search(reg, s).start())
# # print(re.search(reg, s).end())
# # print(re.search(reg, s).group())
# # print(re.match(reg, s).)# Возвращает первое совпадение с искомым шаблоном только в начале строки
#
# import re
#
# # s = "Я ищу совпадения в 2023 году. И я их найду в 2 счёта."
# # reg = ' '
# # ...
# # s = "Я ищу совпадения в 2023 году. И я их найду в 2 счёта."
# # reg = '[иае]'
# # ...
# # print(re.split(reg, s, 5))
#
# # Метод для поиска и замены
# #
# # s = "Я ищу совпадения в 2023 году. И я их найду в 2 счёта."
# # reg = '\\.'# reg = r'.'
# #
# # print(re.findall(reg, s))# findall возвращает список всех совпадений или []
# # print(re.search(reg, s))# search возвращает первое совпадение с искомым шаблоном
# # print(re.search(reg, s).span())
# # print(re.search(reg, s).start())
# # print(re.search(reg, s).end())
# # print(re.search(reg, s).group())
# # print(re.match(reg, s))#match возвращает первое совпадение с искомым шаблоном только в начале строки
# #
# # print(re.split(reg, s, 5))#Разбивает строку на список подстрок по заданному шаблону
# #
# # print(re.sub(reg, "!", s))
#
# # Шаблоны регулярных выражений

# s = "Я ищу совпадения в 2023 году. И [^] я их найду в 2 счёта.47896"
# reg = r'[203]'
# reg = r'[0-9]'
# reg = r'[12][0-9][0-9][0-9]'#[2023]
# reg = r'[а-яё]'
# reg = r'[А-ЯЁа-яё]'
# reg = r'[\[^\].]'
# reg = r'[^0-9]'

# ...
#
# print(re.findall(reg, s))
# print(ord("А"))
# print(ord("Я"))
# print(ord("я"))

# s = "Час в24-часовом формате от 00 до 23. 2021-06-15:21:45. Минуты в диапазоне от 00 до 59. 2021-06-15:01:09 "
# reg = r'[0-2][0-9]:[0-5][0-9]'
# print(re.findall(reg, s))

# s = "Я ищу совпадения в 2023 году. И [^] я их найду в 2 счёта.47896"
# reg = r'\AЯ ищу'
# # reg = r'\d\w\s'
#
# print(re.findall(reg, s))
# \d - одна любая ц))ифра
# \w - буквы, цифры, символ подчеркивания
# \s - символ пробельный , табуляция , перенос на другую строку
# \D\W\S - в верхнем регистре выполняет противоположное действие букве в нижнем регистре

# Занятие 16

import re
import time

# s = "05-03-1987 # Дата рождения"
# print("Дата рождения:", re.sub("#.*", " ",s))
# # Дата рождения : 05.03.1987
# print("Дата рождения:", re.sub("-", ".", re.sub("#.*", " ",s )))
# print("Дата рождения:", "05.03.1987")

# s = "12 сентября 2023 год"
# print(re.findall(req, s)) # получим число 2023 т,к искали четырехзначное число
# req = r'\d{4}'

# s = "12 сентября 2023 год"
# req = r'\d{2,4}' # Пробел между 2 и 4 не ставится будет ошибка
# print(re.findall(req, s)) #получили числа 12 и 2023 т,к искали числа от двух до четырех знаков

# s = "12 сентября 2023 год 4567891"
# req = r'\d{2,4}'
# print(re.findall(req, s)) # получим числа 12, 2023, 4567, 891

# s = "12 сентября 2023 год 4567891"
# req = r'\d{2,}' # '12', '2023', '4567891' от двух элементов и до бесконечного значения
# print(re.findall(req, s))

# s = "12 сентября 2023 год 4567891"
# req = r'\d{,4}'
# print(re.findall(req, s)) #['12', '', '', '', '', '', '', '', '', '', '', '2023', '', '', '', '', '', '4567', '891', '']
# цифры выводятся а вместо букв пробельные символы

# номера телефона

# s = "+7 499 456 45 76, +74994564576, 7 (499) 456 4576, 74994564576"
# reg = r"\+?7\d{10}"
# print(re.findall(reg, s))

# s = "Я ищу совпадения в 2023 году. И я их найду в 2 счета."
# # reg = r'^\w+\s\w+'
# reg = r'\w+\.$'
# print(re.findall(reg, s))

# def walidate_login(name):
#     return re.findall(r'^[A-Za-z_-]{3,16}$', name)
#
#
# print(walidate_login('Python_master'))
# print(walidate_login('@#%Pyt'))


# flags

# print(re.findall(r'\w+', '12 + й'))
# print(re.findall(r'\w+', '12 + й', flags=re.ASCII))

# text = 'Hello world'
# print(re.findall(r'\w+\+', text, flags=re.DEBUG))

# s = 'Я ищу совпадения в 2023 году. И я их найду в 2 счета'
# reg = 'я'
# print(re.findall(reg, s, re.IGNORECASE))
#
# text = """
# one
# two
# """
# print(re.findall(r'one.\w+', text))
# print(re.findall(r'one.\w+', text, flags=re.DOTALL))

# print(re.findall('one$', text))
# print(re.findall('one$', text, flags=re.MULTILINE))

# print(re.findall("""[a-z_-]+ @[a-z_-]+""", 'test@mail.ru')) # если поставить пробел после + ничего не найдет
# print(re.findall("""[a-z_-]+ @[a-z_-]+""", 'test@mail.ru', re.VERBOSE))# verbouse игнорирует пробелы
# print(re.findall("""
# [a-z_-]+# можно оставить свой комменарий
# @       # можно оставить свой комменарий
# [a-z_-]+# можно оставить свой комменарий
# """, 'test@mail.ru', re.VERBOSE))

# Занятие 16 часть 2

# text = """Python,
# python,
# PYTHON
# """
# reg = '(?im)^python'
# print(re.findall(reg, text))

# text = '<body>Пример жадного соответстия регулярного выражения</body>'
# print(re.findall('<.*?>', text)) # ленивый эелемент устанавливается чере ?
# # ленивый элемент можем сделать только у кол-ва повторений *?, +?, ??
# # {n, m}?, { ,n}?, {n, }?

# s = "12 сентября 2023 год 4567891"
# req = r'\d{2,4}?'
# print(re.findall(req, s))

# s = '<p>Изображение <img alt=картинка src=bg.jpg > - фон страницы </p>'
# # reg = r'<img.*?>'
# reg = r'<img[^>]*>'
# print(re.findall(reg, s))
#
# s = '<p>Изображение <img src=bg.jpg > - фон страницы </p>'
# # reg = r'<img.*?>'
# reg = r'<img\s*[^>]*src\s*[^>]*>'
# print(re.findall(reg, s))

# s = 'Петр, Ольга и Виталий отлично учатся!'
# reg = 'Петр|Ольга|Виталий|Николай'
# print(re.findall(reg, s))

# s = 'int = 4, float = 4.0, double = 8.0f'
# reg = r'(?:int|double)\s*=\s*\d+[.\w+]*'
# print(re.findall(reg, s))
#
# s = '127.0.0.1'
# # s = '192.168.255.255'
# # reg = r'\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}'
# reg = r'(?:\d{1,3}.){3}\d{1,3}'
# print(re.findall(reg, s))
#
# s = "Word2016, PS6, AI5"
# reg = r'(([a-z]+)(\d+))'
# print(re.findall(reg, s, re.I))

# s = '5 + 7*2 - 4'
# reg = r'\s*[+*-]\s*'
# print(re.split(reg, s))
#
# s = '5 + 7*2 - 4'
# reg = r'\s*([+*-])\s*'
# print(re.split(reg, s))

# a = '28-08-2021'
# reg = r'(0[1-9]|[12][0-9]|3[01])-(0[1-9]|1[0-2])-(19[0-9][0-9]|20[0-9][0-9])'
# print(re.findall(reg, a))

# s = "Я ищу совпадение в 2023 году. И я их найду в 2 счета"
# reg = r'(\d+)\s(\D+)'
# print(re.search(reg, s).group())
# m = re.search(reg, s)
# print(m[1])
# print(m[2])
# print(m[0])

# text = """
# Самара
# Москва
# Тверь
# Уфа
# Казань
# """
# count = 0
# def repl_find(n):
#     global count
#     count += 1
#     return f"<option value='{count}'>{n.group(1)}</option>\n"
#
# print(re.sub(r'\s*(\w+)\s*', repl_find, text))


# Занятие 17


# s = '<p>Изображение <img alt="картинка" src="bg.jpg" > - фон страницы </p>'
# # reg = r'<img.*?>'
# # reg = r'<img\s+[^>]*src\s*=\s+([\'"])(.+)\1>'
# reg = r'<img\s+[^>]*src\s*=\s+([\'"])(.+)\1>' #(?P<name>...)(?p=name)
# print(re.findall(reg, s))

# s = "Самолет прилетает 10/23/2023. Будем рады видеть вас посде 10/24/2023"
# reg = r'(\d{2})/(\d{2})/(\d{4})'
# print(re.sub(reg, r'\2.\1.\3', s))#23.10.2023

# s = "yandex.com and yandex.ru"
# reg = r'(([a-z0-9-]{2,}\.)+[a-z]{2,4})'
# print(re.sub(reg, r'http://\1', s))

# Работа файлов

# Текстовые и бинарные

# Открытие файла "Open"

# # f = open("C:/Users/New/PycharmProjects/pythonProject/test.txt")
# f = open('test.txt')
# print(f)
# print(*f)

# f = open('test.txt', 'r')
# print(f.read(3))
# f.close()
#
# f = open('test.txt', 'r')
# print(f.read())
# f.close()

# f = open('text.txt', 'r')
# print(f.readline()) #'\n'
# print(f.readline(8))
# print(f.readline())
# print(f.readline())
# f.close()

# f = open('text.txt', 'r')
# print(f.readlines(4))
# print(f.readlines())
# f.close()

# f = open('text.txt', 'r')
# for line in f:
#     print(line)
# f.close()

# Определить кол-во строк в файле

# count = 0
# f = open('text.txt', 'r')
# for line in f:
#     count+=1
# f.close()
# print(count)


# f = open('text.txt', 'r')
# print(len(f.readlines()))
# f.close()

# f = open('xyz.txt', 'w')
# f.write('Hello\nworld')
# f.close()

# f = open('xyz.txt', 'w') # w - если файл есть очистит и запишет информацию если файла нет он будет создан
# print(f.write('New text.'))
# f.close()
#
# f = open('xyz.txt', 'a') #a - дозапись в конец файла
# print(f.write('\nNew text.'))
# f.close()

# f = open('xyz.txt', 'a')
# lines = ['This is line 1', 'This is line 2']
# print(f.writelines(lines))
# f.close()

# f = open('xyz.txt', 'w')
# lst = [str(i) for i in range(1, 20)]
# print(lst)
# for index in lst:
#     f.write(index + '\t')
# f.close()

# Занятие 17 часть 2

# f = open('text2.txt', 'w')
# f.write('Замена строки в текстовом файле;\nизменить строку в списке;\nзаписать список в файл;')
# f.close()
#
# f = open('text2.txt', 'r')
# read_file = f.readlines()
# print(read_file)
# read_file[1] = "Hello world"
# print(read_file)
# f.close()
#
# f = open('text2.txt', 'w')
# f.writelines(read_file)
# f.close()

# f = open('test.txt')
# print(f.read(3))
# print(f.tell())# на какой позиции курсор
# print(f.seek(1))# перемещает курсор в заданную позицию
# print(f.read())
# print(f.tell())
# f.close()

# f = open('test.txt', 'r+')
# print(f.write("I am learning Python"))#20
# print(f.seek(3))#I am learning Python
# print(f.write('-new string-'))#12
# print(f.tell())#15
# f.close()

# with open('test.txt', 'w+') as f:
#     print(f.write('0123456789'))
#
# with open('test.txt', 'r+') as f:
#     print(f.read())

# with open('test.txt', 'r+') as f:
#     for line in f:
#         print(line[:6])

# file_name = 'res_1.txt'
# lst = [4.5, 2.8, 3.9, 1.9, 0.3, 4.33, 7.777]
#
#
# def get_line(lt):
#     lt = list(map(str, lt))
#     return ' '.join(lt)
#
#
# with open('file_name', 'w') as f:
#
#     f.write(get_line(lst))
# get_line(lst)
# print('Done!')

# with open('file_name', 'r') as f:
#     nums = f.read()
#
# print(nums) #str
#
# nums_list = list(map(float, nums.split())) #list(map(float, ['4,5, 2,8, 3,9,1.0']))
# # nums_list = nums.split()
# print(nums_list)
# # print(type(nums_list[0]))
# print(type(nums_list[0]))

# Написать функцию которая выводит слово из файла имеющее максимальную длину (или список слов если их несколько)

# def langest_words(file):
#     with open(file, 'r', encoding='UTF-8') as text:
#         w = text.read().split()
#         # print(w)
#         max_langth = len(max(w, key=len))
#         # print(max_langth)
#         res = [word for word in w if len(word) == max_langth]
#         # print(res)
#         if len(res) ==1:
#             return res[0]
#         return res
#
#
# print(langest_words('file.txt'))

# num = int(input('Введите номер удаляемой строки 1-3'))
# pos = num - 1
#
# f = open('dz17.txt', 'w')
# f.write('Замена строки в текстовом файле;\nизменить строку в списке;\nзаписать список в файл')
# f.close()
#
# f = open('dz17.txt', 'r')
# read_file = f.readlines()
# print(read_file)
# del read_file[pos]
# print(read_file)
# f.close()
#
# f = open('dz17.txt', 'w')
# f.writelines(read_file)
# f.close()

# Занятие 18

# Работа с двумя файлами

# text = 'Строка№1\nСтрока№2\nСтрока№3\nСтрока№3\nСтрока№4\nСтрока№5\nСтрока№6\nСтрока№7\nСтрока№8\nСтрока№9\nСтрока№10'
#
#
# with open('one.txt','w') as f:
#     f.write(text)
#
# read_file = 'one.txt'
# write_file = 'two.txt'
#
# with open(read_file, 'r') as fr, open(write_file, 'w') as fw:
#     for line in fr:
#         line = line.replace('Строка', 'Линия - ')
#         fw.write(line)

# Запись данных из двух файлов в третий

# read_file = 'one.txt'
# write_file = 'two.txt'
# res = 'three.txt'
#
# with open(read_file, 'r') as fr, open(write_file, 'r') as fw, open(res, 'w') as res:
#     # f1 = fr.readlines() # Вариант 1
#     # f2 = fw.readlines()
#     # print(f1)
#     # print(f2)
#     # f3 = f1 + f2
#     # res.writelines(f3)
#     for i, j in zip(fr, fw): # Вариант 2
#         print(i)
#         print(j)
#         res.write(i[:-1] + "->" + j) # Срез нужен для того чтобы убрать \n

# Модуль OS (OS_PATH)

import os

# print("Текущая директория", os.getcwd()) # Путь к файлу
# print(os.listdir()) # Список папок и файлов находящихся в текущей директории
# print(os.listdir('..')) # .. Выйти на уровень выше

# os.mkdir('folder1')# создать папку (только одну)
# os.makedirs('nested1/nested2/nested3')# создает вложенные папки

# os.remove('test.txt') # удаляет файл (совсем)
# os.remove('folder/file.txt') # Удаляет файл в папке

# os.rmdir() # Удаление папки
# os.rmdir('folder1') # Удаляет только пустую папку

# os.rename('xyz.txt','first.txt') # Переименовывает файл 1й параметр - старое название 2й новое название
# os.rename('first.txt', 'nested1/first.txt') # Перемещает файл с переименованием и без
# os.rename('folder', 'nested1/folder') # Может перемещать папку

# for root, dirs, files in os.walk('nested1', topdown=True): # если указать false пойдет наоборот с самой вложенной папки
#     print('Root:', root)
#     print('Subdirs:', dirs)
#     print('Files:', files)

# def remove_empty_dirs(root_tree):
#     print(f'Удаление пустых директорий в папке (root_tree)')
#     print('-' * 30)
#
#     for root, dirs, files in os.walk(root_tree):
#         if not os.listdir(root):
#             os.rmdir(root)
#             print(f'Директория (root) удалена')
#
#     print('-' * 30)
#
# remove_empty_dirs('nested1')


# import os.path

# print(os.path.split(r'C:\Users\New\PycharmProjects\pythonProject\nested1\nested2\two.txt'))# Разбивает путь на кортежи
# #(путь и имя документа )
#
# print(os.path.exists(r'C:\Users\New\PycharmProjects\pythonProject\nested1\nested2')) # Проверят существование указанного пути

# Занятие 18 часть 2

# print(os.path.join(r'D:\Python', 'nested1', 'nested2', 'text.txt'))

# dirs = [r'work\f1', r'work\f2\f21']
# for d in dirs:
#      os.makedirs(d)

# files = {
#      'work': ['w.txt'],
#      r'work\f1': ['f11.txt', 'f12.txt', 'f13.txt'],
#      r'work\f2\f21': ['f211.txt', 'f212.txt']
# }
# for d, file in files.items():
#      for f in file:
#           file_path = os.path.join(d, f)
#           # print(file_path)
#           open(file_path, 'w').close()
#
# file_with_text = [r'work\w.txt', r'work\f1\f12.txt', r'work\f2\f21\f211.txt', r'work\f2\f21\f212.txt']
# for file in file_with_text:
#      with open(file, 'w') as f:
#           f.write(f'Какой-то текст для файла {file} ')
#
#
# def print_tree(root, topdown):
#      print(f'Обход {root} {"сверху вниз" if topdown else "снизу вверх"}')
#      for root, dirs, files in os.walk(root, topdown=topdown):
#           print(root)
#           print(dirs)
#           print(file)
#      print('-' * 50)


# print_tree('work', topdown=False)
# print_tree('work', topdown=True)

# path = 'main.py'
# size = os.path.getsize(path) # Размер файла в байтах
# print(size // 1024, 'KB')
# ctime = os.path.getctime(path)
# print(time.strftime('%d.%m.%Y, %H:%m:%S', time.localtime(ctime)))
# print(os.path.getctime(path)) # Время создани файла в секундах
# print(os.path.getatime(path)) # Время последнего доступа к файлу
# print(os.path.getmtime(path)) # Время последнего изменения файла

# file_path = 'nested1/nested2/three.txt'

# if os.path.exists(file_path):
#      dir0, name= os.path.split(file_path)
#      atime = os.path.getatime(file_path)
#      print(f'{name}({dir0}) - Время последнего доступа к файлу', atime, 'сек')
#
# else:
#      print(f'Файл {file_path} не существует!')

# file_path = 'nested1/nested2/three.txt'
#
# print(os.path.isfile(file_path)) # Возвращает True если путь является файлом
# print(os.path.isdir(file_path)) # Возвращает True если путь является папкой

# dir_name = 'nested1'
#
# objs = os.listdir('nested1')
# print(objs)
# print(os.walk('.'))

# objs = os.listdir('nested1')
#
# for obj in objs:
#      print(obj)
#      p = os.path.join('nested1', obj)
#      # print(p)
# k = sorted(objs, key=os.path.isfile)
# print(k)
# print(objs)


# if os.path.isfile(p):
#      print(f'{obj} - file - {os.path.getsize(p)} bytes')
# else:
#      print(f'{obj} - dir')


# dir_name = "nested1"
# objs = os.listdir(dir_name)
# # print(objs)
#
# # for obj in objs:
# #      p = os.path.join('nested1', obj)
#      # if os.path.isfile(p):
#      print(sorted(objs, key=os.path.isfile))
#      else:
#           print(f'{obj} - dir')

# s = sorted( , key=os.path.isdir)
# print(s)
#
# import os
#
# # Получаем список всех файлов и папок в корневой директории
# items = "nested1"
# objs = os.listdir(items)
# print(objs)
# # Разделяем файлы и папки
# folders = []
# files = []
# for item in objs:
#      p = os.path.join('nested1', item)
#     # Если это папка, добавляем в список папок
#     if os.path.isdir(item):
#         folders.append(item)
#     # Если это файл, добавляем в список файлов
#     elif os.path.isfile(item):
#         files.append(item)
#
# # Сортируем списки папок и файлов
# folders = sorted(folders)
# files = sorted(files)
#
# # Выводим на экран список папок
# print("Папки:")
# for folder in folders:
#     print(folder)
#
# # Выводим на экран список файлов
# print("\nФайлы:")
# for file in files:
#     print(file)


#      print(f'{objs} - file - {os.path.getsize(p)} bytes')
# else:
#      print(f'{objs} - dir')


# Занятие 26 часть 2

# class MySubClass(LoggerMixin, Displayer):
#      def log(self, massage, filename=""):
#           super().log(massage, filename="subClasslog.txt")
#
# subclass = MySubClass()
# subclass.display("Строка будет печататься и сохранятся в файл")


# class Goods:
#      def __init__(self, name, weight, price):
#           print("Init Goods")
#           super().__init__()
#           self.name = name
#           self.weight = weight
#           self.price = price
#
#      def print_info(self):
#           print(f"{self.name}, {self.weight}, {self.price}")
#
#
# class MixinLog:
#      ID = 0
#
#      def __init__(self):
#           print("Init MixinLog")
#           MixinLog.ID += 1
#           self.id = MixinLog.ID
#
#      def save_sell_log(self):
#           print(f"{self.id}: товар был продан в 00:00 часов")
#
#
# class NoteBook(Goods, MixinLog):
#      pass
#
#
# n = NoteBook("HP", 1.5, 35000)
# n.print_info()
# n.save_sell_log()

# Перегрузка операторов

# 24*60*60 = 86400(кол во секунд в дне)
# class Clock:
#      __Day = 86400
#
#      def __init__(self, sec: int):
#           if not isinstance(sec, int):
#                raise ValueError("Секунды должны быть числом")
#           self.sec = sec % self.__Day
#
#
#      def get_format_time(self):
#           s = self.sec % 60
#           m = (self.sec // 60) % 60
#           h = (self.sec // 3600) % 24
#           return  f"{Clock.__get_form(h)}:{Clock.__get_form(m)}:{Clock.__get_form(s)}"
#
#      @staticmethod
#      def __get_form(x):
#           return str(x) if x > 9 else "0" + str(x)
#
#      def __add__(self, other):
#           if not isinstance(other, Clock):
#                raise ArithmeticError("Правый операнд должен быть типом Clock")
#           return  Clock(self.sec + other.sec)
#
#      def __eq__(self, other):
#           if not isinstance(other, Clock):
#                raise ArithmeticError("Правый операнд должен быть типом Clock")
#           return self.sec == other.sec
#
#      def __ne__(self, other):
#           return not self.__eq__(other)
#
# c1 = Clock(100)
# c2 = Clock(100)
# if c1 == c2:
#      print("Время одинаковое")
# else:
#      print("Время разное")
# # c4 = Clock(300)
# # c3 = c1 + c2 + c4
# # c4 += c1 + c2
# print(c1.get_format_time())
# print(c2.get_format_time())
# # print(c4.get_format_time())
# # print(c3.get_format_time())
