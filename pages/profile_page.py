from pages.base_page import BasePage
from locators import profile_locators as loc
from playwright.sync_api import expect
import allure

class ProfilePage(BasePage):
    PAGE_URL = 'customer/account/'

    @allure.step('Check registration message on the page')
    def check_reg_succes(self):
        reg_message = self.find(loc.registration_thank)
        expect(reg_message).to_have_text('Thank you for registering with Main Website Store.')