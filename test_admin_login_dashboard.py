"""
Seems like no matter what username and password used, it's able to login
to the system

Test login and view total orders, total sales and total customers.
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



class TestAdminLoginDashboard(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="chromedriver.exe")
        self.driver.get(admin_login_page_url)

        self.username = self.driver.find_element_by_name("username")
        self.password = self.driver.find_element_by_name("password")
        self.login = self.driver.find_element_by_xpath("//*[@id='content']/div/div/div/div/div[2]/form/div[3]/button")

        # Must be in Dashboard page to get the element
        self.total_orders_url_xpath = "//*[@id='content']/div[2]/div[1]/div[1]/div/div[3]/a"
        self.total_orders_number_xpath = "//*[@id='content']/div[2]/div[1]/div[1]/div/div[2]/h2"
        self.total_sales_url_xpath = "//*[@id='content']/div[2]/div[1]/div[2]/div/div[3]/a"
        self.total_sales_number_xpath = "//*[@id='content']/div[2]/div[1]/div[2]/div/div[2]/h2"
        self.total_customers_url_xpath = "//*[@id='content']/div[2]/div[1]/div[3]/div/div[3]/a"
        self.total_customers_number_xpath = "//*[@id='content']/div[2]/div[1]/div[3]/div/div[2]/h2"

    def test_open_login_page(self):
        self.assertEqual("Administration", self.driver.title)

    def test_login(self):
        self.login.click()

        self.assertEqual("Dashboard", self.driver.title)

    def test_read_total_orders_expect_11dot1_K(self):
        self.login.click()
        total_orders = self.driver.find_element_by_xpath(self.total_orders_number_xpath).text
        self.assertEqual("11.1K", total_orders)


    def test_read_total_sales_expect_11dot4_M(self):
        self.login.click()
        total_sales = self.driver.find_element_by_xpath(self.total_sales_number_xpath).text
        self.assertEqual("11.4M", total_sales)


    def test_read_total_customers_expect_134dot6_K(self):
        self.login.click()
        total_customers = self.driver.find_element_by_xpath(self.total_customers_number_xpath).text
        self.assertEqual("134.6K", total_customers)


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()