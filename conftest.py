import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from pages.collections import CollectionPage
from pages.customer import CustomerPage
from pages.sale import SalePage

@pytest.fixture()
def driver():
    options = Options()
    options.page_load_strategy = "eager"
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    
    yield driver
    chrome_driver.save_screenshot(f'screen{random.randrange(1, 10000)}.png') 
    driver.quit()

@pytest.fixture()
def customer_page(driver):
    return CustomerPage(driver)

@pytest.fixture()
def collection_page(driver):
    return CollectionPage(driver)

@pytest.fixture()
def sale_page(driver):
    return SalePage(driver)
