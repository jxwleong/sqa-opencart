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

        # Must be in the product page
        self.product_quantity = "//*[@id='input-quantity']"


        # Must be in shopping cart page
        self.shopping_cart_first_product_quantity_xpath = "//*[@id='content']/form/div/table/tbody/tr/td[4]/div/input"
   
    def test_add_cart_with_default_quantity_one(self):
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

        # Assume only one product which is HP LP3065 at shopping cart!
        shopping_cart_first_product_quantity = self.driver.find_element_by_xpath(self.shopping_cart_first_product_quantity_xpath).get_attribute("value")
        self.assertEqual("1", shopping_cart_first_product_quantity)


    def test_add_cart_with_quantity_of_ten(self):
        new_quantity = 10
        url = self.all_laptops_page.get_attribute("href")
        self.driver.get(url)
        self.assertEqual(self.driver.title, "Laptops & Notebooks")

        # Need to be in all laptop and notebook page first
        self.hp_lp3065_url = self.driver.find_element_by_xpath(self.hp_lp3065_url_xpath).get_attribute("href")
        self.driver.get(self.hp_lp3065_url)
        
        # Change the quantity
        product_quantity_element = self.driver.find_element_by_xpath(self.product_quantity)
        product_quantity_element.clear()  # Remove current quantity..
        product_quantity_element.send_keys(new_quantity)

        self.add_to_cart_button = self.driver.find_element_by_xpath(self.add_to_cart_button_xpath)
        self.add_to_cart_button.click()   # Add to cart.

        self.driver.get(self.shopping_cart_url)
        # Need to be in shopping cart first to extract this data
        self.shopping_cart_hp_lp3065 = self.driver.find_element_by_xpath(self.shopping_cart_hp_lp3065_xpath)

        text = self.shopping_cart_hp_lp3065.text
        self.assertEqual(text, "HP LP3065")

        # Assume only one product which is HP LP3065 at shopping cart!
        shopping_cart_first_product_quantity = self.driver.find_element_by_xpath(self.shopping_cart_first_product_quantity_xpath).get_attribute("value")
        self.assertEqual("10", shopping_cart_first_product_quantity)

    def tearDown(self):
        self.driver.close()

#driver.close()
if __name__ == "__main__":
    unittest.main()