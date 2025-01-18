from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Шаг 1: Открытие страницы
driver = webdriver.Chrome()
driver.get('http://the-internet.herokuapp.com/add_remove_elements/')

# Шаг 2: Пять раз кликнуть на кнопку "Add Element"
add_element_button = driver.find_element(By.XPATH, '//button[text()="Add Element"]')
for i in range(5):
    add_element_button.click()

# Шаг 3: Собрать со страницы список кнопок "Delete"
delete_buttons = driver.find_elements(By.XPATH, '//button[text()="Delete"]')

# Шаг 4: Вывести на экран размер списка
print(f'Количество кнопок "Delete": {len(delete_buttons)}')

# Закрыть браузер после выполнения всех шагов
driver.quit()