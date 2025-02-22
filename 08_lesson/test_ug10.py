import requests

# Настройки запроса
base_url = "https://ru.yougile.com"
endpoint = "/api-v2/projects/{}"  
url = base_url + endpoint.format('8f0d9190-c995-4521-9815-a00f5003b7b5')

# Заголовки запроса с токеном
headers = {
    "Authorization": "Bearer rjltK7XUivS4edFfMp7XVHBsg3deiC++asKJielq556gyGwJTPP57x32Jhq5XO0T",
    "Content-Type": "application/json"
}

# Тело запроса
data =  {
    "title": "Обновленное название проекта",  # название проекта
    "users": { "de94f601-4edc-40ce-93d5-1358d1b1749e": "admin"
  }
}

# Отправка PUT-запроса
response = requests.put(url, headers=headers, json=data)

# Проверка статуса ответа
assert response.status_code == 404, f"Ожидалось 404, получено {response.status_code}"
print("Тест 3 пройден: система верно отклонила запрос с неправильным ID проекта.")