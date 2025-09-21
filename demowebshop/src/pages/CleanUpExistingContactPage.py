from demowebshop.src.pages.SeleniumExtended import SeleniumExtended
from demowebshop.src.pages.locators.CleanUpExistingContactLocators import CleanUpExistingContactLocators


class CleanUpExistingContactPage(CleanUpExistingContactLocators):

    def __init__(self, driver):
        self.driver = driver
        self.selenium = SeleniumExtended(self.driver)

    def wait_for_order_completed_text(self):
        self.selenium.wait_until_element_is_visible(self.ORDER_COMPLETED_TEXT)

    def click_email_link_text(self):
        self.selenium.wait_and_click(self.MY_ACCOUNT_EMAIL_LINK_TEXT)

    def click_my_account_email_link_text(self):
        self.selenium.wait_and_click(self.MY_ACCOUNT_ADDRESS_LINK_TEXT)

    def click_my_account_address_delete_btn(self):
        self.selenium.wait_and_click(self.MY_ACCOUNT_ADDRESS_DELETE_BTN)

    def confirm_javascript_alert(self):
        self.driver.switch_to.alert.accept()

    def delete_existing_user_contact(self):
        self.wait_for_order_completed_text()
        self.click_email_link_text()
        self.click_my_account_email_link_text()
        self.click_my_account_address_delete_btn()
        self.confirm_javascript_alert()