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


class TestWishlist(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="chromedriver.exe")
        self.driver.get(homepage_url)

        self.wishlist_url = self.driver.find_element_by_xpath("//*[@id='wishlist-total']").get_attribute("href")
        self.all_laptops_page_url = self.driver.find_element_by_xpath("//*[@id='menu']/div[2]/ul/li[2]/div/a").get_attribute("href")
        self.hp_lp3065_url_xpath = "//*[@id='content']/div[4]/div[1]/div/div[2]/div[1]/h4/a"
        self.add_to_wishlist_xpath = "//*[@id='content']/div/div[2]/div[1]/button[1]"
        self.wishlist_hp_lp3065_xpath = "//*[@id='content']/div[1]/table/tbody/tr/td[2]/a"

        self.login_url = self.driver.find_element_by_xpath("//*[@id='top-links']/ul/li[2]/ul/li[2]/a").get_attribute("href")
        self.email_element_name = "email"
        self.passoword_element_name = "password"
        self.login_button_xpath = "//*[@id='content']/div/div[2]/div/form/input[1]"

    def login(self):
        self.driver.get(self.login_url)
        self.email = self.driver.find_element_by_name(self.email_element_name )
        self.password = self.driver.find_element_by_name(self.passoword_element_name)
        self.login = self.driver.find_element_by_xpath(self.login_button_xpath)
        self.email.send_keys("john.doe123@test.com")
        self.password.send_keys("123456")
        self.login.click()

    def test_add_to_wishlist(self):
        self.login()
        self.driver.get(self.all_laptops_page_url)
        self.assertEqual(self.driver.title, "Laptops & Notebooks")

        # Need to be in all laptop and notebook page first
        self.hp_lp3065_url = self.driver.find_element_by_xpath(self.hp_lp3065_url_xpath).get_attribute("href")
        self.driver.get(self.hp_lp3065_url)
        
        self.add_to_wishlist_button = self.driver.find_element_by_xpath(self.add_to_wishlist_xpath)
        self.add_to_wishlist_button.click()   # Add to cart.

        self.driver.get(self.wishlist_url)

        time.sleep(2)
        # Need to be in wishlist first to extract this data
        self.wishlist_hp_lp3065 = self.driver.find_element_by_xpath(self.wishlist_hp_lp3065_xpath)

        text = self.wishlist_hp_lp3065.text
        self.assertEqual(text, "HP LP3065")


    def tearDown(self):
        self.driver.close()

#driver.close()
if __name__ == "__main__":
    unittest.main()