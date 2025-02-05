from selenium.webdriver.common.by import By

class InventoryPage:
    def __init__(self, driver):
        self.driver = driver

    def add_to_cart_by_id(self, item_id):
        button = self.driver.find_element(By.XPATH, f"//button[text()='Add to cart' and @id='add-to-cart-{item_id}']")
        button.click()

    def go_to_cart(self):
        cart_link = self.driver.find_element(By.XPATH, '//a[contains(@class, "shopping_cart_link")]')
        cart_link.click()