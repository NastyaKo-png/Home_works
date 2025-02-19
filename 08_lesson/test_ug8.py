import requests

# Настройки запроса
base_url = "https://ru.yougile.com"
endpoint = "/api-v2/projects/{}"  # Замените {} на ID проекта
url = base_url + endpoint.format('8f0d9190-c995-4521-9815-a00f5003b7b6')

# Заголовки запроса с токеном
headers = {
    "Authorization": "Bearer rjltK7XUivS4edFfMp7XVHBsg3deiC++asKJielq556gyGwJTPP57x32Jhq5XO0T",  # Замените <Ваш токен> на реальный токен
    "Content-Type": "application/json"       # Указываем, что отправляем данные в формате JSON
}

# Тело запроса
data = {
    "title": "Обновленное название проекта",  # Новое название проекта
    "users": { "de94f601-4edc-40ce-93d5-1358d1b1749e": "admin"
  }
}

# Отправка PUT-запроса
response = requests.put(url, headers=headers, json=data)

# Проверка статуса ответа
if response.status_code == 200:
    updated_project = response.json()
    print("Проект успешно обновлён!")
    print(updated_project)
else:
    print(f"Ошибка: {response.status_code} - {response.text}")