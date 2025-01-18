from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

#  Переходим на нужную страницу
driver.get('http://uitestingplayground.com/ajax')

try:
    # Находим синюю кнопку и нажимаем её
    blue_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'button1'))
    )
    blue_button.click()

    #  Получаем текст из зеленой плашки
    green_label_text = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, 'updatedtext'))
    ).text

    #  Выводим текст в консоль
    print(green_label_text)
finally:
    # Закрываем браузер после завершения всех операций
    driver.quit()