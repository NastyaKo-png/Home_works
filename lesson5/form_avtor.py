from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))


# Шаг 3: Переходим на нужную страницу
driver.get('http://the-internet.herokuapp.com/login')

try:
    # Шаг 4: Находим поле username и вводим значение tomsmith
    username_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'username'))
    )
    username_field.send_keys('tomsmith')

    # Шаг 5: Находим поле password и вводим значение SuperSecretPassword!
    password_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'password'))
    )
    password_field.send_keys('SuperSecretPassword!')

    # Шаг 6: Находим кнопку Login и нажимаем её
    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '.radius'))
    )
    login_button.click()
finally:
    # Закрываем браузер после завершения всех операций
    driver.quit()