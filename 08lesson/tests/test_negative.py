import requests  # pytest test_negative.py
import pytest


import requests
import pytest

# Настройки запроса
base_url = "https://ru.yougile.com"
#endpoint = "/api-v2/projects/{}"  # Замените {} на ID проекта
#url = base_url + endpoint

# Заголовки запроса с токеном
headers = {
    "Authorization":  "Bearer rjltK7XUivS4edFfMp7XVHBsg3deiC++asKJielq556gyGwJTPP57x32Jhq5XO0T",
    "Content-Type": "application/json"
}

# Тело запроса
data = {
    "title": "Test Project",  # Название проекта
    "description": "This is a test project.",  # Описание проекта
    "users":  {"de94f601-4edc-40ce-93d5-1358d1b1749e": "admin"}
}
#Негативный тест: создание проекта с пустыми данными.Ожидается, что сервер вернет ошибку 400 (Bad Request).
def test_create_project_empty_data():

    endpoint = "/api-v2/projects"
    url = base_url + endpoint
    empty_data = {}
    response = requests.post(url, headers=headers, json=empty_data)
    assert response.status_code == 400, f"Ожидалось 400, получено {response.status_code}"
    
#Негативный тест: создание проекта с дублирующим названием.Ожидается, что сервер вернет ошибку 409 (Conflict).
def test_create_project_duplicate_title():
    endpoint = "/api-v2/projects"
    url = base_url + endpoint
    duplicate_data = {
        "title": "Duplicate Title",  # Название проекта
        #"description": "This is a test project.",
        "users":  {"de94f601-4edc-40ce-93d5-1358d1b1749e": "admin"}
    }
    # Сначала создаем проект с таким названием
    response = requests.post(url, headers=headers, json=duplicate_data)
    assert response.status_code == 201, f"Ожидалось 201, получено {response.status_code}"
    # Затем пытаемся создать второй проект с тем же названием
    response = requests.post(url, headers=headers, json=duplicate_data)
    assert response.status_code == 409, f"Ожидалось 409, получено {response.status_code}"

# Негативный тест: изменение несуществующего проекта.Ожидается, что сервер вернет ошибку 400 (Not Found).
def test_change_nonexistent_project():

    endpoint = "/api-v2/projects/{}"  
    url = base_url + endpoint.format('8f0d9190-c995-4521-9815-a00f5003b7b5')  
    response = requests.put(url, headers=headers, json=data)
    assert response.status_code == 400, f"Ожидалось 400, получено {response.status_code}"

#Негативный тест: получение несуществующего проекта.Ожидается, что сервер вернет ошибку 400 (Not Found).
def test_get_nonexistent_project():
    endpoint = "/api-v2/projects/{}"  
    url = base_url + endpoint.format('8f0d9190-c995-4521-9815-a00f5003b7b5') 
    response = requests.get(url, headers=headers)
    assert response.status_code == 404, f"Ожидалось 404, получено {response.status_code}"

#Негативный тест: неавторизованный доступ.Ожидается, что сервер вернет ошибку 401 (Unauthorized).
def test_unauthorized_access():
    endpoint = "/api-v2/projects"
    url = base_url + endpoint
    unauthorized_headers = {
        "Authorization": "Bearer rjltK7XUivS4edFfMp7XVHBsg3deiC++asKJielq556gyGwJTPP57x32Jhq5XO0N",
        "Content-Type": "application/json"
    }
    response = requests.get(url, headers=unauthorized_headers)
    assert response.status_code == 401, f"Ожидалось 401, получено {response.status_code}"