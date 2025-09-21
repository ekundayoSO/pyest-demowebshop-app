from time import sleep

import pytest
from demowebshop.src.configs.generic_configs import GenericConfigs
from demowebshop.src.pages.LoginPage import LoginPage


@pytest.mark.usefixtures('init_driver')
class TestLoginWithInValidCredentials:

    @pytest.mark.tcid3
    def test_verify_login_with_invalid_email(self):
        credentials = GenericConfigs()
        login = LoginPage(self.driver)

        login.go_to_login_page()
        login.input_login_email('vpc@gmail.com')
        login.input_login_password(credentials.LOGIN_PASSWORD)
        login.click_on_login_btn()

        # Verify login is successful
        expected_err = 'Login was unsuccessful. Please correct the errors and try again'
        login.wait_until_error_is_displayed(expected_err)

