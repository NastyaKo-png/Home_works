from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

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
    
    driver.quit()