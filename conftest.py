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
    options.page_load_strategy = "eager"

    if os.getenv('CI') == 'true':
        options.add_argument("--headless")  # Без графического интерфейса
        options.add_argument("--no-sandbox")  # Необходимо для Linux
        options.add_argument("--disable-dev-shm-usage")  # Для ограниченных ресурсов
        options.add_argument("--disable-gpu")  # Отключение GPU в CI
        service = Service(executable_path='/usr/bin/chromedriver')
    else:    
        options.add_experimental_option("detach", True)
        service = Service()
        
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


