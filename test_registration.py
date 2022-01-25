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

        # Error message element xpath
        self.firstname_error = "//*[@id='account']/div[2]/div/div"
        self.lastname_error = "//*[@id='account']/div[3]/div/div"
        self.email_error = "//*[@id='account']/div[4]/div/div"
        self.telephone_error = "//*[@id='account']/div[5]/div/div"
        self.password_error = "//*[@id='content']/form/fieldset[2]/div[1]/div/div"
        self.password_confirm_error = "//*[@id='content']/form/fieldset[2]/div[2]/div/div"

        self.checkbox_error = "//*[@id='account-register']/div[1]"
        self.registered_email_error = "//*[@id='account-register']/div[1]"

    def test_open_registration_page(self):
        self.assertEqual("Register Account", self.driver.title)

    #@unittest.skip  # Can't use same email everytime...
    def test_register_given_new_and_correct_credentials_expect_pass(self):
        self.firstname.send_keys("John")
        self.lastname.send_keys("Doe")
        self.email.send_keys("john.doe12312111@test.com")
        self.telephone.send_keys("60123456789")
        self.password.send_keys("123456")
        self.confirm.send_keys("123456")
        self.newsletter.click()
        self.checkbox.click()
        self.continue_.click()

        time.sleep(1)

        self.assertEqual("Your Account Has Been Created!", self.driver.title)

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
            alert = self.driver.find_element_by_xpath(self.registered_email_error)
            alert_message = alert.text
            self.assertIsNotNone(alert)
            self.assertEqual("Warning: E-Mail Address is already registered!", alert_message)
            #print(inspect.currentframe().f_code.co_name)
        except:
            raise Exception("Expecting alert 'Warning: E-Mail Address is already registered!'")

    def test_register_all_invalid_fields(self):
        # Blank and click conitnue
        # expect all error fields
        self.continue_.click()  

        try:
            self.driver.find_element_by_xpath(self.firstname_error)
            self.driver.find_element_by_xpath(self.lastname_error)
            self.driver.find_element_by_xpath(self.email_error)
            self.driver.find_element_by_xpath(self.telephone_error)
            self.driver.find_element_by_xpath(self.password_error)
        except:
            raise Exception("Some alert messages at registration page are missing..")

    # Just make the fields to be tested invalid..
    def test_register_invalid_firstname_lastname(self):
        self.firstname.send_keys("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        self.lastname.send_keys("bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb")
        self.continue_.click()  

        try:
            self.driver.find_element_by_xpath(self.firstname_error)
            self.driver.find_element_by_xpath(self.lastname_error)

        except:
            raise Exception("Some alert messages for first and last name at registration page are missing..")

    # Just make the fields to be tested invalid..
    def test_register_invalid_email(self):
        self.email.send_keys("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa@gmail.com")
        self.continue_.click()  

        try:
            self.driver.find_element_by_xpath(self.email_error)

        except:
            raise Exception("Some alert messages for email at registration page are missing..")

    # Just make the fields to be tested invalid..
    def test_register_invalid_telephone(self):
        self.telephone.send_keys("1")
        self.continue_.click()  

        try:
            self.driver.find_element_by_xpath(self.telephone_error)

        except:
            raise Exception("Some alert messages for telephone at registration page are missing..")


    # Just make the fields to be tested invalid..
    def test_register_invalid_password(self):
        self.password.send_keys("xx")
        self.continue_.click()  

        try:
            self.driver.find_element_by_xpath(self.password_error)

        except:
            raise Exception("Some alert messages for password at registration page are missing..")

    # Just make the fields to be tested invalid..
    def test_register_invalid_password_confirm(self):
        self.password.send_keys("12345")
        self.confirm.send_keys("12345678")
        self.continue_.click()  

        try:
            self.driver.find_element_by_xpath(self.password_confirm_error)

        except:
            raise Exception("Some alert messages for password confirm at registration page are missing..")

    def test_register_given_all_correct_field_but_didnt_check_agree_expect_fail(self):
        self.firstname.send_keys("John")
        self.lastname.send_keys("Doe")
        self.email.send_keys("john.doe123@test.com")
        self.telephone.send_keys("60123456789")
        self.password.send_keys("123456")
        self.confirm.send_keys("123456")
        self.newsletter.click()
        #self.checkbox.click()
        self.continue_.click()  

        try:
            alert = self.driver.find_element_by_xpath(self.checkbox_error)
            alert_message = alert.text
            self.assertIsNotNone(alert)
            self.assertEqual("Warning: You must agree to the Privacy Policy!", alert_message)
            #print(inspect.currentframe().f_code.co_name)
        except:
            raise Exception("Expecting alert 'Warning: You must agree to the Privacy Policy!'")

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()