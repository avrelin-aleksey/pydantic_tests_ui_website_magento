from selenium import webdriver
import allure
import pytest

from selenium import webdriver
from pages.collections import CollectionPage
from pages.customer import CustomerPage
from pages.sale import SalePage
from selenium.webdriver.chrome.options import Options



@pytest.fixture()
def driver():
    options = Options()
    options.add_experimental_option("detach", True)
    options.page_load_strategy = "eager"
    chrome_driver = webdriver.Chrome(options=options)
    chrome_driver.maximize_window()
    yield chrome_driver
    chrome_driver.quit()


@pytest.fixture()
def customer_page(driver):
    return CustomerPage(driver)


@pytest.fixture()
def collection_page(driver):
    return CollectionPage(driver)

@pytest.fixture()
def sale_page(driver):
    return SalePage(driver)


