import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://app.vwo.com/#/login")
driver.find_element(By.ID, "login-username").send_keys("venkat.duguru@gmail.com")
driver.find_element(By.ID, "login-password").send_keys("Venkat@78")
