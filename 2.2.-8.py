import time

from selenium import webdriver
import os

from selenium.webdriver.common.by import By

try:
    # Создаем объект webdriver
    browser = webdriver.Chrome()

    # Открываем страницу
    browser.get("https://suninjuly.github.io/file_input.html")

    # Заполняем текстовые поля
    browser.find_element(By.XPATH,"//input[@placeholder='Enter first name']").send_keys("John")
    browser.find_element(By.XPATH,"//input[@placeholder='Enter last name']").send_keys("Smith")
    browser.find_element(By.XPATH, "//input[@placeholder='Enter email']").send_keys("john.doe@example.com")

    # Загружаем файл
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, "file.txt")
    browser.find_element(By.ID, "file").send_keys(file_path)

    # Нажимаем кнопку "Submit"
    browser.find_element(By.XPATH, "//button[@type='submit']").click()

finally:
    time.sleep(10)
    # Закрываем браузер после всех манипуляций
    browser.quit()
