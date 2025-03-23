from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class BasePage:
    base_url = "https://magento.softwaretestingboard.com"
    page_url = None

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def open_page(self):
        with allure.step(f"Открываем страницу"):
            if self.page_url:
                self.driver.get(f"{self.base_url}{self.page_url}")
            else:
                raise NotImplementedError("Страница не может быть открыта")

    def find(self, locator):
        return self.driver.find_element(*locator)

    def find_all(self, locator):
        return self.driver.find_elements(*locator)

    def wait_until_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))
