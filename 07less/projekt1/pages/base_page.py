from selenium.webdriver.common.by import By


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator):
        return self.driver.find_element(*locator)

    def fill_field(self, locator, value):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(value)

    def click_button(self, locator):
        button = self.find_element(locator)
        button.click()

    def scroll_to_element_and_click_js(self, locator):
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        self.driver.execute_script("arguments[0].click();", element)

    def is_element_with_class_present(self, locator, class_name):
        element = self.find_element(locator)
        classes = element.get_attribute('class')
        return class_name in classes