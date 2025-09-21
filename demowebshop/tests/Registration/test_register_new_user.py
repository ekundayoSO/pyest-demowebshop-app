from time import sleep

from demowebshop.src.pages.RegisterNewUserPage import RegisterNewUserPage
from demowebshop.src.helpers.random_email_helpers import generate_random_email_and_password
import pytest

@pytest.mark.usefixtures('init_driver')
class TestRegisterNewUser:

    @pytest.mark.tcid1
    def test_verify_new_user_registration(self):

        random_email = generate_random_email_and_password()
        register = RegisterNewUserPage(self.driver)

        register.go_to_homepage()
        register.select_gender()
        register.input_first_name('David')
        register.input_last_name('Moore')
        register.input_email(random_email["email"])
        register.input_password('Demo2025#')
        register.confirmed_password('Demo2025#')
        register.click_on_register_button()

        # Verify new user is registered successfully
        register.verify_registration_is_successful()