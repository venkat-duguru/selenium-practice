import time
from selenium import webdriver
#driver = webdriver.Chrome

def test_vwo_login():
    driver = webdriver.Chrome

    print(driver.session_id)
    driver.get("https://app.vwo.com/#/login")
    print(driver.title)
    assert driver.title == "Login - VWO"
time.sleep(2)