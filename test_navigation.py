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


class TestNavigation(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="chromedriver.exe")
        self.driver.get(homepage_url)
        # //*[@id='menu']/div[2]/ul/li[1]/div/a
        """
        global driver
        self.desktop_button = driver.find_element_by_xpath("//*[@id='menu']/div[2]/ul/li[1]/div/a")
        self.laptop_button = driver.find_element_by_xpath("//*[@id='menu']/div[2]/ul/li[2]/a")
        self.component_button = driver.find_element_by_xpath("//*[@id='menu']/div[2]/ul/li[3]/a")
        self.tablet_button = driver.find_element_by_xpath("//*[@id='menu']/div[2]/ul/li[4]/a")
        self.software_button = driver.find_element_by_xpath("//*[@id='menu']/div[2]/ul/li[5]/a")
        self.phones_button = driver.find_element_by_xpath("//*[@id='menu']/div[2]/ul/li[6]/a")
        self.camera_button = driver.find_element_by_xpath("//*[@id='menu']/div[2]/ul/li[7]/a")
        self.mp3_players_button = driver.find_element_by_xpath("//*[@id='menu']/div[2]/ul/li[8]/a")
        """
        self.shopping_cart_button = self.driver.find_element_by_xpath("//*[@id='top-links']/ul/li[4]/a")
        self.checkout_button = self.driver.find_element_by_xpath("//*[@id='top-links']/ul/li[5]/a")

        self.desktop_button = self.driver.find_element_by_xpath("//*[@id='menu']/div[2]/ul/li[1]/div/a")
        self.laptop_button = self.driver.find_element_by_xpath("//*[@id='menu']/div[2]/ul/li[2]/a")
        self.component_button = self.driver.find_element_by_xpath("//*[@id='menu']/div[2]/ul/li[3]/a")
        self.tablet_button = self.driver.find_element_by_xpath("//*[@id='menu']/div[2]/ul/li[4]/a")
        self.software_button = self.driver.find_element_by_xpath("//*[@id='menu']/div[2]/ul/li[5]/a")
        self.phones_button = self.driver.find_element_by_xpath("//*[@id='menu']/div[2]/ul/li[6]/a")
        self.camera_button = self.driver.find_element_by_xpath("//*[@id='menu']/div[2]/ul/li[7]/a")
        self.mp3_players_button = self.driver.find_element_by_xpath("//*[@id='menu']/div[2]/ul/li[8]/a")

        self.about_us = self.driver.find_element_by_xpath("/html/body/footer/div/div/div[1]/ul/li[1]/a")
        self.contact_us = self.driver.find_element_by_xpath("/html/body/footer/div/div/div[2]/ul/li[1]/a")
        self.brand = self.driver.find_element_by_xpath("/html/body/footer/div/div/div[3]/ul/li[1]/a")
        self.my_account = self.driver.find_element_by_xpath("/html/body/footer/div/div/div[4]/ul/li[1]/a")

    def test_shopping_cart(self):
        url = self.shopping_cart_button.get_attribute("href")
        self.driver.get(url)
        self.assertEqual(self.driver.title, "Shopping Cart")
    
    def test_checkout(self):
        # NOTE: Click on Checkout will lead to same page as shopping cart
        url = self.checkout_button.get_attribute("href")
        self.driver.get(url)
        self.assertEqual(self.driver.title, "Shopping Cart")

    def test_show_all_desktop(self):
        url = self.desktop_button.get_attribute("href")
        self.driver.get(url)
        self.assertEqual(self.driver.title, "Desktops")

    def test_show_all_laptops_and_notebooks(self):
        url = self.laptop_button.get_attribute("href")
        self.driver.get(url)
        self.assertEqual(self.driver.title, "Laptops & Notebooks")

    def test_show_all_components(self):
        url = self.component_button.get_attribute("href")
        self.driver.get(url)
        self.assertEqual(self.driver.title, "Components")

    def test_show_all_tablets(self):
        url = self.tablet_button.get_attribute("href")
        self.driver.get(url)
        self.assertEqual(self.driver.title, "Tablets")

    def test_show_all_software(self):
        url = self.software_button.get_attribute("href")
        self.driver.get(url)
        self.assertEqual(self.driver.title, "Software")

    def test_show_all_phones_and_pdas(self):
        url = self.phones_button.get_attribute("href")
        self.driver.get(url)
        self.assertEqual(self.driver.title, "Phones & PDAs")

    def test_show_all_cameras(self):
        url = self.camera_button.get_attribute("href")
        self.driver.get(url)
        self.assertEqual(self.driver.title, "Cameras")

    def test_show_all_mp3_players(self):
        url = self.mp3_players_button.get_attribute("href")
        self.driver.get(url)
        self.assertEqual(self.driver.title, "MP3 Players")

    def test_about_us(self):
        url = self.about_us.get_attribute("href")
        self.driver.get(url)
        self.assertEqual(self.driver.title, "About Us")

    def test_contact_us(self):
        url = self.contact_us.get_attribute("href")
        self.driver.get(url)
        self.assertEqual(self.driver.title, "Contact Us")

    def test_brands(self):
        url = self.brand.get_attribute("href")
        self.driver.get(url)
        self.assertEqual(self.driver.title, "Find Your Favorite Brand")

    def test_my_account(self):
        url = self.my_account.get_attribute("href")
        self.driver.get(url)
        self.assertEqual(self.driver.title, "Account Login")

    def tearDown(self):
        self.driver.close()

#driver.close()
if __name__ == "__main__":
    unittest.main()
    driver.quit()