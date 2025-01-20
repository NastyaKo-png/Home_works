from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# Создание драйвера
driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

# Переход на нужную страницу
driver.get('http://the-internet.herokuapp.com/entry_ad')

try:
    # Шаг 1: Ожидаем появления модального окна и находим кнопку Close
    wait = WebDriverWait(driver, 10)
    close_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, '//p[contains(text(), "Close")]'))
    )

    # Шаг 2: Нажимаем на кнопку Close
    close_button.click()
finally:
    # Завершение работы драйвера
    driver.quit()