from pages.base_page import BasePage
from locators import ef_catalog_locators as loc
from playwright.sync_api import expect
import allure


class EFCatalogPage(BasePage):
    PAGE_URL = 'collections/eco-friendly.html'

    @allure.step('Check the title on the page')
    def check_title_is_(self, text):
        title = self.find(loc.eco_friendly_title)
        expect(title).to_be_visible()
        expect(title).to_have_text(text)

    @allure.step('Check products count on the page')
    def check_products_count(self, count: int):
        product_list = self.find_all(loc.one_item)
        assert len(product_list) == count

    @allure.step('Click on the sort button')
    def click_sort_button(self):
        button = self.find(loc.sort_button).locator('nth=0')
        button.click()

    @allure.step('Select sort by price')
    def select_price_sort(self):
        self.find(loc.sort_button).locator('nth=0').select_option('price')

    @allure.step('Select sort by name')
    def select_name_sort(self):
        self.find(loc.sort_button).locator('nth=0').select_option('name')

    @allure.step('Select sort by position')
    def select_position_sort(self):
        self.find(loc.sort_button).locator('nth=0').select_option('position')

    @allure.step('Checking ascending sort')
    def check_ascending_price_sorting(self):
        items_count = len(self.find_all(loc.one_item))
        prices_list = []
        for i in range(1, items_count + 1):
            item_price = self.find(f'//li[@class="item product product-item"][{i}]/descendant::*[@class="price"]').text_content()
            prices_list.append(float(item_price[1::]))
        assert prices_list == sorted(prices_list)

    @allure.step('Checking descending sort')
    def check_descending_price_sorting(self):
        items_count = len(self.find_all(loc.one_item))
        prices_list = []
        for i in range(1, items_count + 1):
            item_price = self.find(f'//li[@class="item product product-item"][{i}]/descendant::*[@class="price"]').text_content()
            prices_list.append(float(item_price[1::]))
        assert prices_list == sorted(prices_list, reverse=True)