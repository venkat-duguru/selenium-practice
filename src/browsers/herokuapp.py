import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get("https://katalon-demo-cura.herokuapp.com/")
driver.find_element(By.ID, "btn-make-appointment")
assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/"
driver.quit()




