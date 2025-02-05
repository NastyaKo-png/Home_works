import pytest
from pages.calculator_page import CalculatorPage


@pytest.fixture(scope="module")
def driver():
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service
    from webdriver_manager.chrome import ChromeDriverManager

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    yield driver
    driver.quit()


def test_calculation(driver):
    page = CalculatorPage(driver)
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    driver.maximize_window()

    page.set_delay("45")
    page.click_button_7()
    page.click_button_plus()
    page.click_button_8()
    page.scroll_down()

    # Ожидание перед нажатием на знак =
    import time
    time.sleep(5)

    page.click_button_equals()

    # Проверяем результат
    result = page.get_result_value()
    assert result == '15', f'Ожидаемый результат: 15, но получил {result}'

    print("Тест успешно завершен!")