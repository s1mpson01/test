import json



# import random
# Задача 1
# Напишите функцию generate_users(first_names, last_names, cities)
# которая будет генерировать случайных пользователей.
# Функция должна возвращать генератор, который будет
# выдавать каждого пользователя по одному в виде словаря.
#
# Каждый пользователь должен иметь следующие данные:
# first_name — имя из списка first_names
# last_name — фамилия из списка last_names
# age - возраст от 18 до 65 лет
# city - город из списка cities
#
# Сгенерируйте группу пользователей и
# выведите ее списком в консоль в формате JSON.


# def generate_users(first_names, last_names, cities):
#     while True:
#         user = {
#             'first_name': random.choice(first_names),
#             'last_name': random.choice(last_names),
#             'age': random.randint(18, 65),
#             'city': random.choice(cities)
#         }
#         yield user
#
# cities = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Philadelphia']
# first_names = ['John', 'Jane', 'Mark', 'Emily', 'Michael', 'Sarah']
# last_names = ['Doe', 'Smith', 'Johnson', 'Brown', 'Lee', 'Wilson']
#
# users = generate_users(first_names, last_names, cities)
#
# user_group1 = [next(users) for i in range(4)]
# user_group2 = [next(users) for i in range(6)]
# print(user_group1)


# import pytest
# from main import generate_users  # Импортируем из файла с функцией
#
# @pytest.fixture
# def data():
#     return {
#         'first_names': ['John', 'Jane', 'Mark', 'Emily', 'Michael', 'Sarah'],
#         'last_names': ['Doe', 'Smith', 'Johnson', 'Brown', 'Lee', 'Wilson'],
#         'cities': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Philadelphia']
#     }
#
# def test_generate_users_num_users(data):
#     """Проверяет, что количество сгенерированных пользователей равно запрошенному количеству пользователей."""
#     num_users = 5
#     users = [next(generate_users(**data)) for _ in range(num_users)]
#     assert len(users) == num_users
#
#
# def test_generate_users_keys(data):
#     """Проверяет, что у всех сгенерированных пользователей есть правильные ключи."""
#     users = [next(generate_users(**data)) for _ in range(5)]
#     for user in users:
#         assert set(user.keys()) == {'first_name', 'last_name', 'age', 'city'}
#
#
# def test_generate_users_first_names(data):
#     """Проверяет, что у всех сгенерированных пользователей имя является одним из возможных имен."""
#     users = [next(generate_users(**data)) for _ in range(5)]
#     for user in users:
#         assert user['first_name'] in data['first_names']
#
#
# def test_generate_users_last_names(data):
#     """Проверяет, что у всех сгенерированных пользователей фамилия является одной из возможных фамилий."""
#     users = [next(generate_users(**data)) for _ in range(5)]
#     for user in users:
#         assert user['last_name'] in data['last_names']
#
#
# def test_generate_users_age(data):
#     """Проверяет, что у всех сгенерированных пользователей возраст находится в заданном диапазоне."""
#     users = [next(generate_users(**data)) for _ in range(5)]
#     for user in users:
#         assert 18 <= user['age'] <= 65
#
#
# def test_generate_users_cities(data):
#     """Проверяет, что у всех сгенерированных пользователей город является одним из возможных городов."""
#     users = [next(generate_users(**data)) for _ in range(5)]
#     for user in users:
#         assert user['city'] in data['cities']



# Задача 2
# Напишите программу, которая будет принимать на вход JSON-файл
# с данными о финансовых транзакциях, фильтровать транзакции
# , совершенные в определенной валюте, и сохранять отфильтрованные
# данные в новый JSON-файл. Также напишите декоратор, который будет
# выводить в консоль статистику по количеству отфильтрованных транзакций.
# Статистика должна включать в себя количество отфильтрованных транзакций
# и их суммарную стоимость.

def transaction_filtering(json_file, type_currency):
    with open(json_file) as file:
        data = json.load(file)
    new_json = [i for i in data if i.get("currency") == type_currency]

    with open("filter_transactions.json", "w") as file:
        json.dump(new_json, file)
    return new_json

print(transaction_filtering("transactions.json", "USD"))
###########################################################################
def stat_decorator(func):
    """Декоратор для вывода статистики по отфильтрованным транзакциям."""

    def wrapper(*args, **kwargs):
        filtered_transactions = func(*args, **kwargs)
        total_amount = sum([transaction['amount'] for transaction in filtered_transactions])
        print(f"Отфильтровано {len(filtered_transactions)} транзакций на сумму {total_amount}")
        return filtered_transactions

    return wrapper
############################################################################