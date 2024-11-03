from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://app.vwo.com/#/login")
driver.refresh()
