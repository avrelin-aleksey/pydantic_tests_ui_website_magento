import allure

@allure.feature("Страница товаров")
class TestAccountCreation:
    error_password_message = (
        "Minimum length of this field must be equal or greater than 8 symbols."
        " Leading and trailing spaces will be ignored."
    )
    success_message = "Thank you for registering with Main Website Store."

    @allure.title("Успешное добавления товара после фильтрации в сравнение")
    def test_successful_account_creation(self, collection_page):
        # Открыть страницу
        collection_page.open_page()
        # Выбор в меню STYLE(Tee) - SIZE(XL) - CLIMATE(Indoor) - COLOR(blue)
        collection_page.click_menu()
        # Проверить список всех добавленных фильтров
        collection_page.verify_filters()
        # Поменять цвет первого товара на белый
        collection_page.change_color_tee_first()
        # Добавить первый товар в сравнение
        collection_page.add_to_compare(1)
        # Добавить второй товар в сравнение
        collection_page.add_to_compare(2)
        # Нажать кнопку сравнения в уведомлении
        collection_page.click_button_compare()
        # Проверка что на странице есть два добавленных в сравнение товара
        collection_page.verify_two_product_items()
        # Проверка удаления
        collection_page.verify_two_product_items()
