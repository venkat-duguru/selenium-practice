import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument("--page-load-strategy=eager")
driver = webdriver.Chrome(chrome_options)
driver.get("https://app.vwo.com")
driver.maximize_window()
time.sleep(5)
