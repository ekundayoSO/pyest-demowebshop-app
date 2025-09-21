
from selenium.webdriver.common.by import By


class CheckoutLocators:

    TERM_OF_SERVICE = (By.ID, 'termsofservice')
    CHECKOUT_BUTTON = (By.ID, 'checkout')

    # Billing Address
    BILLING_COUNTRY_DROPDOWN = (By.ID, 'BillingNewAddress_CountryId')
    BILLING_CITY = (By.ID, 'BillingNewAddress_City')
    BILLING_ADDRESS1 = (By.ID, 'BillingNewAddress_Address1')
    BILLING_POSTAL_CODE = (By.ID, 'BillingNewAddress_ZipPostalCode')
    BILLING_PHONE_NUMBER = (By.ID, 'BillingNewAddress_PhoneNumber')
    BILLING_CONTINUE_BUTTON = (By.CSS_SELECTOR, 'div.buttons input[onclick="Billing.save()"]')
    # Shipping Address
    SHIPPING_ADDRESS_BUTTON = (By.CSS_SELECTOR, 'div.buttons input[onclick="Shipping.save()"]')
    SHIPPING_METHOD_BUTTON = (By.CSS_SELECTOR, 'div.buttons input[onclick="ShippingMethod.save()"]')
    # Payment Method
    PAYMENT_METHOD_BUTTON = (By.CSS_SELECTOR, 'div.buttons input[onclick="PaymentMethod.save()"]')
    PAYMENT_INFO_BUTTON = (By.CSS_SELECTOR, 'div.buttons input[onclick="PaymentInfo.save()"]')
    # Confirm Order
    CONFIRM_ORDER_BUTTON = (By.CSS_SELECTOR, 'div.buttons input[onclick="ConfirmOrder.save()"]')



