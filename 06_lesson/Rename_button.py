from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


#  Переходим на нужный сайт
driver.get('http://uitestingplayground.com/textinput')

try:
    #  Находим поле ввода и вводим текст "SkyPro"
    text_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'newButtonName'))
    )
    text_input.send_keys('SkyPro')

    #  Находим синюю кнопку и нажимаем её
    blue_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'updatingButton'))
    )
    blue_button.click()

    #  Получаем текст кнопки и выводим его в консоль
    updated_button_text = WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element_value((By.ID, 'updatingButton'), 'SkyPro')
    )
    print(updated_button_text)
finally:
    # Закрываем браузер после завершения всех операций
    driver.quit()