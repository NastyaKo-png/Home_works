# python test_02_calc.py
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time


def wait_for_element(driver, locator):
    return WebDriverWait(driver, 60).until(
        EC.presence_of_element_located(locator)
    )


def main():
    # Указываем путь к драйверу Chrome
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    try:
            # Открываем страницу
            driver.get(
                "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

            # Максимизируем окно браузера
            driver.maximize_window()

            # Вводим задержку в поле delay
            delay_input = wait_for_element(driver, (By.CSS_SELECTOR, "#delay"))
            delay_input.clear()
            delay_input.send_keys("45")

            # Нажатие на кнопку 7
            button_7 = wait_for_element(
    driver, (By.XPATH, "//span[text()='7']"))
            button_7.click()

            # Нажатие на кнопку +
            button_plus = wait_for_element(
    driver, (By.XPATH, "//span[text()='+']"))
            button_plus.click()

            # Нажатие на кнопку 8
            button_8 = wait_for_element(
    driver, (By.XPATH, "//span[text()='8']"))
            button_8.click()

            # Прокручиваем страницу вниз до конца
            driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);")

            # Ожидание перед нажатием на знак =
            time.sleep(10)

            # Нажатие на кнопку =
            button_equals = wait_for_element(
    driver, (By.XPATH, "//span[text()='=']"))
            driver.execute_script("arguments[0].click();", button_equals)

            # Проверяем результат
            result = wait_for_element(
    driver, (By.ID, "result")).get_attribute('value')
            assert result == '15', f'Ожидаемый результат: 15, но получил {result}'

            print("Тест успешно завершен!")

    finally:
            # Закрытие браузера после выполнения теста
            driver.quit()


if __name__ == "__main__":
    main()