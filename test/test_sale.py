import allure

from pages import data_for_test


@allure.feature("Страница SALE")
class TestAccountCreation:
    @allure.title("Проверка ссылок на странице SALE")
    def checking_links_on_sale_page(self, sale_page):
        # Открываем страницу
        sale_page.open_page()

        # Проверяем заголовок страницы
        sale_page.verify_page_title(data_for_test.expected_page)

        # Проверяем блоки с акциями
        sale_page.assert_promo_blocks_match_expected(data_for_test.expected_promo)
