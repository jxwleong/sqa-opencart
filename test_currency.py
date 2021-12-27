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
euro_symbol = "€"
pound_symbol = "£"
dollar_symbol = "$"


class TestCurrency(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="chromedriver.exe")
        self.driver.get(homepage_url)

        self.current_currency = self.driver.find_element_by_xpath("//*[@id='form-currency']/div/button/strong").text
        self.currency_dropdown = self.driver.find_element_by_xpath("//*[@id='form-currency']/div/button")
        self.euro = self.driver.find_element_by_xpath("//*[@id='form-currency']/div/ul/li[1]/button")
        self.pound = self.driver.find_element_by_xpath("//*[@id='form-currency']/div/ul/li[2]/button")
        self.dollar = self.driver.find_element_by_xpath("//*[@id='form-currency']/div/ul/li[3]/button")


    def test_open_homepage(self):
        self.assertEqual("Your Store", self.driver.title)

    def test_change_currency_to_euro(self):
        print(f"Current currency: {self.current_currency}")

        self.currency_dropdown.click()
        self.euro.click()

        updated_currency = self.driver.find_element_by_xpath("//*[@id='form-currency']/div/button/strong").text                   
        
        print(f"Updated current: {updated_currency}")
        self.assertEqual(euro_symbol, updated_currency)


    def test_change_currency_to_pound(self):
        print(f"Current currency: {self.current_currency}")
        self.currency_dropdown.click()
        self.pound.click()

        updated_currency = self.driver.find_element_by_xpath("//*[@id='form-currency']/div/button/strong").text                      
        
        print(f"Updated current: {updated_currency}")
        self.assertEqual(pound_symbol, updated_currency)

    def test_change_currency_to_dollar(self):
        print(f"Current currency: {self.current_currency}")
        self.currency_dropdown.click()
        self.dollar.click()

        updated_currency = self.driver.find_element_by_xpath("//*[@id='form-currency']/div/button/strong").text                      
        
        print(f"Updated current: {updated_currency}")
        self.assertEqual(dollar_symbol, updated_currency)


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()