from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoAlertPresentException

import inspect
import unittest
import time

# Constant variable
login_page_url = "https://demo.opencart.com/index.php?route=account/login"



class TestLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="chromedriver.exe")
        self.driver.get(login_page_url)

        self.email = self.driver.find_element_by_name("email")
        self.password = self.driver.find_element_by_name("password")
        self.login = self.driver.find_element_by_xpath("//*[@id='content']/div/div[2]/div/form/input[1]")


    def test_open_login_page(self):
        self.assertEqual("Account Login", self.driver.title)

    def test_login_given_wrong_email_and_password_expect_fail(self):
        self.email.send_keys("fake.account@test.com")
        self.password.send_keys("fakepass")

        self.login.click()

        try:
            alert = self.driver.find_element_by_xpath("//*[@id='account-login']/div[1]")
            alert_message = alert.text
            self.assertIsNotNone(alert)
            self.assertEqual("Warning: No match for E-Mail Address and/or Password.", alert_message)
            #print(inspect.currentframe().f_code.co_name)
        except:
            raise Exception("Expecting alert 'Warning: No match for E-Mail Address and/or Password.'")

    def test_login_given_correct_email_wrong_password_expect_fail(self):
        self.email.send_keys("john.doe123@test.com")
        self.password.send_keys("fakepass")

        self.login.click()

        try:
            alert = self.driver.find_element_by_xpath("//*[@id='account-login']/div[1]")
            alert_message = alert.text
            self.assertIsNotNone(alert)
            self.assertEqual("Warning: No match for E-Mail Address and/or Password.", alert_message)
            #print(inspect.currentframe().f_code.co_name)
        except:
            raise Exception("Expecting alert 'Warning: No match for E-Mail Address and/or Password.'")

    def test_login_given_wrong_email_correct_password_expect_fail(self):
        self.email.send_keys("fake.account@test.com")
        self.password.send_keys("123456")

        self.login.click()

        try:
            alert = self.driver.find_element_by_xpath("//*[@id='account-login']/div[1]")
            alert_message = alert.text
            self.assertIsNotNone(alert)
            self.assertEqual("Warning: No match for E-Mail Address and/or Password.", alert_message)
            #print(inspect.currentframe().f_code.co_name)
        except:
            raise Exception("Expecting alert 'Warning: No match for E-Mail Address and/or Password.'")
            
    def test_register_given_correct_email_and_password_expect_pass(self):
        self.email.send_keys("john.doe123@test.com")
        self.password.send_keys("123456")

        self.login.click()

        self.assertEqual("My Account", self.driver.title)


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()