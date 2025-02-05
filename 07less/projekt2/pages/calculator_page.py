from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver

    @property
    def delay_input(self):
        return WebDriverWait(self.driver, 60).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#delay")))

    @property
    def button_7(self):
        return WebDriverWait(self.driver, 60).until(
            EC.element_to_be_clickable((By.XPATH, "//span[text()='7']")))

    @property
    def button_plus(self):
        return WebDriverWait(self.driver, 60).until(
            EC.element_to_be_clickable((By.XPATH, "//span[text()='+']")))

    @property
    def button_8(self):
        return WebDriverWait(self.driver, 60).until(
            EC.element_to_be_clickable((By.XPATH, "//span[text()='8']")))

    @property
    def button_equals(self):
        return WebDriverWait(self.driver, 60).until(
            EC.element_to_be_clickable((By.XPATH, "//span[text()='=']")))

    @property
    def result_field(self):
        return WebDriverWait(self.driver, 60).until(
            EC.presence_of_element_located((By.ID, "result")))

    def set_delay(self, value):
        self.delay_input.clear()
        self.delay_input.send_keys(value)

    def click_button_7(self):
        self.button_7.click()

    def click_button_plus(self):
        self.button_plus.click()

    def click_button_8(self):
        self.button_8.click()

    def scroll_down(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def click_button_equals(self):
        self.driver.execute_script("arguments[0].click();", self.button_equals)

    def get_result_value(self):
        return self.result_field.get_attribute('value')