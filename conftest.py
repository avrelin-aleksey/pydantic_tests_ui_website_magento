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
    
    # Настройки для CI 
    if os.getenv('CI') == 'true':
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-gpu")
        service = Service(executable_path='/usr/bin/chromedriver')
    else:
        # Настройки для локального запуска
        options.add_experimental_option("detach", True)
        service = Service()
    
    driver = webdriver.Chrome(service=service, options=options)
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
