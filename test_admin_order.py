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



class TestOrder(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="chromedriver.exe")
        self.driver.get(admin_login_page_url)

        self.username = self.driver.find_element_by_name("username")
        self.password = self.driver.find_element_by_name("password")
        self.login = self.driver.find_element_by_xpath("//*[@id='content']/div/div/div/div/div[2]/form/div[3]/button")

        # Must be in Dashboard page to get the element
        self.total_orders_url_xpath = "//*[@id='content']/div[2]/div[1]/div[1]/div/div[3]/a"

        # Must be in Order page
        self.latest_order_id_xpath = "//*[@id='form-order']/table/tbody/tr[1]/td[2]"


    def test_read_latest_order_it_expect_14530(self):
        self.login.click()
        
        order_page_url = self.driver.find_element_by_xpath(self.total_orders_url_xpath).get_attribute("href")
        self.driver.get(order_page_url)
        self.assertEqual("Orders", self.driver.title)

        latest_order_id = self.driver.find_element_by_xpath(self.latest_order_id_xpath).text
        self.assertEqual("14530", latest_order_id)

if __name__ == "__main__":
    unittest.main()