from selenium.webdriver.common.by import By

class CheckoutStepOnePage:
    def __init__(self, driver):
        self.driver = driver

    def fill_first_name(self, first_name):
        field = self.driver.find_element(By.ID, "first-name")
        field.send_keys(first_name)

    def fill_last_name(self, last_name):
        field = self.driver.find_element(By.ID, "last-name")
        field.send_keys(last_name)

    def fill_postal_code(self, postal_code):
        field = self.driver.find_element(By.ID, "postal-code")
        field.send_keys(postal_code)

    def click_continue(self):
        continue_button = self.driver.find_element(By.CSS_SELECTOR, "[data-test='continue']")
        continue_button.click()