import requests

# Настройки запроса
base_url = "https://ru.yougile.com"
endpoint = "/api-v2/projects"
url = base_url + endpoint

# Заголовки запроса с токеном
headers = {
    "Authorization": "Bearer rjltK7XUivS4edFfMp7XVHBsg3deiC++asKJielq556gyGwJTPP57x32Jhq5XO0T",  # Замените <Ваш токен> на реальный токен
    "Content-Type": "application/json"       # Указываем, что отправляем данные в формате JSON
}

# Тело запроса
data = {
    "title": "New Project",  # Название проекта
    "users": { "de94f601-4edc-40ce-93d5-1358d1b1749e": "admin"
  }
}

# Отправка POST-запроса
response = requests.post(url, headers=headers, json=data)

# Проверка статуса ответа
if response.status_code == 201:
    print("Проект успешно создан!")
    print(response.json())  # Выводим ответ сервера
else:
    print(f"Ошибка: {response.status_code} - {response.text}")