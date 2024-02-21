from selenium import webdriver
import math

from selenium.webdriver.common.by import By


link = "https://SunInJuly.github.io/execute_script.html"
browser = webdriver.Chrome()
browser.get(link)

x_element = browser.find_element("id", "input_value")
x = int(x_element.text)

result = math.log(abs(12*math.sin(x)))

browser.execute_script("window.scrollBy(0, 100);")

input = browser.find_element(By.ID, "answer")
input.send_keys(str(result))

option = browser.find_element(By.XPATH, "//input[@id='robotCheckbox']")
option.click()

option = browser.find_element(By.XPATH, "//input[@id='robotsRule']")
option.click()

button = browser.find_element(By.XPATH, "//button[@type='submit']")
button.click()

import time
time.sleep(3)
browser.quit()

