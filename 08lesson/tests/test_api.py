import requests
import pytest

# Настройки запроса
base_url = "https://ru.yougile.com"
# Заголовки запроса с токеном
headers = {
    "Authorization": "Bearer rjltK7XUivS4edFfMp7XVHBsg3deiC++asKJielq556gyGwJTPP57x32Jhq5XO0T",   #токен
    "Content-Type": "application/json"       # отправляем данные в формате JSON
}

# Тело запроса для создания нового проекта
create_data = {
    "title": "New Project",  # Название проекта
    "users": {"de94f601-4edc-40ce-93d5-1358d1b1749e": "admin"}
}

# Тело запроса для обновления проекта
update_data = {
    "title": "Обновленное название проекта",  # Новое название проекта
    "users": {"de94f601-4edc-40ce-93d5-1358d1b1749e": "admin"}
}

# Тестовая функция для создания проекта
def test_create_project():
    endpoint = "/api-v2/projects"
    url = base_url + endpoint

    # Отправка POST-запроса
    response = requests.post(url, headers=headers, json=create_data)

    # Проверка статуса ответа
    if (response.status_code) == 201:
        print("Проект успешно создан!")
        print(response.json())  # Выводим ответ сервера
    else:
        print(f"Ошибка: {response.status_code} - {response.text}")

# Тестовая функция для получения списка проектов
def test_get_projects():
    endpoint = "/api-v2/projects"
    url = base_url + endpoint

    # Параметры запроса
    query_params = {
        "includeDeleted": False,  # По умолчанию False, поставьте True, чтобы вернуть удаленные объекты
        "limit": 50,              # Максимум 1000
        "offset": 0               # Индекс первого элемента страницы
    }

    # Отправка GET-запроса
    response = requests.get(url, headers=headers, params=query_params)

    # Проверка статуса ответа
    if (response.status_code) == 200:
        projects = (response.json())["content"]  # Извлекаем список проектов из ответа
        
 
        print(projects)
        print("\nУспешно! Список проектов:")
        print(response.json())
    else:
        print(f"Ошибка: {response.status_code} - {response.text}")

# Тестовая функция для получения проекта по ID
def test_get_project_by_id():
    endpoint = "/api-v2/projects/{}"  
    url = base_url + endpoint.format('8f0d9190-c995-4521-9815-a00f5003b7b6')  

    # Отправка GET-запроса
    response = requests.get(url, headers=headers)

    # Проверка статуса ответа
    if (response.status_code) == 200:
        project = (response.json())
        print("Успешно! Проект по ID:")
        print(project)
    else:
        print(f"Ошибка: {response.status_code} - {response.text}")

# Тестовая функция для обновления проекта
def test_update_project():
    endpoint = "/api-v2/projects/{}"  # Замените {} на ID проекта
    url = base_url + endpoint.format('8f0d9190-c995-4521-9815-a00f5003b7b6')

    # Отправка PUT-запроса
    response = requests.put(url, headers=headers, json=update_data)

    # Проверка статуса ответа
    if (response.status_code) == 200:
        updated_project = (response.json())
        print("Проект успешно обновлён!")
        print(updated_project)
    else:
        print(f"Ошибка: {response.status_code} - {response.text}")

# pytest test_api.py 
