

from selenium.webdriver.common.by import By

class CleanUpExistingContactLocators:

    MY_ACCOUNT_EMAIL_LINK_TEXT = (By.CSS_SELECTOR, 'div.header-links li a.account')
    MY_ACCOUNT_ADDRESS_LINK_TEXT = (By.CSS_SELECTOR, 'div.block-account-navigation a[href="/customer/addresses"]')
    MY_ACCOUNT_ADDRESS_DELETE_BTN = (By.CSS_SELECTOR, 'input[value=Delete]')
    ORDER_COMPLETED_TEXT = (By.CSS_SELECTOR, 'div.order-completed strong')
    NO_ADDRESS_TEXT = (By.CSS_SELECTOR, 'div.page div.address-list')
