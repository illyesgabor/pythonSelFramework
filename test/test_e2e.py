from pageObjects.homePage import HomePage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_e2e(self):

        log = self.getLogger()
        home_page = HomePage(self.driver)
        checkout_page = home_page.shop_item()
        log.info("Getting all card titles.")
        home_page.shop_item()

        content = checkout_page.get_card_items()
        i = -1
        for card in content:
            i = i+1
            card_text = card.text
            log.info(card_text)
            if card_text == "Blackberry":
                checkout_page.get_card_button()[i].click()

        checkout = checkout_page.get_checkout_text().text
        assert "Checkout ( 1 )" in checkout
        confirm_page = checkout_page.get_checkout_shop_button()

        product_name = checkout_page.get_product_text().text
        assert "Blackberry" in product_name
        checkout_page.get_checkout_button().click()
        log.info("Entering country name as Hun.")
        confirm_page.get_country().send_keys("Hun")
        self.verify_link_presence("Hungary")
        confirm_page.get_country_link_text().click()
        confirm_page.get_checkbox_ts().click()
        confirm_page.get_purchase_btn().click()

        success_msg = confirm_page.get_success_msg().text
        log.info("Text received from application is "+success_msg)
        assert "Success" in success_msg
