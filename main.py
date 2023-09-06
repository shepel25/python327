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

# Занятие 16

import re


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

#номера телефона

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


#flags

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

#Занятие 16 часть 2

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


#Занятие 17


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

#Открытие файла "Open"

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

file_name = 'res_1.txt'
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
#     with open(file, 'r') as text:
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

