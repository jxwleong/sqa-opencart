from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support.ui import Select

import inspect
import unittest
import time

# Constant variable
homepage_url = "https://demo.opencart.com/index.php"

class TestCheckout(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="chromedriver.exe")
        self.driver.implicitly_wait(20) # https://stackoverflow.com/a/27113068 solved element unable locate issue
        self.driver.get(homepage_url)

        self.hp_lp3065_url = "https://demo.opencart.com/index.php?route=product/product&path=18&product_id=47"
        self.macbook_url = "https://demo.opencart.com/index.php?route=product/product&product_id=43"
        self.macbook_checkout_image_xpath = "//*[@id='content']/form/div/table/tbody/tr[1]/td[1]/a/img"
        self.remove_macbook_button_xpath = "//*[@id='content']/form/div/table/tbody/tr[1]/td[4]/div/span/button[2]"
        self.first_product_name_xpath = "//*[@id='content']/form/div/table/tbody/tr[1]/td[2]/a"
        self.shopping_cart_url = self.driver.find_element_by_xpath("//*[@id='top-links']/ul/li[4]/a").get_attribute("href")
        self.all_laptops_page = self.driver.find_element_by_xpath("//*[@id='menu']/div[2]/ul/li[2]/div/a")
        self.add_to_cart_button_xpath = "//*[@id='button-cart']"
        self.checkout_button_xpath = "//*[@id='content']/div[3]/div[2]/a"
        self.alert_message_xpath = "//*[@id='checkout-cart']/div[1]"


        self.login_url = self.driver.find_element_by_xpath("//*[@id='top-links']/ul/li[2]/ul/li[2]/a").get_attribute("href")
        self.email_element_name = "email"
        self.passoword_element_name = "password"
        self.login_button_xpath = "//*[@id='content']/div/div[2]/div/form/input[1]"

        self.checkout_step2_continue_xpath = "//*[@id='button-payment-address']"
        self.checkout_step3_continue_xpath = "//*[@id='button-shipping-address']"
        self.checkout_step4_continue_xpath = "//*[@id='button-shipping-method']"
        self.checkout_step5_checkbox_xpath = "//*[@id='collapse-payment-method']/div/div[2]/div/input[1]"
        self.checkout_step5_continue_xpath = "//*[@id='button-payment-method']"
        self.checkout_step6_confirm_order_xpath = "//*[@id='button-confirm']"

    def login(self):
        self.driver.get(self.login_url)
        self.email = self.driver.find_element_by_name(self.email_element_name )
        self.password = self.driver.find_element_by_name(self.passoword_element_name)
        self.login = self.driver.find_element_by_xpath(self.login_button_xpath)
        self.email.send_keys("john.doe123@test.com")
        self.password.send_keys("123456")
        self.login.click()

    def checkout_fill_billing_details(self):
        self.firstname = self.driver.find_element_by_name("firstname")
        self.lastname = self.driver.find_element_by_name("lastname")
        self.address_1 = self.driver.find_element_by_name("address_1")
        self.city = self.driver.find_element_by_name("city")
        self.postcode = self.driver.find_element_by_name("postcodde")
        # Drop down reference: https://stackoverflow.com/a/59145705
        self.country_select = Select(self.driver.find_element_by_xpath("//*[@id='input-payment-country']"))
        self.region_select = Select(self.driver.find_element_by_xpath("//*[@id='input-payment-zone']"))

        self.firstname.send_keys("Foo")
        self.lastname.send_keys("ya")
        self.address_1.send_keys("Noland")
        self.city.send_keys("Nowhere")
        self.postcode.send_keys("99999")
        self.country_select.select_by_index(1)
        self.region_select.select_by_index(1)

    #@unittest.skip
    def test_checkout_invalid_item_expect_error_message(self):
        self.login()

        self.driver.get(self.macbook_url)
        self.assertEqual(self.driver.title, "MacBook")

        
        self.add_to_cart_button = self.driver.find_element_by_xpath(self.add_to_cart_button_xpath)
        self.add_to_cart_button.click()   # Add to cart.

        self.driver.get(self.shopping_cart_url)

        self.checkout_button_url = self.driver.find_element_by_xpath(self.checkout_button_xpath).get_attribute("href")
        self.driver.get(self.checkout_button_url)

        try:
            alert = self.driver.find_element_by_xpath(self.alert_message_xpath)
            alert_message = alert.text[:-2] # Remove the "\nx" character to get the pure string for assertion later
            self.assertIsNotNone(alert)
            self.assertEqual("Products marked with *** are not available in the desired quantity or not in stock!", alert_message)
        except:
            raise Exception("Expecting message 'Products marked with *** are not available in the desired quantity or not in stock!' ")

    def test_checkout_valid_item_expect_pass(self):
        self.login()
        
        self.driver.get(self.hp_lp3065_url)
        self.assertEqual(self.driver.title, "HP LP3065")

        
        self.add_to_cart_button = self.driver.find_element_by_xpath(self.add_to_cart_button_xpath)
        self.add_to_cart_button.click()   # Add to cart.

        self.driver.get(self.shopping_cart_url)
        try:  
            first_product = self.driver.find_element_by_xpath(self.first_product_name_xpath)
            if first_product.text == "MacBook":
                self.driver.find_element_by_xpath(self.macbook_checkout_image_xpath)
                remove_button = self.driver.find_element_by_xpath(self.remove_macbook_button_xpath)
                remove_button.click()
        except:  # pass, no invalid item in the shopping cart
            pass
        
        time.sleep(2)  # Need this else wont checkout..
        self.checkout_button_url = self.driver.find_element_by_xpath(self.checkout_button_xpath).get_attribute("href")
        self.driver.get(self.checkout_button_url)
        #time.sleep(5)
        #self.checkout_fill_billing_details() SKip because already set for the account login
        continue_ = self.driver.find_element_by_xpath(self.checkout_step2_continue_xpath)
        continue_.click()
        time.sleep(1) 
        continue_ = self.driver.find_element_by_xpath(self.checkout_step3_continue_xpath)
        continue_.click()
        time.sleep(1) 
        continue_ = self.driver.find_element_by_xpath(self.checkout_step4_continue_xpath)
        continue_.click()
        time.sleep(1) 
        checkbox = self.driver.find_element_by_xpath(self.checkout_step5_checkbox_xpath)
        checkbox.click()
        time.sleep(1) 
        continue_ = self.driver.find_element_by_xpath(self.checkout_step5_continue_xpath)
        continue_.click()
        time.sleep(1) 
        confirm = self.driver.find_element_by_xpath(self.checkout_step6_confirm_order_xpath)
        confirm.click()
        time.sleep(5) # Delay needed for the final page to be fully loaded
        self.assertEqual(self.driver.title, "Your order has been placed!")

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()