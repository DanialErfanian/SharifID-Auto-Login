import os
from selenium import webdriver

username = "danial.erfanian"
password = "enter your password :)"

driver = webdriver.Chrome(os.path.dirname(os.path.abspath(__file__)) + "/chromedriver")

try:
    driver.get("https://net2.sharif.edu/login")
    driver.find_element_by_name("username").send_keys(username)
    driver.find_element_by_name("password").send_keys(password)
    driver.find_element_by_class_name("login100-form-btn").click()
except:
    pass
if driver is not None:
    driver.quit()
