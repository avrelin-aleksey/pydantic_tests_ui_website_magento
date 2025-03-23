import allure

from faker import Faker
from pages.locators import customer_locator as loc
from pages.base_page import BasePage

fake = Faker()


class CustomerPage(BasePage):
    page_url = "/customer/account/create/"

    def customer_form(self, first_name, last_name, email, password):
        self.find(loc.first_name_field_loc).send_keys(first_name)
        self.find(loc.last_name_field_loc).send_keys(last_name)
        self.find(loc.email_field_loc).send_keys(email)
        self.find(loc.password_field_loc).send_keys(password)
        self.driver.implicitly_wait(1)
        self.find(loc.password_confirmation_loc).send_keys(password)
        self.driver.implicitly_wait(1)

    def customer_account_form(self):
        with allure.step("Заполнение полей формы"):
            first_name = fake.first_name()
            last_name = fake.last_name()
            email = fake.email()
            password = fake.password()
            self.customer_form(first_name, last_name, email, password)

    def incorrect_password_empty_customer_account_form(self, password):
        with allure.step("Заполнение полей формы"):
            first_name = fake.first_name()
            last_name = fake.last_name()
            email = fake.email()
            self.customer_form(first_name, last_name, email, password)

    def create_account_form(self):
        with allure.step("Отправка формы по кнопке 'Create an Account'"):
            self.find(loc.button_create_an_account).click()

    def assert_result(self, locator, text):
        with allure.step("Сравнение полученного результата с ожидаемым"):
            result_text = self.wait_until_visible(locator).text
            assert result_text == text, f"Фактический текст: '{result_text}'"
