from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_step_one_page import CheckoutStepOnePage
from pages.checkout_overview_page import CheckoutOverviewPage

def test_purchase_total(driver):
    # Открываем страницу
    url = "https://www.saucedemo.com/"
    driver.get(url)

    # Создаем объекты страниц
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)
    checkout_step_one_page = CheckoutStepOnePage(driver)
    checkout_overview_page = CheckoutOverviewPage(driver)

    # Выполнение шагов теста
    login_page.enter_username("standard_user")
    login_page.enter_password("secret_sauce")
    login_page.click_login_button()

    inventory_page.add_to_cart_by_id("sauce-labs-backpack")
    inventory_page.add_to_cart_by_id("sauce-labs-bolt-t-shirt")
    inventory_page.add_to_cart_by_id("sauce-labs-onesie")
    inventory_page.go_to_cart()

    cart_page.click_checkout()

    checkout_step_one_page.fill_first_name("Иван")
    checkout_step_one_page.fill_last_name("Иванов")
    checkout_step_one_page.fill_postal_code("433821")
    checkout_step_one_page.click_continue()

    # Получение итоговой стоимости
    total = checkout_overview_page.get_total_price()

    # Вывод в консоль
    print(total)

    # Проверяем итоговую сумму
    assert total == 'Total: $58.29'