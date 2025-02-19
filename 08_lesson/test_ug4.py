import requests

# Настройки запроса
base_url = "https://ru.yougile.com"
endpoint = "/api-v2/auth/keys"
url = base_url + endpoint

# Тело запроса
data = {
    "login": "avast1991-07@ya.ru",
    "password": "teremok1223",
    "companyId": " 54aa0243-afbf-4612-88c9-160bc031c4e7"
}

# Отправка POST-запроса
response = requests.post(url, json=data)

# Проверка статуса ответа
if response.status_code == 201:
    print("Успешно! Список ключей:")
    print(response.json())
else:
    print(f"Ошибка: {response.status_code} - {response.text}")