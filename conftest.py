from playwright.sync_api import Page
import pytest
from pages.create_account_page import CreateAccPage
from pages.eco_friendly_catalog_page import EFCatalogPage
from pages.sale_page import SalePage
from pages.profile_page import ProfilePage

@pytest.fixture(scope="function")
def page(context):
    page: Page = context.new_page()
    yield page
    page.close()

@pytest.fixture()
def create_acc_page(page):
    return CreateAccPage(page)

@pytest.fixture()
def ef_catalog_page(page):
    return EFCatalogPage(page)

@pytest.fixture()
def sale_page(page):
    return SalePage(page)

@pytest.fixture()
def profile_page(page):
    return ProfilePage(page)