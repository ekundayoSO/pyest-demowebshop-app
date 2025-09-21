
from selenium.webdriver.common.by import By

class DeleteProductInShoppingCartLocators:

    UPDATE_SHOPPING_CART_BTN = (By.CSS_SELECTOR, 'input[value="Update shopping cart"]')
    QTY_OF_PRODUCTS_IN_CART = (By.CSS_SELECTOR, 'li a.ico-cart span.cart-qty')

