import requests

# Настройки запроса
base_url = "https://ru.yougile.com"
endpoint = "/api-v2/projects/{}"  
url = base_url + endpoint.format('8f0d9190-c995-4521-9815-a00f5003b7b6')  

# Заголовки запроса с токеном
headers = {
    "Authorization": "Bearer rjltK7XUivS4edFfMp7XVHBsg3deiC++asKJielq556gyGwJTPP57x32Jhq5XO0T"  
}

# Отправка GET-запроса
response = requests.get(url, headers=headers)

# Проверка статуса ответа
if response.status_code == 200:
    project = response.json()
    print("Успешно! Проект по ID:")
    print(project)
else:
    print(f"Ошибка: {response.status_code} - {response.text}")