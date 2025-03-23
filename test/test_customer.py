import allure
import pytest

from pages.locators import customer_locator as loc


@allure.feature("Создание аккаунта")
class TestAccountCreation:
    error_password_message = (
        "Minimum length of this field must be equal or greater than 8 symbols."
        " Leading and trailing spaces will be ignored."
    )
    success_message = "Thank you for registering with Main Website Store."

    @allure.title("Успешное создание аккаунта")
    def test_successful_account_creation(self, customer_page):
        # Открыть страницу
        customer_page.open_page()
        # Заполнить форму
        customer_page.customer_account_form()
        # Нажать кнопку 'Create an Account'
        customer_page.create_account_form()
        # Сравнить ожидаемый результат и фактический
        customer_page.assert_result(loc.success_message_loc, self.success_message)

    @allure.title("Попытка создания аккаунта с некорректным паролем (менш")
    @pytest.mark.parametrize("password", ["243234", "a", "ssss", "ADas!@d"])
    def test_invalid_password(self, customer_page, password):
        # Открыть страницу
        customer_page.open_page()
        # Заполнить форму паролем меньше 8 символов
        customer_page.incorrect_password_empty_customer_account_form(password)
        # Нажать кнопку 'Create an Account'
        customer_page.create_account_form()
        # Сравнить ожидаемый результат и фактический
        customer_page.assert_result(
            loc.error_message_password_8symbols_loc, self.error_password_message
        )
