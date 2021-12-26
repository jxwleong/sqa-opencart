from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoAlertPresentException

import inspect
import unittest
import time

# Constant variable
compare_product_page_url = "https://demo.opencart.com/index.php?route=product/compare"
product_1_url = "https://demo.opencart.com/index.php?route=product/product&path=18&product_id=47"
product_2_url = "https://demo.opencart.com/index.php?route=product/product&path=18&product_id=44"
#driver = webdriver.Chrome(executable_path="chromedriver.exe")
#driver.get(homepage_url)


class TestCart(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="chromedriver.exe")
        self.driver.implicitly_wait(5) # seconds, Ref: https://selenium-python.readthedocs.io/waits.html#implicit-waits

        self.shopping_cart_url = "https://demo.opencart.com/index.php?route=checkout/cart"

        # Must be in the product page
        self.add_to_compare_button_xpath = "//*[@id='content']/div/div[2]/div[1]/button[2]"
        self.add_to_cart_button_xpath = "//*[@id='button-cart']"
                

        # Must be in compare page
        self.product1_name_in_compare_page_xpath = "//*[@id='content']/table/tbody[1]/tr[1]/td[2]/a/strong"
        self.product2_name_in_compare_page_xpath = "//*[@id='content']/table/tbody[1]/tr[1]/td[3]/a/strong"

        # Must be in compare page and must have 2 product
        self.remove_product2_in_compare_page_xpath = "//*[@id='content']/table/tbody[2]/tr/td[3]/a"
    
        # Must be in shopping cart page
        self.shopping_cart_hp_lp3065_xpath = "//*[@id='content']/form/div/table/tbody/tr/td[2]/a"

    def test_add_2_product_then_add_product1_to_cart(self):
        # Add product 1 to compare
        self.driver.get(product_1_url)
        self.assertEqual(self.driver.title, "HP LP3065")
        
        add_to_compare_button = self.driver.find_element_by_xpath(self.add_to_compare_button_xpath)
        add_to_compare_button.click()

        time.sleep(1)  # Some delay to really ensure it really added before switch page
        
        # Add product 2 to compare
        self.driver.get(product_2_url)
        self.assertEqual(self.driver.title, "MacBook Air")
        
        add_to_compare_button = self.driver.find_element_by_xpath(self.add_to_compare_button_xpath)
        add_to_compare_button.click()

        time.sleep(1)

        # Goto compare page
        self.driver.get(compare_product_page_url)
        self.assertEqual(self.driver.title, "Product Comparison")
         
        add_to_cart_product1_button = self.driver.find_element_by_xpath("//*[@id='content']/table/tbody[4]/tr/td[2]/input")
        add_to_cart_product1_button.click()
        
        time.sleep(1)
        
        # It will redirect me to the product page...
        self.add_to_cart_button = self.driver.find_element_by_xpath(self.add_to_cart_button_xpath)
        self.add_to_cart_button.click()   # Add to cart.
        self.driver.get(self.shopping_cart_url)

        self.assertEqual(self.driver.title, "Shopping Cart")

        self.shopping_cart_hp_lp3065 = self.driver.find_element_by_xpath(self.shopping_cart_hp_lp3065_xpath)

        text = self.shopping_cart_hp_lp3065.text
        self.assertEqual(text, "HP LP3065")
        
    #@unittest.skip
    def test_add_to_compare_for_two_product(self):
        # Add product 1 to compare
        self.driver.get(product_1_url)
        self.assertEqual(self.driver.title, "HP LP3065")
        
        add_to_compare_button = self.driver.find_element_by_xpath(self.add_to_compare_button_xpath)
        add_to_compare_button.click()

        time.sleep(1)  # Some delay to really ensure it really added before switch page
        
        # Add product 2 to compare
        self.driver.get(product_2_url)
        self.assertEqual(self.driver.title, "MacBook Air")
        
        add_to_compare_button = self.driver.find_element_by_xpath(self.add_to_compare_button_xpath)
        add_to_compare_button.click()

        time.sleep(1)

        # Goto compare page
        self.driver.get(compare_product_page_url)
        self.assertEqual(self.driver.title, "Product Comparison")

        # Check whether both product are in the product comparison page
        try:
            product1_comparison_page_header = self.driver.find_element_by_xpath(self.product1_name_in_compare_page_xpath)
            product2_comparison_page_header = self.driver.find_element_by_xpath(self.product2_name_in_compare_page_xpath)
        except:
            raise Exception("Expect both 'HP LP3065' and 'MacBook Air' are in the comparion page, seems like it's missing..")
 
        # If we make it here, means pass!
        self.assertEqual("HP LP3065", product1_comparison_page_header.text)
        self.assertEqual("MacBook Air", product2_comparison_page_header.text)

    #@unittest.skip
    def test_add_to_compare_for_two_product_but_remove_product2(self):
        # Assume the adding multiple product to compare part is done
        # This test method just remove the product2 (MacBook Air)
        # Add product 1 to compare
        self.driver.get(product_1_url)
        self.assertEqual(self.driver.title, "HP LP3065")
        
        add_to_compare_button = self.driver.find_element_by_xpath(self.add_to_compare_button_xpath)
        add_to_compare_button.click()

        time.sleep(1)  # Some delay to really ensure it really added before switch page
        
        # Add product 2 to compare
        self.driver.get(product_2_url)
        self.assertEqual(self.driver.title, "MacBook Air")
        
        add_to_compare_button = self.driver.find_element_by_xpath(self.add_to_compare_button_xpath)
        add_to_compare_button.click()

        time.sleep(1)

        # Goto compare page
        self.driver.get(compare_product_page_url)
        self.assertEqual(self.driver.title, "Product Comparison")
        

        # Remove product2

        remove_product2_url = self.driver.find_element_by_xpath("//*[@id='content']/table/tbody[4]/tr/td[3]/a").get_attribute("href")
        self.driver.get(remove_product2_url)

        # Check whether both product are in the product comparison page
        try:
            product2_comparison_page_header = self.driver.find_element_by_xpath(self.product2_name_in_compare_page_xpath)
        except:
            return

        raise Exception("Expect can't find product2 (MacBook Air) in the compare page, looks like it's there :P")

    def tearDown(self):
        self.driver.close()

#driver.close()
if __name__ == "__main__":
    unittest.main()