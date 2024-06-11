import allure


@allure.title('Creating account')
def test_create_acc(create_acc_page, profile_page):
    create_acc_page.open_page()
    create_acc_page.fill_name_field()
    create_acc_page.fill_last_name_field()
    create_acc_page.fill_email_field()
    create_acc_page.fill_same_passwords_field()
    create_acc_page.check_button_is_enable()
    create_acc_page.click_create_acc_button()
    profile_page.check_reg_succes()

@allure.title('Negative. Creating account with different passwords')
def test_error_with_different_passwords(create_acc_page):
    create_acc_page.open_page()
    create_acc_page.fill_name_field()
    create_acc_page.fill_last_name_field()
    create_acc_page.fill_email_field()
    create_acc_page.fill_different_passwords()
    create_acc_page.check_button_is_enable()
    create_acc_page.click_create_acc_button()
    create_acc_page.check_conf_pass_error_is_('Please enter the same value again.')

@allure.title('Cheking errors under epty fields')
def test_empty_fields_errors(create_acc_page):
    create_acc_page.open_page()
    create_acc_page.check_button_is_enable()
    create_acc_page.click_create_acc_button()
    create_acc_page.check_name_error_is_('This is a required field.')
    create_acc_page.check_last_name_error_is_('This is a required field.')
    create_acc_page.check_email_error_is_('This is a required field.')
    create_acc_page.check_pass_error_is_('This is a required field.')
    create_acc_page.check_conf_pass_error_is_('This is a required field.')

@allure.title('Checking title on the creating account page')
def test_check_title(create_acc_page):
    create_acc_page.open_page()
    create_acc_page.check_title_is_('Create New Customer Account')