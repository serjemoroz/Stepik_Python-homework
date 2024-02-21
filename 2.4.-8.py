import confirm
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    link = "https://suninjuly.github.io/explicit_wait2.html"
    browser.get(link)

    button = browser.find_element(By.ID, "book")
    WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID,"price"), "100"))
    button.click()

    time.sleep(2)

    number_x = browser.find_element(By.ID, "input_value").text
    answer_input = browser.find_element(By.ID, "answer")
    answer_input.send_keys(calc(number_x))

    button = browser.find_element(By.XPATH, "//button[@type='submit']")
    button.click()

finally:
    time.sleep(4)
    browser.quit()