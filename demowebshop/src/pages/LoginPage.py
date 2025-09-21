from demowebshop.src.helpers.config_helpers import get_base_url
from demowebshop.src.pages.SeleniumExtended import SeleniumExtended
from demowebshop.src.pages.locators.LoginLocators import LoginLocators


class LoginPage(LoginLocators):

    endpoint = '/login/'

    def __init__(self, driver):
        self.driver = driver
        self.selenium = SeleniumExtended(self.driver)

    def go_to_login_page(self):
        base_url = get_base_url()
        login_url = base_url + self.endpoint
        self.driver.get(login_url)
        self.driver.fullscreen_window()

    def click_login_header_btn(self):
        self.selenium.wait_and_click(self.LOGIN_HEADER_BTN)

    def input_login_email(self, email):
        self.selenium.wait_and_input_text(self.LOGIN_EMAIL, email)

    def input_login_password(self, password):
        self.selenium.wait_and_input_text(self.LOGIN_PASSWORD, password)

    def click_on_login_btn(self):
        self.selenium.wait_and_click(self.LOGIN_BTN)

    def verify_login_is_successful(self):
        self.selenium.wait_until_element_is_visible(self.SUCCESS_LOGIN_VERIFICATION)

    def wait_until_error_is_displayed(self, exp_err):
        self.selenium.wait_until_element_contains_text(self.INVALID_LOGIN_EMAIL_ERROR_MSG, exp_err)
