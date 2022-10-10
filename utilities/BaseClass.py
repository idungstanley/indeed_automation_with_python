import pytest
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures('setup')
class BaseClass:
    continue_btn = (By.CLASS_NAME, "ia-continueButton")

    def scroll_down(self):
        return self.driver.execute_script("window.scrollBy(0, document.body.scrollHeight)")

    def click_continue(self):
        return self.driver.find_element(*BaseClass.continue_btn).click()
