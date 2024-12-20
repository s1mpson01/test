
# Задача 1
# Написать функцию, которая будет принимать путь до файла
# и название города и выполнять следующие действия:
#
# Прочитать JSON-файл с данными о погоде в формате JSON.
# Выбрать из этого файла данные для города, который введет пользователь.
# Рассчитать среднюю температуру за неделю для выбранного города.
# Записать результат расчета в новый JSON-файл.

# Пример входного файла с данными:

# {
#   "Moscow": {
#     "Monday": 5,
#     "Tuesday": 2,
#     "Wednesday": -3,
#     "Thursday": -6,
#     "Friday": -2,
#     "Saturday": 0,
#     "Sunday": 2
#   },
#   "St. Petersburg": {
#     "Monday": 2,
#     "Tuesday": -1,
#     "Wednesday": -4,
#     "Thursday": -6,
#     "Friday": -1,
#     "Saturday": 1,
#     "Sunday": 3
#   },
#   "Kazan": {
#     "Monday": 1,
#     "Tuesday": -2,
#     "Wednesday": -6,
#     "Thursday": -7,
#     "Friday": -3,
#     "Saturday": 0,
#     "Sunday": 2
#   }
# }
# Пример выходного файла для города "Moscow":
# {
#   "Moscow": {
#     "Average temperature": -0.29
#   }
# }

# import json
# from json import JSONDecodeError
#
#
# def display_weather_data(path_to_file, citi):
#     try:
#         with open(path_to_file) as file:
#             try:
#                 data = json.load(file)
#             except JSONDecodeError:
#                 print("Ошибка обработки файла")
#                 return False
#     except FileNotFoundError:
#         print("Файл не найден")
#         return False
#
#     avg_temp = round(sum(data[citi].values()) / len(data[citi].values()), 2)
#     write_json_file = {
#     citi:{
#         "Average temperature":avg_temp
#         }
#     }
#     with open("out.json", "w") as file:
#         json.dump(write_json_file, file)
#     return True
#
# print(display_weather_data("weather.json", "Moscow"))
###############################################################################
# Задача 2
# Напишите функцию  get_days_between_dates(date1, date2) которая
# принимает на вход две даты в формате "dd.mm.yyyy" и возвращает
# количество дней между ними. Пример использования функции:
# get_days_between_dates("01.01.2022", "31.01.2022")     30

# import datetime
# def get_days_between_dates(date1, date2):
#     data1_obj = datetime.datetime.strptime(date1, "%d.%m.%Y")
#     data2_obj = datetime.datetime.strptime(date2, "%d.%m.%Y")
#     duration = (data2_obj - data1_obj).days
#     return duration
# print(get_days_between_dates("01.01.2022", "31.01.2022"))

#######################################################################################

# Задача 3
# Напишите функцию с названием get_github_repos(username: str) -> list[str]
# которая принимает на вход имя пользователя GitHub
# и возвращает список названий репозиториев этого пользователя.
# Для выполнения задания необходимо использовать следующие этапы:
# Сделать GET-запрос к API GitHub, используя следующий URL:
# https://api.github.com/users/{username}/repos
# Обработать ответ и извлечь из него названия репозиториев.
# Вернуть список названий репозиториев.
# Если пользователь с указанным именем не найден,
# функция должна вернуть пустой список.
# Пример использования:
# repos = get_github_repos('octocat')
# print(repos)

# import requests
# def get_github_repos(username: str) -> list[str]:
#     result = []
#     responce = requests.get(f"https://api.github.com/users/{username}/repos")
#     if responce.status_code == 200:
#         content = responce.json()
#         for i in content:
#             reposit = i.get("name")
#             result.append(reposit)
#     return result
# print(get_github_repos("s1mpson01"))
########################################################################################
