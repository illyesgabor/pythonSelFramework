from selenium.webdriver.common.by import By


class ConfirmPage:

    def __init__(self,driver):
        self.driver = driver

    country_selector = (By.CSS_SELECTOR, "input[id='country']")
    country_link_text = (By.LINK_TEXT, "Hungary")
    terms_cons = (By.CSS_SELECTOR, "label[for='checkbox2']")
    purchase_btn = (By.CSS_SELECTOR, "input[type='submit']")
    success_msg = (By.CSS_SELECTOR, ".alert.alert-success.alert-dismissible")

    def get_country(self):
        return self.driver.find_element(*ConfirmPage.country_selector)

    def get_country_link_text(self):
        return self.driver.find_element(*ConfirmPage.country_link_text)

    def get_checkbox_ts(self):
        return self.driver.find_element(*ConfirmPage.terms_cons)

    def get_purchase_btn(self):
        return self.driver.find_element(*ConfirmPage.purchase_btn)

    def get_success_msg(self):
        return self.driver.find_element(*ConfirmPage.success_msg)
