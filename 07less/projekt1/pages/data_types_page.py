
from pages.base_page import BasePage
# from base_page import BasePage
from selenium.webdriver.common.by import By


class DataTypesPage(BasePage):
    
    URL = 'https://bonigarcia.dev/selenium-webdriver-java/data-types.html'
    
    # Локаторы полей формы
    FIRST_NAME_FIELD = (By.CSS_SELECTOR, 'input[name="first-name"]')
    LAST_NAME_FIELD = (By.CSS_SELECTOR, 'input[name="last-name"]')
    ADDRESS_FIELD = (By.CSS_SELECTOR, 'input[name="address"]')
    EMAIL_FIELD  = (By.CSS_SELECTOR, 'input[name="e-mail"]')
    PHONE_NUMBER_FIELD = (By.CSS_SELECTOR, 'input[name="phone"]')
    ZIP_CODE_FIELD = (By.NAME, 'zip-code')
    #ZIP_CODE_FIELD  = (By.CSS_SELECTOR, 'input[name="zip-code"]')
    CITY_FIELD  = (By.CSS_SELECTOR, 'input[name="city"]')
    COUNTRY_FIELD = (By.CSS_SELECTOR, 'input[name="country"]')
    JOB_POSITION_FIELD = (By.CSS_SELECTOR, 'input[name="job-position"]')
    COMPANY_FIELD = (By.CSS_SELECTOR, 'input[name="company"]')
    SUBMIT_BUTTON = (By.CSS_SELECTOR, 'button.btn.btn-outline-primary.mt-3')

    def open(self):
        self.driver.get(self.URL)

    def fill_form(self, first_name, last_name, address, email, phone_number, city, country, job_position, company, zip_code=""):
        self.fill_field(self.FIRST_NAME_FIELD, first_name)
        self.fill_field(self.LAST_NAME_FIELD, last_name)
        self.fill_field(self.ADDRESS_FIELD, address)
        self.fill_field(self.EMAIL_FIELD, email)
        self.fill_field(self.PHONE_NUMBER_FIELD, phone_number)
        self.fill_field(self.ZIP_CODE_FIELD, zip_code)  # Поле останется пустым
        self.fill_field(self.CITY_FIELD, city)
        self.fill_field(self.COUNTRY_FIELD, country)
        self.fill_field(self.JOB_POSITION_FIELD, job_position)
        self.fill_field(self.COMPANY_FIELD, company)

    def submit_form(self):
        self.scroll_to_element_and_click_js(self.SUBMIT_BUTTON)

    def is_zip_code_highlighted_red(self):
        return self.is_element_with_class_present(self.ZIP_CODE_FIELD, 'is-invalid')

    def are_fields_highlighted_green(self, fields):
        for field_locator in fields:
            if not self.is_element_with_class_present(field_locator, 'is-valid'):
                return False
        return True