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

# занятие 11

# домашнее задание
# def outer(a, b, c):
#      def inner(x, y):
#           return x * y
#      s = 2*(inner(a, b) + inner(b, c) + inner(a, c))
#      return s
#
# print(outer(2, 4, 6))

 # Занятие 11. Замыкание

 # def outer(n):
 #      def inner(x):
 #           return n + x
 #
 #      return inner
 #
 # i = outer(5)
 # print(i(10))

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

# анонимные функции (лямбда выражения)

# def suma(x, y):
#     return x + y
#
#
# print(suma(1, 2))
#
# print((lambda x, y: x + y)(1, 2))
# print((lambda x=5, y=7: x + y)())
# print((lambda *args: sum(args))(1, 7, 8, 9))
#
# a = lambda x, y: x + y # так использовать не рекоменжуется
#
# print(a(1, 2))

# c = (lambda x: x * 2, # кортеж из лямбда выражений
#      lambda x: x * 3,
#      lambda x: x * 4)
#
# for t in c:
#     print(t("abc "))

# def outer(n):
#     def inner(x):
#         return x + n
#
#     return inner
#
#
# f = outer(42)
# print(f(1))

# def outer1(n):
#     return lambda x: x + n
#
# f1 = outer1(42)
# print(f1(1))

# outer2 = lambda n: lambda x: x + n
#
#
# f2 = outer2(42)
# print(f2(1))

# print((lambda n: lambda x: x + n)(42)(1))

# print((lambda a: lambda b: lambda c: a + b + c)(2)(4)(6))

# d = {"c": 10, "a": 15, "b": 4}
# # d = sorted(d) # этот метод не подходит для словаря
# # print(d)
# q = list(d.items())
# print(q)
# # q.sort(key=lambda i: i[1], reverse=True) #reverse=True делает сортировку по убыванию , без него по возрастанию
# # q.sort(key=sort val,reverse=True) # надо сверху дописать функцию
# print(q)
# d1 = dict(q)
# print(d1)


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

# a = [(lambda x, y: x + y), (lambda x, y: x - y), (lambda x, y: x * y), (lambda x, y: x / y)]
# b = a[3](12, 5)
# print(b)

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


# Готовые функции

#map (func, iter), filter(func, iter)

# def nult(t):
#     return t * 2
#
#
# lst = [2, 8, 12, 5, 10]
#
# a = list(map(nult, lst))
# print(a)

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

# def argd_decorator(fn):
#     def wrap(*args, **kwargs):
#         print("args", args)
#         print("kwargs", kwargs)
#         fn(*args, **kwargs)
#
#
#     return wrap


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

#Создать декоратор который будет принимать в виде аргумента число которое будет умножаться на число принимаемое функцией

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


# Системы исчислений

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

# Префиксы строк

# print("C:\folder\file.txt")
# print("C:\\folder\\file.txt") #чтобы отображался надо экранировать
# print(r"C:\folder\file.txt") # можно не экранировать а указать r
#
# print("C:\folder\file.txt\\"[:-1])
# print(r"C:\folder\file.txt"* '\\')


# name = "Дмитрий"
# age = 28
# print('Меня зовут', name, "мне", age, "лет", sep='')
# print('Меня зовут' + name + "мне" + str(age) + "лет", sep='')
# print(f'Меня зовут {name}. мне {age} лет.')
#
# printprint(f'Число: {round(10/3, 2)}')
#      print(f'Число: {10/3:.2f}')


# print("Hello Github")

# print("Все получилось")

# print("Стока созданная в новом репозитории")