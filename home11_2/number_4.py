# Задача 1
# Напишите декоратор, который проверяет, что все числа,
# возвращаемые декорируемой функцией, являются целыми,
# и округляет их до целых, если это не так.

def check_integers(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        # Проверка на тип с использованием type()
        if type(result) == float:
            return round(result)
        elif type(result) in (list, tuple):
            rounded = [round(x) if type(x) == float else x for x in result]
            # Возвращаем тот же тип, что и исходный (list или tuple)
            return type(result)(rounded)
        else:
            return result
    return wrapper


# Задача 2
# Напишите декоратор, который повторно вызывает
# декорируемую функцию три раза. Каждый раз через три секунды,
# если произошла ошибка.

import time

def retry(func):
    def wrapper(*args, **kwargs):
        for i in range(3):
            try:
                return func(*args, **kwargs)
            except:
                time.sleep(3)
        raise Exception('Function call failed after multiple retries.')
    return wrapper

# Задача 3
# Напишите декоратор, который позволяет возвращать
# элементы декорируемой функции по одному через yield
# если эта функция возвращает список или кортеж.

def yield_items(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        # Проверка на тип с использованием type()
        if type(result) in (list, tuple):
            for item in result:
                yield item
        else:
            yield result
    return wrapper

# Задача 4
# Напишите декоратор, который берет результат декорируемой функции
# (текст) и возвращает текст, в котором каждое слово
# сокращено до 8 символов. Если слово было сокращено,
# в конце слова ставится точка.

def shorten_words(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        words = result.split()
        shortened_words = []
        for word in words:
            if len(word) > 8:
                shortened_word = word[:8] + "."
                shortened_words.append(shortened_word)
            else:
                shortened_words.append(word)
        return " ".join(shortened_words)
    return wrapper

# Задача 5
# Напишите три декоратора, которые можно применять
# последовательно к результату декорируемой функции.


# Первый декоратор
# должен заменять в тексте, который выдает функция,
# все восклицательные знаки ! на !!!

def exclamation_marks(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.replace("!", "!!!")
    return wrapper

# Второй декоратор
# должен заменять в тексте, который выдает функция,
# все знаки вопроса ? на ???

def question_marks(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.replace("?", "???")
    return wrapper

# Третий декоратор
# должен заменять в тексте, который выдает функция,
# все точки . на ...

def dots(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.replace(".", "...")
    return wrapper

# Вызов декораторов:
@exclamation_marks
@question_marks
@dots
def my_function():
    return "This is a sentence. It has a question? Does it need more exclamation!"

print(my_function())