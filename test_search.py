from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoAlertPresentException

import inspect
import unittest
import time

# Constant variable
homepage_url = "https://demo.opencart.com/index.php"



class TestSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="chromedriver.exe")
        self.driver.get(homepage_url)

        self.search_bar = self.driver.find_element_by_name("search")
        self.search_button = self.driver.find_element_by_xpath("//*[@id='search']/span/button")
        self.no_product_found = "//*[@id='content']/p[2]"

    def test_search_given_invalid_searchterm_expect_no_output(self):
        self.search_bar.send_keys("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!AAAAAAAAAAAAAAAAAAAAAAAAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB")
        self.search_button.click()

        try:
            search_output = self.driver.find_element_by_xpath(self.no_product_found)
            message = search_output.text
            self.assertIsNotNone(message)
            self.assertEqual("There is no product that matches the search criteria.", message)
            #print(inspect.currentframe().f_code.co_name)
        except:
            raise Exception("Expecting output 'There is no product that matches the search criteria.'")

    def test_search_apple_expected_output_apple_cinema_found(self):
        self.search_bar.send_keys("Apple")
        self.search_button.click()

        try:
            search_output = self.driver.find_element_by_xpath(self.no_product_found)
            #print(inspect.currentframe().f_code.co_name)
        except: # expect come here, just sanity check
            search_output = self.driver.find_element_by_xpath("//*[@id='content']/div[3]/div/div/div[2]/div[1]/h4/a")
            title = search_output.text
            self.assertIsNotNone(title)
            self.assertEqual('Apple Cinema 30"', title)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()