
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


def wait_for_element(driver, locator):
    return WebDriverWait(driver, 20).until(
        EC.presence_of_element_located(locator)
    )


def test_purchase_total():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    # Максимизируем окно браузера
    driver.maximize_window()

    # Открытие страницы
    url = "https://www.saucedemo.com/"
    driver.get(url)

    # Авторизация стандартным пользователем
    user_name = driver.find_element(By.XPATH, '//*[@id="user-name"]')
    user_name.clear()
    user_name.send_keys('standard_user')

    password = driver.find_element(By.CSS_SELECTOR, "#password")
    password.clear()
    password.send_keys('secret_sauce')

    # Ждем видимости кнопки входа
    login_button = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#login-button"))
    )

    # Кликаем на кнопку входа
    login_button.click()

    # Добавляем товары в корзину
    driver.find_element(By.XPATH, "//button[text()='Add to cart' and @id='add-to-cart-sauce-labs-backpack']").click()
    driver.find_element(By.XPATH, '//button[@data-test="add-to-cart-sauce-labs-bolt-t-shirt"]').click()
    driver.find_element(By.XPATH, '//button[@data-test="add-to-cart-sauce-labs-onesie"]').click()

    # Переходим в корзину
    driver.find_element(By.XPATH, '//a[contains(@class, "shopping_cart_link")]').click()

    # Нажимаем Checkout
    driver.find_element(By.CSS_SELECTOR, "button.checkout_button").click()

    # Заполняем форму своими данными
    first_name_field = driver.find_element(By.ID, "first-name")
    first_name_field.send_keys('Иван')

    last_name_field = driver.find_element(By.ID, "last-name")
    last_name_field.send_keys('Иванов')

    postal_code_field = driver.find_element(By.ID, "postal-code")
    postal_code_field.send_keys('433821')

    # Нажимаем Continue
    driver.find_element(By.CSS_SELECTOR, "[data-test='continue']").click()

    # Найти элемент с итоговой стоимостью
    total = driver.find_element(By.CSS_SELECTOR, "div.summary_total_label").text

    # Вывести итоговую стоимость в консоль
    print(total)

    # Проверить, что итоговая сумма равна '$58.29'
    assert total == 'Total: $58.29'

    # Закрыть браузер
    driver.quit()


if __name__ == "__main__":
    test_purchase_total()