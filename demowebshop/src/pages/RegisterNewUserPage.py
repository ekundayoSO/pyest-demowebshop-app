from demowebshop.src.helpers.config_helpers import get_base_url
from demowebshop.src.pages.SeleniumExtended import SeleniumExtended
from demowebshop.src.pages.locators.RegisterNewUserLocators import RegisterNewUserLocators


class RegisterNewUserPage(RegisterNewUserLocators):

    endpoint = '/register/'

    def __init__(self, driver):
        self.driver = driver
        self.selenium = SeleniumExtended(driver)

    def go_to_homepage(self):
        base_url = get_base_url()
        my_account_url = base_url + self.endpoint
        self.driver.get(my_account_url)
        self.driver.fullscreen_window()

    def select_gender(self):
        self.selenium.wait_and_click(self.GENDER_BUTTON)

    def input_first_name(self, firstname):
        self.selenium.wait_and_input_text(self.FIRST_NAME_FIELD, firstname)

    def input_last_name(self, lastname):
        self.selenium.wait_and_input_text(self.LAST_NAME_FIELD, lastname)

    def input_email(self, email):
        self.selenium.wait_and_input_text(self.EMAIL_FIELD, email)

    def input_password(self, password):
        self.selenium.wait_and_input_text(self.PASSWORD_FIELD, password)

    def confirmed_password(self, confirm_passwd):
        self.selenium.wait_and_input_text(self.CONFIRM_PASSWORD_FIELD, confirm_passwd)

    def click_on_register_button(self):
        self.selenium.wait_and_click(self.REGISTER_BUTTON)

    def verify_registration_is_successful(self):
        self.selenium.wait_until_element_is_visible(self.REGISTRATION_VERIFICATION)