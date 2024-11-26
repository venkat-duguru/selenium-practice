import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://katalon-demo-cura.herokuapp.com/")
make_appointment_button = driver.find_element(By.XPATH, "//a[@='btn-make-appointment']")
make_appointment_button.click()
time.sleep(5)

