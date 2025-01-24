import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Создаем экземпляр драйвера Chrome
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Переход на нужный сайт
driver.get('https://bonigarcia.dev/selenium-webdriver-java/data-types.html')

try:
    # Нахождение поля ввода и ввод текста Иван
    first_name_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'input[name="first-name"]'))
    )
    first_name_field.send_keys('Иван')

    # Нахождение поля ввода и ввод текста last-name Петров
    last_name_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'input[name="last-name"]'))
    )
    last_name_field.send_keys('Петров')

    # Нахождение поля ввода и ввод текста Address Ленина, 55-3
    address_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'input[name="address"]'))
    )
    address_field.send_keys('Ленина, 55-3')

    # Нахождение поля ввода и ввод текста Email test@skypro.com
    email_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'input[name="e-mail"]'))
    )
    email_field.send_keys('test@skypro.com')

    # Нахождение поля ввода и ввод текста Phone number +7985899998787
    phone_number_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'input[name="phone"]'))
    )
    phone_number_field.send_keys('+7985899998787')

    # Нахождение поля ввода и оставляем пустым
    zip_code_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'input[name="zip-code"]'))
    )
    zip_code_field.clear()

    # Нахождение поля ввода и ввод текста City Москва
    city_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'input[name="city"]'))
    )
    city_field.send_keys('Москва')

    # Нахождение поля ввода и ввод текста Country Россия
    country_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'input[name="country"]'))
    )
    country_field.send_keys('Россия')

    # Нахождение поля ввода и ввод текста Job position QA
    job_position_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'input[name="job-position"]'))
    )
    job_position_field.send_keys('QA')

    # Нахождение поля ввода и ввод текста Company SkyPro
    company_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'input[name="company"]'))
    )
    company_field.send_keys('SkyPro')

    # Нажатие кнопки Submit
    def click_submit():
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.btn.btn-outline-primary.mt-3'))
        )
        
        # Прокручиваем страницу к кнопке
        submit_button.location_once_scrolled_into_view
        
        # Выполнить клик с помощью JavaScript
        driver.execute_script("arguments[0].click();", submit_button)

    # Выполнение клика по кнопке Submit
    click_submit()

    # Проверяем, что поле Zip Code подсвечено красным
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, 'invalid-feedback'))
    )
    assert 'is-invalid' in zip_code_field.get_attribute('class'), 'Поле Zip Code должно быть подсвечено красным.'

    # Проверяем, что остальные поля подсвечены зеленым
    fields_to_check = [
        first_name_field,
        last_name_field,
        address_field,
        email_field,
        phone_number_field,
        city_field,
        country_field,
        job_position_field,
        company_field
    ]

    for field in fields_to_check:
        assert 'is-valid' in field.get_attribute('class'), f'Поле {field.get_attribute("name")} должно быть подсвечено зеленым.'

except Exception as e:
    print(f"Произошла ошибка: {e}")
finally:
    driver.quit()