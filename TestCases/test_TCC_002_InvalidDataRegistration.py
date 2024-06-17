from Base import InitiateDriver
from selenium.webdriver.common.by import By
from Library import ConfigReader

def test_registration_invalid_data():
    driver = InitiateDriver.startBrowser()
    driver.find_element(by=By.NAME,value=ConfigReader.fetchelementLocators("Registration","password_name")).send_keys("hello")