from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    link = "https://suninjuly.github.io/get_attribute.html"
    browser.get(link)

    inp_valuex = browser.find_element(By.ID, "treasure")
    x = inp_valuex.get_attribute("valuex")
    print(x)
    y = calc(x)
    print(y)
    print(x)

    answer = browser.find_element(By.ID, "answer")
    answer.send_keys(str(y))

    option1 = browser.find_element(By.ID, "robotCheckbox")
    option1.click()

    option2 = browser.find_element(By.ID, "robotsRule")
    option2.click()

    button = browser.find_element(By.CSS_SELECTOR, "button")
    button.click()

finally:
    # успеваем скопировать код за 3 секунды
    time.sleep(3)
    # закрываем браузер после всех манипуляций
    browser.quit()


