import allure


expected_page = "Sale"
expected_promo = [
    {
        "title": "Pristine prices on pants, tanks and bras.",
        "info": "Women’s Deals",
        "more": "Shop Women’s Deals",
    },
    {
        "title": "Men’s Bargains",
        "info": "Stretch your budget with active attire",
        "more": "Shop Men’s Deals",
    },
    {
        "title": "Luma Gear Steals",
        "info": "Your best efforts deserve a deal",
        "more": "Shop Luma Gear",
    },
    {
        "title": "20% OFF",
        "info": "Every $200-plus purchase!",
        "more": None,  # У этого блока нет кнопки "more"
    },
    {
        "title": "Spend $50 or more — shipping is free!",
        "info": "Buy more, save more",
        "more": None,  # У этого блока нет кнопки "more"
    },
    {
        "title": "You can't have too many tees",
        "info": "4 tees for the price of 3. Right now",
        "more": "Tees on sale",
    },
]


@allure.feature("Страница SALE")
class TestAccountCreation:
    @allure.title("Проверка ссылок на странице SALE")
    def test_sale_page(self, sale_page):
        # Открываем страницу
        sale_page.open_page()

        # Проверяем заголовок страницы
        sale_page.verify_page_title(expected_page)

        # Проверяем блоки с акциями
        sale_page.verify_promo_blocks(expected_promo)
