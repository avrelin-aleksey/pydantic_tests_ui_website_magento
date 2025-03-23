import allure

from pages.locators import collections_locator as loc
from pages.base_page import BasePage
from selenium.webdriver.common.action_chains import ActionChains


class CollectionPage(BasePage):
    page_url = "/collections/eco-friendly.html"

    def click_menu(self):
        self.driver.implicitly_wait(2)
        with allure.step("Выбрать фильтр STYLE"):
            self.find(loc.style_menu_loc).click()

        with allure.step("Выбрать Tee"):
            self.find(loc.style_menu_tee_loc).click()
            self.driver.implicitly_wait(1)

        with allure.step("Выбрать фильтр SIZE"):
            self.find(loc.size_menu_loc).click()

        with allure.step("Выбрать XL"):
            self.find(loc.size_menu_XL_loc).click()
            self.driver.implicitly_wait(1)

        with allure.step("Выбрать фильтр CLIMATE"):
            self.find(loc.climate_menu_loc).click()

        with allure.step("Выбрать Indoor"):
            self.find(loc.climate_menu_indoor_loc).click()
            self.driver.implicitly_wait(1)

        with allure.step("Выбрать фильтр COLOR"):
            self.find(loc.color_menu_loc).click()

        with allure.step("Выбрать blue"):
            self.find(loc.color_menu_blue_loc).click()
            self.driver.implicitly_wait(1)

    def add_to_compare(self, number):
        second_product = (
            "xpath",
            f"(//div[@class='product details product-item-details'])[{number}]",
        )
        add_to_compare = ("xpath", f"(//div/a[@class='action tocompare'])[{number}]")

        with allure.step("Навести курсор мыши на выбранную футболку"):
            actions = ActionChains(self.driver)
            actions.move_to_element(self.find(second_product))
            self.driver.implicitly_wait(2)
        with allure.step("Добавление в сравнение"):
            actions.move_to_element(self.find(add_to_compare)).click().perform()

    def check_comparison_message(self, text):
        comparison_message = self.find(loc.message_add_to_comparison_list_loc)
        actual_text = comparison_message.text

        with allure.step("Проверка текста после добавления в сравнение"):
            assert text in actual_text, (
                f"Текст после добавления в сравнение не соответствует ожидаемому. "
                f"Фактический текст: {actual_text}"
            )

    def change_color_tee_first(self):
        with allure.step("Изменить цвет первого овара на белый"):
            self.find(loc.color_tee_first_wight_loc).click()
            self.driver.implicitly_wait(1)

    # def find_element_and_check_content_filters(self, number):
    #     now_shopping_by_number = ("xpath", f"//strong[@data-count='{number}']")
    #     with allure.step("Найти сколько добавлено фильтрации 'Now Shopping by'"):
    #         if self.find(now_shopping_by_number):
    #             pass
    #         else:
    #             print(f"Количество добавленных фильтров не равно {number}")
    #
    #     with allure.step("Получаем тест номера на странице"):
    #         element_text = self.find(now_shopping_by_number).text
    #
    #     with allure.step("Проверка содержимого на равенство '4'"):
    #         assert element_text == number, f"Текст элемента не равен {number}. Фактическое значение: {element_text}"

    def verify_filters(self):
        with allure.step("Проверить список всех добавленных фильтров"):
            filter_items = self.find_all(loc.filter_current_items_loc)

            filters = [
                {"label": "Style", "value": "Tee"},
                {"label": "Size", "value": "XL"},
                {"label": "Climate", "value": "Indoor"},
                {"label": "Color", "value": "Blue"},
            ]

            assert len(filter_items) == len(filters), "Количество фильтров не совпадает"
            for i, filter_item in enumerate(filter_items):
                label = filter_item.find_element(*loc.filter_label_loc).text
                value = filter_item.find_element(*loc.filter_value_loc).text

                assert label == filters[i]["label"]
                assert value == filters[i]["value"]

    def click_button_compare(self):
        with allure.step("Нажать кнопку сравнения в уведомлении"):
            self.wait_until_visible(loc.button_comparison_list_loc).click()

    def verify_two_product_items(self):
        with allure.step(
            "Проверка что на странице есть два добавленных в сравнение товара"
        ):
            product_items = self.find_all(loc.product_items_loc)
            assert len(product_items) == 2
