import allure


@allure.title('Checking title on the Sale page')
def test_sale_page_title(sale_page):
    sale_page.open_page()
    sale_page.check_title_is_('Sale')

@allure.title('Checking redirection on the women sale page')
def test_redirect_to_women_sale_page(sale_page):
    sale_page.open_page()
    sale_page.check_wd_button_is_enabled()
    sale_page.click_wd_button()
    sale_page.wait_until_page_load()
    sale_page.check_redirect_to_women_sale()

@allure.title('Checking the text in the md banner')
def test_md_banner_text(sale_page):
    sale_page.open_page()
    sale_page.check_md_banner_text_is_('Men’s Bargains')

@allure.title('Checking the text in the lg banner')
def test_lg_banner_text(sale_page):
    sale_page.open_page()
    sale_page.check_lg_banner_text_is_('Luma Gear Steals')