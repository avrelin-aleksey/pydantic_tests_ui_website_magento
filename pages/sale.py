import allure

from pages.base_page import BasePage
from pages.locators import sale_locator as loc


class SalePage(BasePage):
    page_url = "/sale.html"

    @allure.step("Проверка заголовка страницы")
    def verify_page_title(self, expected_title):
        page_title = self.find(loc.page_title_loc).text
        print(f"Заголовок страницы: {page_title}")
        assert (
            page_title == expected_title
        ), f"Заголовок страницы не совпадает: {page_title} != {expected_title}"

    def assert_promo_blocks_match_expected(self, expected_data):
        promo_blocks = self.find_all(loc.promo_blocks_loc)
        print(f"Найдено ссылок с акциями: {len(promo_blocks)}")

        with allure.step("Проверка количество ссылок"):
            assert len(promo_blocks) == len(expected_data)

        with allure.step("Проверка каждой ссылки"):
            i = 0
            for block in promo_blocks:
                i += 1
                print(f"\nПроверка ссылки № = {i}:")
                with allure.step(f"Проверка ссылки {i}"):
                    title = block.find_element(*loc.title_loc).text
                    print(f"Заголовок ссылки: {title}")
                    assert (
                        title == expected_data[i - 1]["title"]
                    ), f"Название не совпадает: {title} != {expected_data[i - 1]['title']}"

                    info = block.find_element(*loc.info_loc).text
                    print(f"Информация: {info}")
                    assert (
                        info == expected_data[i - 1]["info"]
                    ), f"Информация не совпадает: {info} != {expected_data[i - 1]['info']}"

                    if expected_data[i - 1]["more"]:
                        more = block.find_element(*loc.more_loc).text
                        print(f"Текст кнопки: {more}")
                        assert (
                            more == expected_data[i - 1]["more"]
                        ), f"Текст кнопки не совпадает: {more} != {expected_data[i - 1]['more']}"
