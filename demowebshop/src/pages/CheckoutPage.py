from demowebshop.src.pages.SeleniumExtended import SeleniumExtended
from demowebshop.src.pages.locators.CheckoutLocators import CheckoutLocators


class CheckoutPage(CheckoutLocators):

    def __init__(self, driver):
        self.driver = driver
        self.selenium = SeleniumExtended(self.driver)

    def click_on_service_term(self):
        self.selenium.wait_and_click(self.TERM_OF_SERVICE)

    def click_on_checkout_btn(self):
        self.selenium.wait_and_click(self.CHECKOUT_BUTTON)

    def select_country_dropdown(self, country):
        country = 'Select country' if not country else country
        self.selenium.wait_select_dropdown(self.BILLING_COUNTRY, to_select=country, select_by="visible_test")

    def select_billing_country(self, country=None):
        self.selenium.wait_select_dropdown(self.BILLING_COUNTRY_DROPDOWN, to_select=country, select_by="visible_text")

    def input_billing_city(self, city=None):
        self.selenium.wait_and_input_text(self.BILLING_CITY, city)

    def input_billing_address1(self, address1=None):
        self.selenium.wait_and_input_text(self.BILLING_ADDRESS1, address1)

    def input_billing_postal_code(self, zip_code=None):
        self.selenium.wait_and_input_text(self.BILLING_POSTAL_CODE, zip_code)

    def input_billing_phone_number(self, phone=None):
        self.selenium.wait_and_input_text(self.BILLING_PHONE_NUMBER, phone)

    def click_billing_continue_btn(self):
        self.selenium.wait_and_click(self.BILLING_CONTINUE_BUTTON)

    def click_shipping_address_btn(self):
        self.selenium.wait_and_click(self.SHIPPING_ADDRESS_BUTTON)

    def click_shipping_method_btn(self):
        self.selenium.wait_and_click(self.SHIPPING_METHOD_BUTTON)

    def click_payment_method_btn(self):
        self.selenium.wait_and_click(self.PAYMENT_METHOD_BUTTON)

    def click_payment_info_btn(self):
        self.selenium.wait_and_click(self.PAYMENT_INFO_BUTTON)

    def click_confirm_order_btn(self):
        self.selenium.wait_and_click(self.CONFIRM_ORDER_BUTTON)

    def billing_info(self, country=None, city=None, address1=None, zip_code=None, phone=None):
        self.select_billing_country(country=country)
        self.input_billing_city(city=city)
        self.input_billing_address1(address1=address1)
        self.input_billing_postal_code(zip_code=zip_code)
        self.input_billing_phone_number(phone=phone)

    def shipping_info(self):
        self.click_shipping_address_btn()
        self.click_shipping_method_btn()

    def payment_info(self):
        self.click_payment_method_btn()
        self.click_payment_info_btn()

