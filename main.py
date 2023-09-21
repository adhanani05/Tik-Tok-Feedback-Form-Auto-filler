from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()

url = "https://www.tiktok.com/legal/report/feedback"
driver.get(url)

driver.implicitly_wait(20)

# Find input fields and fill them
email = driver.find_element(By.NAME, "email")
email.send_keys("your email")
print("Email Filled")

username = driver.find_element(By.NAME, "username")
username.send_keys("your username")
print("Username Filled")

text_area = driver.find_element(By.NAME, "feedback")
text_area.send_keys("My account @____ was mistakenly banned.")
print("Help us more filled")

# Find dropdowns and select an option
topic = driver.find_element(By.NAME, "option")
option_to_select = topic.find_element(By.XPATH, "//option[@value='TikTok Creator Fund']")
option_to_select.click()

tell_us_more = driver.find_element(By.NAME, "option2")
option_to_select2 = topic.find_element(By.XPATH, "//option[@value='Hacked or suspended account']")
option_to_select2.click()

# Find checkboxes and check them
checkbox = driver.find_elements(By.XPATH, "//span[@class='jsx-716101526']")[0].click()
checkbo1 = driver.find_elements(By.XPATH, "//span[@class='jsx-716101526']")[1].click()
print("Boxes Checked")

time.sleep(100)

#submit = driver.find_element(By.CLASS_NAME, "jsx-2335260363")
#submit.click()

print("Submitted")

driver.quit()


