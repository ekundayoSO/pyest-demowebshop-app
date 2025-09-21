from demowebshop.src.helpers.config_helpers import get_base_url
from demowebshop.src.pages.SeleniumExtended import SeleniumExtended
from demowebshop.src.pages.locators.AddProductsToCartLocators import AddProductsToCartLocators


class AddProductsToCartPage(AddProductsToCartLocators):

    def __init__(self, driver):
        self.driver = driver
        self.selenium = SeleniumExtended(self.driver)

    def go_to_homepage(self):
        base_url = get_base_url()
        self.selenium.driver.get(base_url)
        self.driver.fullscreen_window()

    def search_item_and_click_enter(self, item):
        self.selenium.wait_and_input_text_and_click_enter(self.SEARCH_STORE_FIELD, item)

    def add_items_to_cart(self):
        self.selenium.wait_and_click(self.ADD_TO_CART_BTN)

    def bar_notification_visible(self):
        self.selenium.wait_until_element_is_visible(self.BAR_NOTIFICATION)

    def click_cart_element(self):
        self.selenium.wait_and_click(self.CART_ELEMENT_LINK)

    def get_all_product_names_in_cart(self):
        product_name_elements = self.selenium.wait_and_get_elements(self.PRODUCT_NAME_IN_CART)
        product_names = []
        for name in product_name_elements:
            product_names.append(name.text)
        return product_names

