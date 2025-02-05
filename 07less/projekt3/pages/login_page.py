from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def enter_username(self, username):
        user_name = self.driver.find_element(By.XPATH, '//*[@id="user-name"]')
        user_name.clear()
        user_name.send_keys(username)

    def enter_password(self, password):
        pwd = self.driver.find_element(By.CSS_SELECTOR, "#password")
        pwd.clear()
        pwd.send_keys(password)

    def click_login_button(self):
        login_button = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#login-button"))
        )
        login_button.click()