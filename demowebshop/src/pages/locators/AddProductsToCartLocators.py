
from selenium.webdriver.common.by import By

class AddProductsToCartLocators:

    SEARCH_STORE_FIELD = (By.ID, "small-searchterms")
    ADD_TO_CART_BTN = (By.CSS_SELECTOR, 'input[value="Add to cart"]')
    CART_QTY_INDICATOR =(By.CSS_SELECTOR, 'li a.ico-cart span.cart-qty')
    BAR_NOTIFICATION = (By.CSS_SELECTOR, 'div#bar-notification p.content')
    CART_ELEMENT_LINK = (By.CSS_SELECTOR, 'li a.ico-cart span.cart-label')
    PRODUCT_NAME_IN_CART = (By.CSS_SELECTOR, 'tr td.product')