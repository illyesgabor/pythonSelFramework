import inspect
import logging

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


@pytest.mark.usefixtures("setup")
class BaseClass:

    def verify_link_presence(self, text_to_verify):
        wait = WebDriverWait(self.driver, 10)
        wait.until(ec.visibility_of_element_located((By.LINK_TEXT, text_to_verify)))

    def select_option_by_text(self, locator, text):
        dropdown = Select(locator)
        dropdown.select_by_visible_text(text)

    def getLogger(self):
        logger_name = inspect.stack()[1][3]
        logger = logging.getLogger(logger_name)

        file_handler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")

        file_handler.setFormatter(formatter)

        logger.addHandler(file_handler)

        logger.setLevel(logging.DEBUG)
        return logger
