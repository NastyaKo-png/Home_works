from selenium.webdriver.common.by import By

class CartPage:
    def __init__(self, driver):
        self.driver = driver

    def click_checkout(self):
        checkout_button = self.driver.find_element(By.CSS_SELECTOR, "button.checkout_button")
        checkout_button.click()