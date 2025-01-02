import requests
import json
import logging



# Задача 1
# Напишите функцию, которая получает список пользователей
# из API, сохраняет его в JSON-файл и добавляет в файл логов дату
# и время запроса. Ссылка на API: https://jsonplaceholder.typicode.com/users.
# Пример содержимого файла log.txt
# INFO:root:Request time: 2022-10-22 14:30:05
# INFO:root:Request time: 2022-10-22 14:45:12

# logger = logging.getLogger()
# console_handler = logging.FileHandler("log.txt")
# console_formater = logging.Formatter("%(levelname)s:%(name)s:Request time:%(asctime)s")
# console_handler.setFormatter(console_formater)
# logger.addHandler(console_handler)
# logger.setLevel(logging.INFO)
#
# def get_users():
#     data = requests.get("https://jsonplaceholder.typicode.com/users")
#     data_json = data.json()
#     logger.info("ok")
#     with open("data.json", "w") as file:
#         json.dump(data_json, file)
#
# get_users()
#############################################################################
# задача 2
# У вас есть API: https://jsonplaceholder.typicode.com/photos
# Напишите приложение, которое скачивает картинки заданного альбома и
# сохраняет в директории photos Все шаги должны логироваться: от старта приложения
# до вывода текущего состояния и информации о завершении приложения
# и общем количестве скачанных картинок.Требования:
#
# Все шаги приложения должны выводиться в консоль,
# для этого нужно использовать logging
# Приложение должно принимать аргументы: album_id(обязательный) и
# limit(необязательный, по умолчанию 100)
# Приложение должно скачивать картинки по одной и выводить каждую в консоль с
# указанием имени файла и номера текущей картинки.
# В конце работы приложения должна выводиться информация о завершении
# работыи общем количестве скачанных картинок.
#
# Пример вывода логов в консоль:
# INFO:root:Starting app...
# INFO:root:Downloading album 1 images...
# INFO:root:Saving image 1 to photos/1-1.jpg
# INFO:root:Saving image 2 to photos/1-2.jpg
# INFO:root:Saving image 3 to photos/1-3.jpg
# INFO:root:Saving image 4 to photos/1-4.jpg
# INFO:root:Saving image 5 to photos/1-5.jpg
# INFO:root:Finished downloading images. Total images downloaded: 5



# logging.basicConfig(level=logging.INFO,
#                     format="%(levelname)s:%(name)s:%(message)s")
# logger = logging.getLogger("number_11")
#
#
#
# def download_photo(album_id, limit=100):
#     logger.info("Starting app...")
#     counter = 1
#     r = requests.get("https://jsonplaceholder.typicode.com/photos")
#     logger.info(f"Downloading album {album_id} images")
#     for i in r.json():
#         if i.get("albumId") == album_id:
#             image_url = i.get("url")
#             image_data = requests.get(image_url)
#             logger.info(f"Saving image {counter} to photos {album_id}-{counter}.png")
#
#             with open(f"../photos/{album_id}-{counter}.png", "wb") as file:
#                 file.write(image_data.content)
#             counter += 1
#             if counter > limit:
#                 break
#     logger.info(f"Finished downloading images. Total images downloaded: {counter - 1}")
#
# download_photo(2,3)