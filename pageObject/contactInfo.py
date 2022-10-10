from selenium.webdriver.common.by import By


class ContactInfo:
    def __int__(self, driver):
        self.driver = driver

    first_name = (By.XPATH, "//input[@name='firstName']")
    last_name = (By.XPATH, "//input[@name='lastName']")
    phone_number = (By.ID, "input-phoneNumber")
    continue_btn = (By.CLASS_NAME, "ia-continueButton")

    def enter_firstname(self, firstname):
        return self.driver.find_element(*ContactInfo.first_name).send_keys(firstname)

    def enter_lastname(self, lastname):
        return self.driver.find_element(*ContactInfo.last_name).send_keys(lastname)

    def enter_number(self, number):
        return self.driver.find_element(*ContactInfo.phone_number).send_keys(number)

    def click_continue(self):
        return self.driver.find_element(*ContactInfo.continue_btn).click()


