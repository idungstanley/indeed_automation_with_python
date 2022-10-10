import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope='class')
def setup(request):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("head")
    chrome_options.add_argument("--start-maximized")
    service_obj = Service("/Users/USER/Documents/chromedriver/chromedriver")
    driver = webdriver.Chrome(service=service_obj, options=chrome_options)
    home = "https://secure.indeed.com/auth?hl=en_NG&co=NG&continue=https%3A%2F%2Fng.indeed.com%2F&tmpl=desktop&service=my&from=gnav-util-homepage&jsContinue=https%3A%2F%2Fng.indeed.com%2F&empContinue=https%3A%2F%2Faccount.indeed.com%2Fmyaccess&_ga=2.198173101.340449773.1665348080-423117004.1665348080"
    driver.get(home)
    driver.maximize_window()
    request.cls.driver = driver
