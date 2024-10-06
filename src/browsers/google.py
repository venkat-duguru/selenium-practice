from selenium import webdriver
driver = webdriver.Edge()
driver.get("https://google.com")
assert driver.current_url == "https://www.google.com/"
