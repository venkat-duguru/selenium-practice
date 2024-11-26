from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

# Set up the driver
driver = webdriver.Chrome()  # Make sure you have the ChromeDriver installed
driver.maximize_window()


# Navigate to the FitPeo Homepage
driver.get("https://www.fitpeo.com")  # Replace with the actual URL of the FitPeo homepage
time.sleep(2)

# Navigate to the Revenue Calculator Page
revenue_calculator_link = driver.find_element(By.LINK_TEXT, "Revenue Calculator")  # Adjust locator as needed
revenue_calculator_link.click()
time.sleep(2)

# Scroll Down to the Slider section
slider_section = driver.find_element(By.XPATH, "//span/input[@type='range']")  # Adjust locator as needed
driver.execute_script("arguments[0].scrollIntoView();", slider_section)
time.sleep(2)

# Adjust the Slider
slider = driver.find_element(By.XPATH, "//span[@data-index='0']")  # Adjust locator as needed
action = ActionChains(driver)

# Drag slider to the desired position
action.click_and_hold(slider).move_by_offset(200, 0).release().perform()  # Adjust offset to match "820"
time.sleep(2)
action.click_and_hold(slider).move_by_offset(-(105), 0).release().perform()
time.sleep(2)


# Verify the bottom text field value
bottom_text_field = driver.find_element(By.XPATH, "//input[@type='number']")  # Adjust locator as needed
value = bottom_text_field.get_attribute("value")  # Replace "value" with the correct attribute if needed

if value == "820":
    print("Test Passed: Slider adjusted to 820 successfully!")
else:
    print(f"Test Failed: Expected '820', but got '{value}'.")


text_field = driver.find_element(By.XPATH, "//input[@type='number']")

# to enter the value into the text field we have to clear the text inside the text field
actions = ActionChains(driver)
actions.click(text_field).key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).send_keys(Keys.BACKSPACE).perform()
time.sleep(2)

#to enter value into the text field
text_field.send_keys("560")
time.sleep(2)

checkbox_ids = ["CPT-99091", "CPT-99453", "CPT-99454", "CPT-99474"]  # Replace with actual IDs of the checkboxes
for checkbox_id in checkbox_ids:
    checkbox = driver.find_element(By.XPATH, "//input[@type='checkbox']")  # Adjust locator if needed
    if not checkbox.is_selected():
        checkbox.click()
time.sleep(2)

text_field = driver.find_element(By.XPATH, "//input[@type='number']")

# to enter the value into the text field we have to clear the text inside the text field
actions = ActionChains(driver)
actions.click(text_field).key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).send_keys(Keys.BACKSPACE).perform()
time.sleep(2)

#to enter value into the text field
text_field.send_keys("820")
time.sleep(2)

checkbox_ids = ["CPT-99091", "CPT-99453", "CPT-99454", "CPT-99474"]  # Replace with actual IDs of the checkboxes
for checkbox_id in checkbox_ids:
    checkbox = driver.find_element(By.XPATH, "//input[@type='checkbox']")  # Adjust locator if needed
    if not checkbox.is_selected():
        checkbox.click()
time.sleep(5)

#checking the total reimbursement is $110700
header_text = driver.find_element(By.CLASS_NAME, "MuiTypography-body1").text
print(header_text)

if header_text == "$110700":
    print(True)
else:
    print(False)

#closing the browser
driver.close()





