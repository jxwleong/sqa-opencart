from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time

# Assume the chromedriver.exe haveing the same directory as this file..
driver = webdriver.Chrome(executable_path="chromedriver.exe")
#driver.get(url="https://demo.opencart.com/")
driver.get("https://www.opencart.com/index.php?route=account/register")
print("get")
print(driver.title)
#time.sleep(10)


# Register
# url: https://www.opencart.com/index.php?route=account/register
username = driver.find_element_by_name("username")
username.send_keys("username")
firstname = driver.find_element_by_name("firstname")
firstname.send_keys("firstname")
lastname = driver.find_element_by_name("lastname")
lastname.send_keys("lastname")
email = driver.find_element_by_name("email")
email.send_keys("user@test.com")
# Select country dropdown box
# https://www.guru99.com/select-option-dropdown-selenium-webdriver.html
country = driver.find_element_by_name("country_id")
password = driver.find_element_by_name("password")
password.send_keys("abc123")

driver.find_element()

print("close")
driver.close()