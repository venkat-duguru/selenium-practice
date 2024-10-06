import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--incognito")
driver = webdriver.Chrome(chrome_options)
driver.get("https://app.vwo.com")
time.sleep(10)
