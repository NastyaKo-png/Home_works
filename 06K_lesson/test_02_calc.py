from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.action_chains import ActionChains


def wait_for_element(driver, locator):
    return WebDriverWait(driver, 30).until(
        EC.presence_of_element_located(locator)
    )

def main():
    # Настройка драйвера
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get('https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html')

    try:
        # Вводим задержку 45 секунд
        delay_input = wait_for_element(driver, (By.ID, 'delay'))
        delay_input.clear()
        delay_input.send_keys('45')  # миллисекунды

        # Нажатие кнопок
        button_7 = wait_for_element(driver, (By.XPATH, '//span[text()="7"]'))
        button_plus = wait_for_element(driver, (By.XPATH, '//span[text()="+"]'))
        button_8 = wait_for_element(driver, (By.XPATH, '//span[text()="8"]'))
        button_equals = wait_for_element(driver, (By.XPATH, '//span[text()="="]'))

        button_7.click()
        button_plus.click()
        button_8.click()
        action = ActionChains(driver)
        element = driver.find_element(By.XPATH, '//span[text()="="]')
        action.move_to_element(element).click().perform()

        # Ждем чуть больше 45 секунд для завершения вычислений
        driver.implicitly_wait(46)

        # Проверка результата
        result = wait_for_element(driver, (By.ID, 'result')).text
        assert result == '15', f'Ожидался результат "15", но получен "{result}"'

    finally:
        driver.quit()

if __name__ == '__main__':
    main()