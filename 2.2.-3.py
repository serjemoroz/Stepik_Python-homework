from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

try:
    # Открываем страницу
    link = "https://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    time.sleep(3)

    # Находим числа на странице
    num1_element = browser.find_element(By.ID, "num1")
    num2_element = browser.find_element(By.ID, "num2")

    # Получаем текст чисел
    num1 = int(num1_element.text)
    num2 = int(num2_element.text)

    # Считаем сумму чисел
    sum_result = num1 + num2

    # Выбираем значение в выпадающем списке равное сумме
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(sum_result))

    # Нажимаем кнопку "Submit"
    submit_button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    submit_button.click()

finally:
    # Ждем некоторое время и закрываем браузер
    time.sleep(5)
    browser.quit()
