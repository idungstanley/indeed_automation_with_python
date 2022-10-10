from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class Questions:
    def __int__(self, driver):
        self.driver = driver

    heading = (By.CSS_SELECTOR, "h1[class ='ia-BasePage-heading fs-unmask']")
    question_div = (By.CSS_SELECTOR, "span[class ='css-1ux7cjx e1wnkr790']")
    input_questions = (By.CSS_SELECTOR, "input[class ='css-1ytox4c e1jgz0i3']")
    radio_btn = (By.CSS_SELECTOR, "label[class ='css-d0lawn es2vvo70'] input[type='radio']")
    dropdown = (By.CSS_SELECTOR, "select[class ='css-5mhq3o eh9h2790']")

    def confirm_heading(self):
        return self.driver.find_element(*Questions.headin).text

    def list_of_questions(self):
        return self.driver.find_element(*Questions.question_div)

    def input_questions(self, question):
        return self.driver.find_element(*Questions.input_questions).send_keys(question)

    def select_radio_option(self, answer):
        self.driver.find_element(*Questions.radio_btn)
        for option in self.driver.find_element(*Questions.radio_btn):
            if option.get_attribute("value") == answer:
                option.click()

    def select_dropdown(self, answer):
        select = Select(self.driver.find_element(*Questions.dropdown))
        return select.select_by_visible_text(answer)



