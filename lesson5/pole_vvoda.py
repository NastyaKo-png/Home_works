from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))


# Шаг 1: Переходим на нужную страницу
driver.get('http://the-internet.herokuapp.com/inputs')

try:
    # Шаг 2: Находим поле ввода
    input_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, 'input'))
    )

    # Шаг 3: Вводим текст "1000" в поле
    input_field.send_keys('1000')

    # Шаг 4: Очищаем поле (методом clear())
    input_field.clear()

    # Шаг 5: Вводим текст "999" в очищенное поле
    input_field.send_keys('999')
finally:
    # Закрываем браузер после завершения всех операций
    driver.quit()