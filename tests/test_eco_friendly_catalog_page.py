import allure


@allure.title('Checking title on the Eco Friendly catalod page')
def test_check_title(ef_catalog_page):
    ef_catalog_page.open_page()
    ef_catalog_page.check_title_is_('Eco Friendly')

@allure.title('Cheking default number of products on the page')
def test_number_of_displayed_items(ef_catalog_page):
    ef_catalog_page.open_page()
    ef_catalog_page.check_products_count(12)

@allure.title('Test ascending sorting by price')
def test_ascending_price_sorting(ef_catalog_page):
    ef_catalog_page.open_page()
    ef_catalog_page.click_sort_button()
    ef_catalog_page.select_price_sort()
    ef_catalog_page.wait_until_page_load()
    ef_catalog_page.check_ascending_price_sorting()

@allure.title('Test descending sorting by price')
def test_descending_price_sorting(ef_catalog_page):
    ef_catalog_page.open_page()
    ef_catalog_page.click_sort_button()
    ef_catalog_page.select_price_sort()
    ef_catalog_page.switch_sort_direction()
    ef_catalog_page.wait_until_page_load()
    ef_catalog_page.check_descending_price_sorting()