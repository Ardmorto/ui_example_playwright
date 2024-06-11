from pages.base_page import BasePage
from faker import Faker
from locators import create_acc_locators as loc
from playwright.sync_api import expect
import allure


class CreateAccPage(BasePage):
    PAGE_URL = 'customer/account/create/'
    fake = Faker(locale='ru_RU')

    @allure.step('Filling the name field')
    def fill_name_field(self):
        field = self.find(loc.name_field)
        field.fill(self.fake.first_name())

    @allure.step('Filling the last name field')
    def fill_last_name_field(self):
        field = self.find(loc.last_name_field)
        field.fill(self.fake.last_name())

    @allure.step('Filling the emsil field')
    def fill_email_field(self):
        field = self.find(loc.email_field)
        field.fill(self.fake.free_email())

    @allure.step('Filling password ans confirmation fields with same password')
    def fill_same_passwords_field(self):
        pass_field = self.find(loc.password_field)
        confirm_field = self.find(loc.password_confirm_field)
        password = self.fake.password()
        pass_field.fill(password)
        confirm_field.fill(password)

    @allure.step('Filling password and confirmation fields with different passwords')
    def fill_different_passwords(self):
        pass_field = self.find(loc.password_field)
        confirm_field = self.find(loc.password_confirm_field)
        pass_field.fill(self.fake.password())
        confirm_field.fill(self.fake.password())

    @allure.step('Checking that creating button is enabled')
    def check_button_is_enable(self):
        button = self.find(loc.create_acc_button)
        expect(button).to_be_enabled()

    @allure.step('Click create button')
    def click_create_acc_button(self):
        button = self.find(loc.create_acc_button)
        button.click()

    @allure.step('Check name error')
    def check_name_error_is_(self, text):
        name_error = self.find(loc.name_error)
        expect(name_error).to_be_visible()
        expect(name_error).to_have_text(text)

    @allure.step('Check last name error')
    def check_last_name_error_is_(self, text):
        last_name_error = self.find(loc.last_name_error)
        expect(last_name_error).to_be_visible()
        expect(last_name_error).to_have_text(text)

    @allure.step('Check email error')
    def check_email_error_is_(self, text):
        email_error = self.find(loc.email_error)
        expect(email_error).to_be_visible()
        expect(email_error).to_have_text(text)

    @allure.step('Check password error')
    def check_pass_error_is_(self, text):
        password_error = self.find(loc.password_error)
        expect(password_error).to_be_visible()
        expect(password_error).to_have_text(text)

    @allure.step('Check confirmation password error')
    def check_conf_pass_error_is_(self, text):
        conf_pass_error = self.find(loc.conf_pass_error)
        expect(conf_pass_error).to_be_visible()
        expect(conf_pass_error).to_have_text(text)

    @allure.step('Сhecking the title on the page')
    def check_title_is_(self, text):
        title = self.find(loc.create_acc_title)
        expect(title).to_be_visible()
        expect(title).to_have_text(text)