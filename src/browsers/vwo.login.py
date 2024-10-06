import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get("https://app.vwo.com/#/login")
driver.find_element(By.ID, "this_id_doesnt_Exist")
time.sleep(2)

