from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoAlertPresentException

import inspect
import unittest
import time

# Constant variable
registration_page_url = "https://demo.opencart.com/index.php?route=account/register"



class TestRegistration(unittest.TestCase):
    def is_alert_present(self):
        try:
            self.driver.switch_to.alert()
        except NoAlertPresentException: 
            return False

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="chromedriver.exe")
        self.driver.get(registration_page_url)

        self.firstname = self.driver.find_element_by_name("firstname")
        self.lastname = self.driver.find_element_by_name("lastname")
        self.email = self.driver.find_element_by_name("email")
        self.telephone = self.driver.find_element_by_name("telephone")
        self.password = self.driver.find_element_by_name("password")
        self.confirm = self.driver.find_element_by_name("confirm")
        self.newsletter = self.driver.find_element_by_name("newsletter")
        self.checkbox = self.driver.find_element_by_name("agree")
        self.continue_ = self.driver.find_element_by_xpath("//*[@id='content']/form/div/div/input[2]")

    def test_open_registration_page(self):
        self.assertEqual("Register Account", self.driver.title)

    @unittest.skip
    def test_register_given_new_and_correct_credentials_expect_pass(self):
        self.firstname.send_keys("John")
        self.lastname.send_keys("Doe")
        self.email.send_keys("john.doe123@test.com")
        self.telephone.send_keys("60123456789")
        self.password.send_keys("123456")
        self.confirm.send_keys("123456")
        self.newsletter.click()
        self.checkbox.click()
        self.continue_.click()


    def test_register_given_registered_email_expect_fail(self):
        self.firstname.send_keys("John")
        self.lastname.send_keys("Doe")
        self.email.send_keys("john.doe123@test.com")
        self.telephone.send_keys("60123456789")
        self.password.send_keys("123456")
        self.confirm.send_keys("123456")
        self.newsletter.click()
        self.checkbox.click()
        self.continue_.click()  

        try:
            alert = self.driver.find_element_by_xpath("//*[@id='account-register']/div[1]")
            alert_message = alert.text
            self.assertIsNotNone(alert)
            self.assertEqual("Warning: E-Mail Address is already registered!", alert_message)
            #print(inspect.currentframe().f_code.co_name)
        except:
            raise Exception("Expecting alert 'Warning: E-Mail Address is already registered!'")

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()