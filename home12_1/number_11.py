import requests
import json
from unittest.mock import patch

# Задача 1
# Напишите программу, которая получает информацию
# о репозиториях пользователей GitHub.
#
# 1)Принимает на вход список пользователей GitHub
# 2)Для каждого пользователя получает его информацию
# и список его репозиториев.
# 3)Составляет список результатов в формате JSON, в котором
# для каждого пользователя указаны его логин,
# количество публичных репозиториев и список его репозиториев.
#
# Для получения информации о пользователе и его
# репозиториях должны использоваться открытые API GitHub.
#
# Пример использования программы:
# users = ['user1', 'user2', 'user3']
# result = get_github_users(users)
# print(result)

# def get_github_users(users):
#     results = []
#     for user in users:
#         status, user_data = get_user_info(user)
#         if not status:
#             continue
#
#         status, repositories = get_user_repos(user)
#         if not status:
#             continue
#
#         result = {
#             'login': user_data['login'],
#             'public_repos': user_data['public_repos'],
#             'repositories': repositories
#         }
#         results.append(result)
#     return json.dumps(results)
#
#
# def get_user_info(user: str) -> tuple[bool, dict]:
#     url = f"https://api.github.com/users/{user}"
#     response = requests.get(url)
#     if response.status_code != 200:
#         return False, {}
#     return True, response.json()
#
#
# def get_user_repos(user: str) -> tuple[bool, list]:
#     repo_url = f"https://api.github.com/users/{user}/repos"
#     repo_response = requests.get(repo_url)
#     if repo_response.status_code != 200:
#         return False, []
#     return True, [repo['name'] for repo in repo_response.json()]
#
# print(get_github_users(["s1mpson01"]))

# @patch('src.github.requests.get')
# def test_get_user_info(mocked_get):
#     mocked_get.return_value.status_code = 200
#     mocked_get.return_value.json.return_value = {'login': 'test_user', 'public_repos': 10}
#     result = get_user_info('test_user')
#     assert result == (True, {'login': 'test_user', 'public_repos': 10})
#
# @patch('src.github.requests.get')
# def test_get_user_info_invalid(mocked_get):
#     mocked_get.return_value.json.return_value = {'message': 'Not Found'}
#     result = get_user_info('non_existent_user')
#     assert result == (False, {})
#
# @patch('src.github.requests.get')
# def test_get_user_repos(mocked_get):
#     mocked_get.return_value.status_code = 200
#     mocked_get.return_value.json.return_value = [{'name': 'repo1'}, {'name': 'repo2'}]
#     result = get_user_repos('test_user')
#     assert result == (True, ['repo1', 'repo2'])
#
# @patch('src.github.requests.get')
# def test_get_user_repos_invalid(mocked_get):
#     mocked_get.return_value.status_code = 404
#     mocked_get.return_value.json.return_value = {'message': 'Not Found'}
#     result = get_user_repos('non_existent_user')
#     assert result == (False, [])
#
# @patch('src.github.get_user_info')
# @patch('src.github.get_user_repos')
# def test_get_github_users(mock_get_user_repos, mock_get_user_info):
#     mock_get_user_info.return_value = (True, {'login': 'user1', 'public_repos': 2})
#     mock_get_user_repos.return_value = (True, ['repo1', 'repo2'])
#     expected_result = [{'login': 'user1', 'public_repos': 2, 'repositories': ['repo1', 'repo2']}]
#     result = get_github_users(['user1'])
#     assert result == json.dumps(expected_result)
#
# @patch('src.github.get_user_info')
# @patch('src.github.get_user_repos')
# def test_get_github_users_negative(mock_get_user_repos, mock_get_user_info):
#     mock_get_user_info.return_value = (False, {})
#     mock_get_user_repos.return_value = (False, [])
#     result = get_github_users(['non_existent_user'])
#     assert result == None

#############################################################################
# Задача 2
# Напишите функцию, которая будет получать курс валюты
# на текущую дату из API ЦБ РФ и возвращать его в формате JSON.
# Используйте сайт https://www.cbr-xml-daily.ru/daily_json.js.
#
# Пример вызова функции:
# rate = get_currency_rate("USD")
# print(rate)
#
# Результат:
# {
#     "currency_code": "USD",
#     "rate": 72.7384
# }

# def get_currency_rate(currency_code):
#     url = f"https://www.cbr-xml-daily.ru//daily_json.js"
#     response = requests.get(url)
#     if response.status_code != 200:
#         raise ValueError(f"Failed to get currency rate")
#     data = response.json()
#     currency_data = data["Valute"].get(currency_code)
#     if not currency_data:
#         raise ValueError(f"No data for currency {currency_code}")
#     return {
#         "currency_code": currency_code,
#         "rate": currency_data["Value"],
#     }
#
# print(get_currency_rate("USD"))
#
# def test_get_currency_rate_success():
#     mock_response = Mock()
#     mock_response.status_code = 200
#     mock_response.json.return_value = {
#         "Valute": {
#             "USD": {
#                 "Value": 73.5
#             }
#         }
#     }
#
#     with patch('requests.get', return_value=mock_response):
#         result = get_currency_rate("USD")
#         assert result == {
#             "currency_code": "USD",
#             "rate": 73.5
#         }
#
#
# def test_get_currency_rate_no_currency():
#     mock_response = Mock()
#     mock_response.status_code = 200
#     mock_response.json.return_value = {
#         "Valute": {
#             "EUR": {
#                 "Value": 89.5
#             }
#         }
#     }
#
#     with patch('requests.get', return_value=mock_response):
#         with pytest.raises(ValueError, match="No data for currency"):
#             get_currency_rate("USD")
#
#
# def test_get_currency_rate_failed_request():
#     mock_response = Mock()
#     mock_response.status_code = 500
#
#     with patch('requests.get', return_value=mock_response):
#         with pytest.raises(ValueError, match="Failed to get currency rate"):
#             get_currency_rate("USD")
