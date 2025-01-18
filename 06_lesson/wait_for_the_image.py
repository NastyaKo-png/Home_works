from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

#  Переходим на нужный сайт
driver.get('https://bonigarcia.dev/selenium-webdriver-java/loading-images.html')

try:
    #  Дожидаемся загрузки всех изображений
    images = WebDriverWait(driver, 20).until(
        EC.visibility_of_all_elements_located((By.TAG_NAME, 'img'))
    )

    if len(images) >= 3:
        #  Получаем значение атрибута src третьей картинки
        third_image_src = images[2].get_attribute('src')
        
        #  Выводим значение в консоль
        print(third_image_src)
    else:
        print("На странице менее трех изображений!")
finally:
    # Закрываем браузер после завершения всех операций
    driver.quit()
