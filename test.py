from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time

# Assume the chromedriver.exe haveing the same directory as this file..
driver = webdriver.Chrome(executable_path="chromedriver.exe")
driver.get(url="https://demo.opencart.com/")
print("get")
time.sleep(10)


# Register
# url: https://www.opencart.com/index.php?route=account/register
username = driver.find_element_by_name("username")
firstname = driver.find_element_by_name("firstname")
lastname = driver.find_element_by_name("lastname")
email = driver.find_element_by_name("email")
# Select country dropdown box
# https://www.guru99.com/select-option-dropdown-selenium-webdriver.html
country = driver.find_element_by_name("country_id")
password = driver.find_element_by_name("password")



print("close")
driver.close()