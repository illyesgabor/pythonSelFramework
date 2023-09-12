import pytest

from TestData.HomePageData import HomePageData
from pageObjects.homePage import HomePage
from utilities.BaseClass import BaseClass


class TestHomepage(BaseClass):

    def test_for_submission(self, get_data):
        home_page = HomePage(self.driver)
        home_page.get_name().send_keys(get_data["firstname"])
        home_page.get_email().send_keys(get_data["lastname"])
        home_page.get_password().send_keys("test")
        home_page.get_checkbox().click()
        home_page.get_radio_button().click()
        self.select_option_by_text(home_page.get_dropdown(), get_data["gender"])
        home_page.get_text().send_keys("hello")
        home_page.get_submit_btn().click()
        message = home_page.get_message().text
        print(message)
        home_page.get_clear_msg().clear()
        assert "Success" in message
        self.driver.refresh()

    @pytest.fixture(params=HomePageData.get_test_data("testcase2"))
    def get_data(self, request):
        return request.param
