from selenium.webdriver.common.by import By

from pageObjects.confirmPage import ConfirmPage


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver

    card = (By.CSS_SELECTOR, ".card-title a")
    card_button = (By.CSS_SELECTOR, ".card-footer button")
    check_out = (By.CSS_SELECTOR, ".btn.btn-success")
    checkout_text = (By.CSS_SELECTOR, "a[class$='nav-link btn btn-primary']")
    product_text = (By.XPATH, "//td/div/div/h4/a")
    checkout_button = (By.CSS_SELECTOR, "a[class$='nav-link btn btn-primary']")

    def get_card_items(self):
        return self.driver.find_elements(*CheckoutPage.card)

    def get_card_button(self):
        return self.driver.find_elements(*CheckoutPage.card_button)

    def get_checkout_button(self):
        return self.driver.find_element(*CheckoutPage.check_out)

    def get_checkout_text(self):
        return self.driver.find_element(*CheckoutPage.checkout_text)

    def get_product_text(self):
        return self.driver.find_element(*CheckoutPage.product_text)

    def get_checkout_shop_button(self):
        self.driver.find_element(*CheckoutPage.checkout_button).click()
        confirm_page = ConfirmPage(self.driver)
        return confirm_page
