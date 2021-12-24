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
#driver = webdriver.Chrome(executable_path="chromedriver.exe")
#driver.get(homepage_url)


class TestCart(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="chromedriver.exe")
        self.driver.get(homepage_url)

        self.shopping_cart_url = self.driver.find_element_by_xpath("//*[@id='top-links']/ul/li[4]/a").get_attribute("href")
        self.all_laptops_page = self.driver.find_element_by_xpath("//*[@id='menu']/div[2]/ul/li[2]/div/a")
        self.hp_lp3065_url_xpath = "//*[@id='content']/div[4]/div[1]/div/div[2]/div[1]/h4/a"
        self.add_to_cart_button_xpath = "//*[@id='button-cart']"
        self.shopping_cart_hp_lp3065_xpath = "//*[@id='content']/form/div/table/tbody/tr/td[2]/a"

    def test_add_cart(self):
        url = self.all_laptops_page.get_attribute("href")
        self.driver.get(url)
        self.assertEqual(self.driver.title, "Laptops & Notebooks")

        # Need to be in all laptop and notebook page first
        self.hp_lp3065_url = self.driver.find_element_by_xpath(self.hp_lp3065_url_xpath).get_attribute("href")
        self.driver.get(self.hp_lp3065_url)
        
        self.add_to_cart_button = self.driver.find_element_by_xpath(self.add_to_cart_button_xpath)
        self.add_to_cart_button.click()   # Add to cart.

        self.driver.get(self.shopping_cart_url)
        # Need to be in shopping cart first to extract this data
        self.shopping_cart_hp_lp3065 = self.driver.find_element_by_xpath(self.shopping_cart_hp_lp3065_xpath)

        text = self.shopping_cart_hp_lp3065.text
        self.assertEqual(text, "HP LP3065")


    def tearDown(self):
        self.driver.close()

#driver.close()
if __name__ == "__main__":
    unittest.main()