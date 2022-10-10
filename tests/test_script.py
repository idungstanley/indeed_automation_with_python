import time
import pytest
from TestData.ContactPageData import ContactPageData
from TestData.LoginPageData import LoginPageData
from TestData.QuestionPage import QuestionPageData
from pageObject.LoginPage import LoginPage
from pageObject.contactInfo import ContactInfo
from pageObject.questionsPage import Questions
from pageObject.savesJobsPage import SavedJobs
from utilities.BaseClass import BaseClass


class TestApplication(BaseClass):
    def test_visit_and_login(self, get_login_data):
        LoginPage.enter_email(self, get_login_data["email"])
        self.scroll_down()
        LoginPage.submit_email(self)
        time.sleep(3)
        LoginPage.click_link_pw(self)
        LoginPage.enter_password(self, get_login_data["password"])
        LoginPage.submit_password(self)

    # Navigate to saved jobs
    def test_apply_from_saved_jobs(self, get_contact_data, get_question_data):
        self.driver.get("https://myjobs.indeed.com/saved")
        saved_jobs = SavedJobs.apply_now_btn(self)
        for job in saved_jobs:
            job.click()
            windows = self.driver.window_handles
            self.driver.switch_to.window(windows[1])
            try:
                time.sleep(2)
                SavedJobs.apply_for_job.click(self)
            finally:
                print("no word")
            # add your information
            try:
                ContactInfo.enter_firstname(self, get_contact_data["first_name"])
                ContactInfo.enter_lastname(self, get_contact_data["last_name"])
                ContactInfo.enter_number(self, get_contact_data["number"])
                self.scroll_down()
                self.click_continue(self)
            finally:
                print("add information done")
            #### Add Cv
            try:
                self.scroll_down()
                self.click_continue(self)
            finally:
                print("Cv uploaded")

            #### Job experience
            try:
                heading = Questions.confirm_heading(self)
                if "Questions" in heading:
                    list_questions = Questions.list_of_questions(self)
                    for question in list_questions:
                        if question == "Address":
                            Questions.input_questions(self, get_question_data["Address"])
                        elif question == "City":
                            Questions.input_questions(self, get_question_data["City"])
                        elif question == "State":
                            Questions.input_questions(self, get_question_data["State"])
                        elif question == "Postal Code":
                            Questions.input_questions(self, get_question_data["Postal Code"])
                        elif question == "Do you live in the United Kingdom?":
                            Questions.select_radio_option(self, "yes")
                        elif question == "Do you require employer sponsorship to work in the UK?*":
                            Questions.select_radio_option(self, "yes")
                        elif question == "What's your highest level of education completed?":
                            Questions.select_dropdown(self, get_question_data["education"])
                        elif question == "Desired salary":
                            Questions.input_questions(self, get_question_data["salary"])
                    self.scroll_down()
                    self.click_continue()
            finally:
                print("job experience done")

            ##### preview application
            try:
                self.scroll_down()
                self.click_continue()
            finally:
                print("application submitted")

    @pytest.fixture(params=LoginPageData.test_login_data)
    def get_login_data(self, request):
        return request.param

    @pytest.fixture(params=ContactPageData.test_contact_data)
    def get_contact_data(self, request):
        return request.param

    @pytest.fixture(params=QuestionPageData.questions_and_answers)
    def get_question_data(self, request):
        return request.param
