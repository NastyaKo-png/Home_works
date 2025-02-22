import requests

# Настройки запроса
base_url = "https://ru.yougile.com"
endpoint = "/api-v2/auth/companies"
url = base_url + endpoint

# Параметры запроса
query_params = {
    "limit": 50,  # Максимум 1000
    "offset": 0   # Индекс первого элемента страницы
}

# Тело запроса
data = {
  "login": "avast1991-07@ya.ru",
  "password": "teremok1223"
}

# Заголовки запроса
headers = {
    "Accept": "application/json"  # Указываем, что ожидаем ответ в формате JSON
}

# Отправка POST-запроса
response = requests.post(url, params=query_params, json=data, headers=headers)

# Проверка статуса ответа
if response.status_code == 200:
    companies = response.json()["content"]
    for company in companies:
        print("Успешно! Список компаний:")
        print(f"ID: {company['id']}, Name: {company['name']}, Admin: {company['isAdmin']}")
    
else:
    print(f"Ошибка: {response.status_code} - {response.text}")