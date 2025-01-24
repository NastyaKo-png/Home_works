import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService

@pytest.fixture(scope='session')
def browser():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    yield driver
    driver.quit()

class TestForm:
    def test_fill_form(self, browser):
        """Тестирование заполнения формы и проверки правильности заполнения полей"""
        # Код для заполнения формы и проверки полей
        WebDriverWait(browser, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'input[name="first-name"]'))
        ).send_keys('Иван')

        WebDriverWait(browser, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'input[name="last-name"]'))
        ).send_keys('Петров')

        WebDriverWait(browser, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'input[name="address"]'))
        ).send_keys('Ленина, 55-3')

        WebDriverWait(browser, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'input[name="email"]'))
        ).send_keys('test@skypro.com')

        WebDriverWait(browser, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'input[name="phone"]'))
        ).send_keys('+7985899998787')

        WebDriverWait(browser, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'input[name="zip-code"]'))
        ).clear()

        WebDriverWait(browser, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'input[name="city"]'))
        ).send_keys('Москва')

        WebDriverWait(browser, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'input[name="country"]'))
        ).send_keys('Россия')

        WebDriverWait(browser, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'input[name="job-position"]'))
        ).send_keys('QA')

        WebDriverWait(browser, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'input[name="company"]'))
        ).send_keys('SkyPro')

        WebDriverWait(browser, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.btn.btn-outline-primary.mt-3'))
        ).click()

        zip_code_field = WebDriverWait(browser, 20).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[name="zip-code"]'))
        )
        assert 'is-invalid' in zip_code_field.get_attribute('class'), 'Поле Zip Code должно быть подсвечено красным.'

        fields_to_check = [
            WebDriverWait(browser, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'input[name="first-name"]'))
            ),
            WebDriverWait(browser, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'input[name="last-name"]'))
            ),
            WebDriverWait(browser, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'input[name="address"]'))
            ),
            WebDriverWait(browser, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'input[name="email"]'))
            ),
            WebDriverWait(browser, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'input[name="phone"]'))
            ),
            WebDriverWait(browser, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'input[name="city"]'))
            ),
            WebDriverWait(browser, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'input[name="country"]'))
            ),
            WebDriverWait(browser, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'input[name="job-position"]'))
            ),
        ]