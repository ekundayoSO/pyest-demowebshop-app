from demowebshop.src.pages.SeleniumExtended import SeleniumExtended
from demowebshop.src.pages.locators.DeleteProductInShoppingCartLocators import DeleteProductInShoppingCartLocators
from selenium.webdriver.common.by import By

class DeleteProductInShoppingCartPage(DeleteProductInShoppingCartLocators):

    def __init__(self, driver):
        self.driver = driver
        self.selenium = SeleniumExtended(self.driver)

    def delete_single_product(self, product_name):
        checkbox_locator = (
            By.XPATH,
            f"//td[@class='product']/a[text()='{product_name}']/ancestor::tr//input[@name='removefromcart']"
        )
        self.selenium.wait_and_click(checkbox_locator)

    def update_shopping_cart(self):
        self.selenium.wait_and_click(self.UPDATE_SHOPPING_CART_BTN)

    def count_products_left_in_shopping_cart(self, qty):
        expected_qty = str(qty)
        self.selenium.wait_until_element_contains_text(self.QTY_OF_PRODUCTS_IN_CART, expected_qty)
