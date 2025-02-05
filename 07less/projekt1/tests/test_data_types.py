import pytest
from pages.data_types_page import DataTypesPage


@pytest.mark.usefixtures('browser')
class TestDataTypes:
    @pytest.fixture(autouse=True)
    def setup(self, browser):
        self.page = DataTypesPage(browser)

    def test_fill_form_and_submit(self):
        # Открываем страницу
        self.page.open()
        
        # Заполняем форму данными
        self.page.fill_form(
            first_name='Иван',
            last_name='Петров',
            address='Ленина, 55-3',
            email='test@skypro.com',
            phone_number='+7985899998787',
            city='Москва',
            country='Россия',
            job_position='QA',
            company='SkyPro',
            zip_code="",  # Оставляем поле пустым
        )
        
        # Нажимаем кнопку Submit
        self.page.submit_form()
        
        # Проверяем, что поле Zip code подсвечено красным
        assert self.page.is_zip_code_highlighted_red()
        
        # Проверяем, что остальные поля подсвечены зеленым
        green_fields = [
            self.page.FIRST_NAME_FIELD,
            self.page.LAST_NAME_FIELD,
            self.page.ADDRESS_FIELD,
            self.page.EMAIL_FIELD,
            self.page.PHONE_NUMBER_FIELD,
            self.page.CITY_FIELD,
            self.page.COUNTRY_FIELD,
            self.page.JOB_POSITION_FIELD,
            self.page.COMPANY_FIELD
        ]
        assert self.page.are_fields_highlighted_green(green_fields)