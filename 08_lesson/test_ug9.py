import requests

# Настройки запроса
base_url = "https://ru.yougile.com"
endpoint = "/api-v2/projects/{}"  # Замените {} на ID проекта
url = base_url + endpoint.format('8f0d9190-c995-4521-9815-a00f5003b7b6')

# Заголовки запроса с токеном
headers = {
    "Authorization": "Bearer rjltK7XUivS4edFfMp7XVHBsg3deiC++asKJielq556gyGwJTPP57x32Jhq5XO0N",
    "Content-Type": "application/json"
}

# Тело запроса
data = {
    "title": "Обновленное название проекта",
    "users": { "de94f601-4edc-40ce-93d5-1358d1b1749e": "admin"
  }
}

# Отправка PUT-запроса
response = requests.put(url, headers=headers, json=data)

# Проверка статуса ответа
assert response.status_code == 401, f"Ожидалось 401, получено {response.status_code}"
print("Тест 1 пройден: система верно отклонила запрос с неправильным токеном.")