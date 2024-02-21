import confirm
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time
import math



def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    link = "https://suninjuly.github.io/redirect_accept.html"
    browser.get(link)

    button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    button.click()

    time.sleep(2)

    new_window = browser.window_handles[1]  # получили массив имен вкладок
    browser.switch_to.window(new_window)

    number_x = browser.find_element(By.ID, "input_value").text
    answer_input = browser.find_element(By.ID, "answer")
    answer_input.send_keys(calc(number_x))

    button = browser.find_element(By.XPATH, "//button[@type='submit']")
    button.click()

finally:
    time.sleep(4)
    browser.quit()