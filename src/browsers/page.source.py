import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options



driver = webdriver.Chrome()
driver.get("https://app.vwo.com")
print(driver.page_source)
