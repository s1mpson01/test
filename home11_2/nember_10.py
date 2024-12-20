############################################################################################
# Задача 1
# Создайте декоратор @positive_integers, который проверяет,
# что все аргументы функции — положительные целые числа.
# Если аргумент — неположительное число,
# выбрасывается исключение ValueError с сообщением
# All arguments must be positive integers.
# Пример использования:



# @positive_integers
# def multiply(*args):
#     result = 1
#     for arg in args:
#         result *= arg
#     return result

# multiply(2, 3, 4)
# Вывод: 24

# multiply(2, 0, 4)
# Выбрасывает исключение ValueError с сообщением "All arguments must be positive integers"

# def positive_integers(func):
#     def wrapper(*args):
#         result = func(*args)
#         for arg in args:
#             if arg > 0:
#                 return result
#             else:
#                 raise ValueError("All arguments must be positive integers")
#     return wrapper
#
#
# @positive_integers
# def multiply(*args):
#     result = 1
#     for arg in args:
#         result *= arg
#     return result
# print(multiply(2, 3, 4))
###############################################################################################
# Задача 2
# Создайте декоратор @is_palindrome, который проверяет,
# то аргумент функции является палиндромом
# (строкой, которая читается одинаково слева направо и справа налево).
# Если аргумент не является палиндромом, выбрасывается исключение
# ValueError с сообщением Argument must be a palindrome
# Пример использования:

# @is_palindrome
# def reverse_string(string):
#     return string[::-1]
#
# reverse_string('racecar')
#  "racecar"

# reverse_string('Racecar')
# "racecaR"

# reverse_string('hello')
# Выбрасывает исключение ValueError с сообщением
# "Argument must be a palindrome"

# def is_palindrome(func):
#     def wrapper(*args):
#         result = func(*args)
#         for arg in args:
#             if arg.lower() == arg[::-1].lower():
#                 return result
#             else:
#                 raise ValueError("Argument must be a palindrome")
#     return wrapper
#
# @is_palindrome
# def reverse_string(string):
#     return string[::-1]
#
# print(reverse_string('racecar'))
# print(reverse_string('Racecar'))
#############################################################################################################
# Задача 3
# Создайте декоратор @logging который будет логировать
# вызовы функции и ее результат. Лог должен выводиться на экран.
# Пример вывода:

# @logging
# def multiply(x, y):
#     return x * y
# multiply(2, 3)
# Function multiply called with args: (2, 3) and kwargs: {}.Result: 6

# def logging(func):
#     def wrapper(*args, **kwargs):
#         result = func(*args, **kwargs)
#         print(f"Function {func.__name__}multiply called with args:{args} and kwargs: {kwargs}. Result: {result}")
#         return result
#     return wrapper
#
#
# @logging
# def multiply(x, y):
#     return x * y
# print(multiply(2, 3))
#
# @logging
# def lists(x, y):
#     result_1 = sum(i for i in x)
#     result_2 = sum(i for i in y)
#     return result_1 + result_2
# print(lists(x= [1,2,3,4],y= [2,3,4]))
############################################################################################################

# Задача4
# Создайте декоратор @memoize  который кеширует результаты
# функции для определенных аргументов. Если функция вызывается
# с теми же аргументами, что и в предыдущий раз,она должна
# возвращать результат из кеша, а не вычислять его заново.
#
# Также создайте два дополнительных декоратора:
#
# @slowit(n) -  декоратор с параметрами, которые замедляют работу
# функции на n секунд. Без параметров декоратор замедляет функцию
# на 1 секунду. В декораторе используется функция time.sleep(n)
#
# @timeit декоратор, который выводит время работы функции.
#
# Без кеширования время работы функции при каждом вызове не менее 2 секунд.
# @timeit
# @slowit(2)
# def product(n):
#     return reduce(lambda x, y: x * y, range(1, n+1)) if n > 0 else None
#
# product(10)
# product(10)
#
# С кешированием время работы функции при первом вызове не менее 2 секунд, при втором вызове почти мгновенно.
# @timeit
# @memoize
# @slowit(2)
# def product(n):
#     return reduce(lambda x, y: x * y, range(1, n+1)) if n > 0 else None
#
# product(10)
# product(10)
from functools import reduce
from time import time

def memoize(func):
    cache_dict = {}
    def wrapper(*args):

        cache_dict[args] = func(*args)
        if args not in cache_dict:
            return func(*args)
        else:
            return func(*args)
    return wrapper

##################
from time import time
def slowit(n=1):
    def wrapper(func):
        def inner(*args, **kwargs):
            time.sleep(n)
            return func(*args, **kwargs)
        return inner
    return wrapper

###############
import time
def timeit(func):
    def wrapper(*args):
        start_time = time.time()
        result = func(*args)
        finish_time = time.time()
        result_time = finish_time - start_time
        print(result_time)
        return result
    return wrapper


@memoize
@timeit
@slowit(2) # прибавляет к результату 1 сек
def product(n):
    return reduce(lambda x, y: x * y, range(1, n+1)) if n > 0 else None

print(product(10))
print(product(10))
