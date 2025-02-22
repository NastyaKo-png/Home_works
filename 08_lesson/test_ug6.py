import requests

# Функция для красивого вывода проектов
def pretty_print_projects(projects):
    for project in projects:
        title = project['title']
        timestamp = project['timestamp']
        users = ', '.join([f'{user}: {role}' for user, role in project.get('users', {}).items()])
        id = project['id']
        
        print(f"""
Title: {title}
Timestamp: {timestamp}
Users: {users}
ID: {id}
""")

# Настройки запроса
base_url = "https://ru.yougile.com"
endpoint = "/api-v2/projects"
url = base_url + endpoint

# Заголовки запроса с токеном
# Заголовки запроса с токеном
headers = {
    "Authorization": "Bearer rjltK7XUivS4edFfMp7XVHBsg3deiC++asKJielq556gyGwJTPP57x32Jhq5XO0T",  # Замените <Ваш токен> на реальный токен
    "Content-Type": "application/json"       # Указываем, что отправляем данные в формате JSON
}

# Параметры запроса
query_params = {
    "includeDeleted": False,  # По умолчанию False, поставьте True, чтобы вернуть удаленные объекты
    "limit": 50,              # Максимум 1000
    "offset": 0               # Индекс первого элемента страницы
}

# Отправка GET-запроса
response = requests.get(url, headers=headers, params=query_params)

# Проверка статуса ответа
if response.status_code == 200:
    projects = response.json()["content"]  # Извлекаем список проектов из ответа
    
    # Вызов функции для красивого вывода проектов
    pretty_print_projects(projects)
    
    print("\nУспешно! Список проектов:")
    print(response.json())
else:
    print(f"Ошибка: {response.status_code} - {response.text}")