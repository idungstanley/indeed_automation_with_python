from selenium.webdriver.common.by import By


class SavedJobs:
    def __int__(self, driver):
        self.driver = driver

    applyBtn = (By.LINK_TEXT, "Apply now")
    apply_for_job = (By.CLASS_NAME, "ia-IndeedApplyButton")

    def apply_now_btn(self):
        return self.driver.find_elements(*SavedJobs.applyBtn)

    def click_apply_job(self):
        return self.driver.find_element(*SavedJobs.apply_for_job)

