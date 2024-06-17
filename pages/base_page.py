import re
from playwright.sync_api import Page, expect
import allure


class BasePage:
    BASE_URL = 'https://magento.softwaretestingboard.com/'
    PAGE_URL = None

    def __init__(self, page: Page):
        self.page = page

    @allure.step('Open the page')
    def open_page(self):
        if self.PAGE_URL:
            self.page.goto(f'{self.BASE_URL}{self.PAGE_URL}')
        else:
            raise NotImplementedError('Unable to open the page')

    def find(self, locator):
        return self.page.locator(locator)

    def find_all(self, locator):
        return self.page.query_selector_all(locator)

    @allure.step('Waiting until page is load')
    def wait_until_page_load(self):
        self.page.wait_for_function("document.readyState === 'complete'")

    def wait_until_url_have_(self, text: str):
        expect(self.page).to_have_url(re.compile(f".*{text}"), timeout=30000)