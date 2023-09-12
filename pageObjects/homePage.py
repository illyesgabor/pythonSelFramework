from selenium.webdriver.common.by import By

from pageObjects.checkoutPage import CheckoutPage


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    shop = (By.CSS_SELECTOR, "a[href*='shop']")
    email = (By.NAME, "email")
    password = (By.ID, "exampleInputPassword1")
    checkbox = (By.ID, "exampleCheck1")
    radio_button = (By.CSS_SELECTOR, "input[id='inlineRadio1']")
    dropdown = (By.ID, "exampleFormControlSelect1")
    name = (By.CSS_SELECTOR, "input[name='name']")
    text = (By.XPATH, "//input[@type='text']")
    submit_btn = (By.CSS_SELECTOR, "input[type='submit']")
    message = (By.CLASS_NAME, "alert-success")
    clear_msg = (By.XPATH, "(//input[@type='text'])[3]")

    def shop_item(self):
        self.driver.find_element(*HomePage.shop).click()
        checkout_page = CheckoutPage(self.driver)
        return checkout_page

    def get_email(self):
        return self.driver.find_element(*HomePage.email)

    def get_password(self):
        return self.driver.find_element(*HomePage.password)

    def get_checkbox(self):
        return self.driver.find_element(*HomePage.checkbox)

    def get_radio_button(self):
        return self.driver.find_element(*HomePage.radio_button)

    def get_dropdown(self):
        return self.driver.find_element(*HomePage.dropdown)

    def get_name(self):
        return self.driver.find_element(*HomePage.name)

    def get_text(self):
        return self.driver.find_element(*HomePage.text)

    def get_submit_btn(self):
        return self.driver.find_element(*HomePage.submit_btn)

    def get_message(self):
        return self.driver.find_element(*HomePage.message)

    def get_clear_msg(self):
        return self.driver.find_element(*HomePage.clear_msg)
