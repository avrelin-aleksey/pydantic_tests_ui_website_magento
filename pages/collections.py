import allure

from pages.locators import collections_locator as loc
from pages.base_page import BasePage
from selenium.webdriver.common.action_chains import ActionChains


class CollectionPage(BasePage):
    page_url = "/collections/eco-friendly.html"

    def apply_product_filters(self, filters):
        self.select_filter("style", filters["style"])
        self.select_filter("size", filters["size"])
        self.select_filter("climate", filters["climate"])
        self.select_filter("color", filters["color"])

    def select_filter(self, filter_type, value):
        filter_locators = {
            "style": (loc.style_menu_loc, loc.style_menu_tee_loc),
            "size": (loc.size_menu_loc, loc.size_menu_XL_loc),
            "climate": (loc.climate_menu_loc, loc.climate_menu_indoor_loc),
            "color": (loc.color_menu_loc, loc.color_menu_blue_loc)
        }

        with allure.step(f"Применение фильтра {filter_type}: {value}"):
            menu_loc, value_loc = filter_locators[filter_type]
            self.find(menu_loc).click()
            self.find(value_loc).click()
            self.driver.implicitly_wait(1)

    def verify_applied_filters(self, expected_filters):
        with allure.step("Проверка применённых фильтров"):
            filter_items = self.find_all(loc.filter_current_items_loc)

            assert len(filter_items) == len(expected_filters), "Количество фильтров не совпадает"

            for i, (filter_name, expected_value) in enumerate(expected_filters.items()):
                label = filter_items[i].find_element(*loc.filter_label_loc).text
                value = filter_items[i].find_element(*loc.filter_value_loc).text

                assert label == filter_name.capitalize()
                assert value == expected_value

    def change_first_tee_color_to_white(self):
        with allure.step("Изменение цвета первого товара на белый"):
            self.find(loc.color_tee_first_wight_loc).click()
            self.driver.implicitly_wait(1)

    def add_product_to_compare(self, product_number):
        product_locator = ("xpath", f"(//div[@class='product details product-item-details'])[{product_number}]")
        compare_locator = ("xpath", f"(//div/a[@class='action tocompare'])[{product_number}]")

        with allure.step(f"Добавление товара #{product_number} в сравнение"):
            actions = ActionChains(self.driver)
            actions.move_to_element(self.find(product_locator))
            actions.move_to_element(self.find(compare_locator)).click().perform()

    def click_compare_button_in_notification(self):
        with allure.step("Нажатие кнопки сравнения в уведомлении"):
            self.wait_until_visible(loc.button_comparison_list_loc).click()

    def verify_compare_list_has_products(self, expected_count):
        with allure.step(f"Проверка что в сравнении {expected_count} товара(ов)"):
            product_items = self.find_all(loc.product_items_loc)
            assert len(product_items) == expected_count
