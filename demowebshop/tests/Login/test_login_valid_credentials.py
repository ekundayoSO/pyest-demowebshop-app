import pytest
from demowebshop.src.configs.generic_configs import GenericConfigs
from demowebshop.src.pages.LoginPage import LoginPage


@pytest.mark.usefixtures('init_driver')
class TestLogin:

    @pytest.mark.tcid2
    def test_verify_login_with_valid_credentials(self):
        credentials = GenericConfigs()
        login = LoginPage(self.driver)

        login.go_to_login_page()
        login.input_login_email(credentials.LOGIN_EMAIL)
        login.input_login_password(credentials.LOGIN_PASSWORD)
        login.click_on_login_btn()

        # Verify login is successful
        login.verify_login_is_successful()

