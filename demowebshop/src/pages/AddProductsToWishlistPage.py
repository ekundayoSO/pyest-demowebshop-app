from demowebshop.src.pages.SeleniumExtended import SeleniumExtended
from demowebshop.src.pages.locators.AddProductsToWishlistLocators import AddProductsToWishlistLocators


class AddProductsToWishlistPage(AddProductsToWishlistLocators):

    def __init__(self, driver):
        self.driver = driver
        self.selenium = SeleniumExtended(self.driver)

    def add_products_to_wishlist(self):
        self.selenium.wait_and_click(self.ADD_TO_WISHLIST_BTN)

    def click_product_card(self):
        self.selenium.wait_and_click(self.PRODUCT_CARD)

    def click_wishlist_element(self):
        self.selenium.wait_and_click(self.WISHLIST_ELEMENT_LINK)

    def get_all_product_names_in_wishlist(self):
        product_name_elements = self.selenium.wait_and_get_elements(self.PRODUCT_NAME_IN_WISHLIST)

        product_names = [name.text for name in product_name_elements]
        return product_names
