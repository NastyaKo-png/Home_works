from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def click_blue_button():
    # Шаг 1: Открытие страницы
    driver = webdriver.Chrome()
    driver.get('http://uitestingplayground.com/dynamicid')

    try:
        # Шаг 2: Клик на синюю кнопку
        blue_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn-primary"))
        )
        blue_button.click()
        
        # Подтверждение успешного клика
        print("Синяя кнопка успешно нажата.")
    finally:
        # Закрытие браузера после выполнения всех шагов
        driver.quit()

if __name__ == "__main__":
    for _ in range(3):
        click_blue_button()