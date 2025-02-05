from selenium.webdriver.common.by import By

class CheckoutOverviewPage:
    def __init__(self, driver):
        self.driver = driver

    def get_total_price(self):
        element = self.driver.find_element(By.CSS_SELECTOR, "div.summary_total_label")
        return element.text