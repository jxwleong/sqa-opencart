"""
Seems like no matter what username and password used, it's able to login
to the system

"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoAlertPresentException

import inspect
import unittest
import time

# Constant variable
admin_login_page_url = "https://demo.opencart.com/admin/"


class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="chromedriver.exe")
        self.driver.get(admin_login_page_url)

        self.username = self.driver.find_element_by_name("username")
        self.password = self.driver.find_element_by_name("password")
        self.login = self.driver.find_element_by_xpath("//*[@id='content']/div/div/div/div/div[2]/form/div[3]/button")

        # Must be in Dashboard page to get the element
        self.navigation_button_xpath = "//*[@id='header-logo']/a"
        self.customers_collapsable_button_xpath = "//*[@id='menu-customer']/a"
        self.customers_view_url_xpath = "//*[@id='collapse33']/li[1]/a"

        # Must be in customer page
        self.first_customer_name = "//*[@id='form-customer']/table/tbody/tr[1]/td[2]"
        self.first_customer_edit_button_xpath = "//*[@id='form-customer']/table/tbody/tr[1]/td[8]/div/a"

        # Must be in invidiual customer edit page
        self.customer_telephone_xpath = "//*[@id='input-telephone']"
        self.customer_edit_save_button_xpath = "//*[@id='content']/div[1]/div/div/button"


    def test_login_and_view_customers_then_chech_first_customer_name(self):
        self.login.click()
        self.assertEqual("Dashboard", self.driver.title)
        #navbar_button = self.driver.find_element_by_xpath("//*[@id='button-menu']")
        #navbar_button = self.driver.find_element_by_xpath("//*[@id='button-menu']/span")
        navbar_button = self.driver.find_element_by_xpath(self.navigation_button_xpath)
        navbar_button.click()
        
        customers_collapsable_button = self.driver.find_element_by_xpath(self.customers_collapsable_button_xpath)
        customers_collapsable_button.click()

        customers_view_url = self.driver.find_element_by_xpath(self.customers_view_url_xpath).get_attribute("href")

        self.driver.get(customers_view_url)
        self.assertEqual("Customers", self.driver.title)

        first_customer_name = self.driver.find_element_by_xpath(self.first_customer_name).text
        self.assertEqual("Md Kbds", first_customer_name)
    
    # No permission to modify...
    @unittest.skip
    def test_foo(self):
        new_telephone_number = "121111222222222222222"

        self.login.click()
        self.assertEqual("Dashboard", self.driver.title)

        navbar_button = self.driver.find_element_by_xpath(self.navigation_button_xpath)
        navbar_button.click()
        
        customers_collapsable_button = self.driver.find_element_by_xpath(self.customers_collapsable_button_xpath)
        customers_collapsable_button.click()

        customers_view_url = self.driver.find_element_by_xpath(self.customers_view_url_xpath).get_attribute("href")

        self.driver.get(customers_view_url)
        self.assertEqual("Customers", self.driver.title)

        first_customer_edit_button = self.driver.find_element_by_xpath(self.first_customer_edit_button_xpath)
        first_customer_edit_button.click()
        
        current_telephone_element = self.driver.find_element_by_xpath(self.customer_telephone_xpath)
        current_telephone = current_telephone_element.get_attribute("value")
        if current_telephone == new_telephone_number:
            new_telephone_number = current_telephone + "1"
            current_telephone_element.clear()
        current_telephone = current_telephone_element.get_attribute("value")
        current_telephone_element.send_keys(new_telephone_number)

        edit_save_button = self.driver.find_element_by_xpath(self.customer_edit_save_button_xpath)
        edit_save_button.click()


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()