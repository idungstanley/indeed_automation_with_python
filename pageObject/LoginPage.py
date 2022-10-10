from selenium.webdriver.common.by import By


class LoginPage:
    def __int__(self, driver):
        self.driver = driver

    emailSelector = (By.NAME, "__email")
    emailSubmit = (By.XPATH, "//button[@data-tn-element='auth-page-email-submit-button']")
    linkToPassword = (By.ID, "auth-page-google-password-fallback")
    passwordSelector = (By.NAME, "__password")
    passwordSubmit = (By.XPATH, "//button[@type='submit']")

    def enter_email(self, email):
        return self.driver.find_element(*LoginPage.emailSelector).send_keys(email)

    def submit_email(self):
        return self.driver.find_element(*LoginPage.emailSubmit).click()

    def click_link_pw(self):
        return self.driver.find_element(*LoginPage.linkToPassword).click()

    def enter_password(self, password):
        return self.driver.find_element(*LoginPage.passwordSelector).send_keys(password)

    def submit_password(self):
        return self.driver.find_element(*LoginPage.passwordSubmit).click()
