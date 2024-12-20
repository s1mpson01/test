# Задача 1
# Напишите декоратор, который проверяет,
# что все числа, возвращаемые декорируемой функцией,
# являются целыми, и округляет их до целых, если это не так.
# Декоратор должен принимать параметр precision,
# который указывает, до скольких цифр после запятой округлять числа.


# def check_to_int(precision):
#     def my_decorator(func):
#         def wrapper(*args, **kwargs):
#             result = func(*args, **kwargs)
#             if type(result) == float:
#                 return round(result, precision)
#             elif type(result) in (list, tuple):
#                 rounded = [round(x, precision) if type(x) == float else x for x in result]
#                 return rounded
#             else:
#                 return result
#         return wrapper
#     return my_decorator


# Задача 2
# Напишите декоратор, который повторно вызывает декорируемую
# функцию заданное количество раз через заданное время,
# если произошла ошибка. Параметры, передаваемые в декоратор,
# обязательно должны быть именованными.

# import time
# def call_back(number_of_times=3, delay=3):
#     def my_decorator(func):
#         def wrapper(*args, **kwargs):
#             for i in range(number_of_times):
#                 try:
#                     return func(*args, **kwargs)
#                 except:
#                     time.sleep(delay)
#                 raise Exception
#             return wrapper
#         return my_decorator


# Задача 3
# Напишите декоратор, который берет результат
# декорируемой функции (текст) и возвращает текст,
# в котором каждое слово сокращено до определенной длины.
# Если слово было сокращено, в конце слова ставится
# переданный символ. Количество символов
# в слове и знак в конце сокращенного слова
# — параметры декоратора, причем символ обязательно
# должен передаваться как именованный аргумент.

# def shorten_words(*, number_of_char=5, label_of_reduction="^"):
#     def wrapper(func):
#         def inner(*args, **kwargs):
#             resul = func(*args, **kwargs)
#             new_list = []
#             words = resul.split()
#             for x in words:
#                 if len(x) > number_of_char:
#                    new_word = x[:number_of_char] + label_of_reduction
#                    new_list.append(new_word)
#                 else:
#                     new_list.append(x)
#             return " ".join(new_list)
#         return inner
#     return wrapper


# Задача 4
# Напишите тесты с использованием библиотеки pytest
# для проверки корректности работы декоратора из задачи 3.

# @shorten_words(number_of_char=3, label_of_reduction="^")
# def enter_string():
#     return f"Слово"
# print(enter_string())