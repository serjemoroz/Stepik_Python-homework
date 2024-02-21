from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest
import os
import math

class TestAbs(unittest.TestCase):
    def test_registration1(self):
        link = 'http://suninjuly.github.io/registration1.html'
        browser = webdriver.Chrome()
        browser.get(link)

        first_name_input = browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your first name']")
        first_name_input.send_keys("Vanya")

        last_name_input = browser.find_element(By.XPATH, "//input[@placeholder='Input your last name']")
        last_name_input.send_keys("First")

        Email_input = browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your email']")
        Email_input.send_keys("vanya@gmail.com")

        input1 = browser.find_element(By.XPATH, "//input[@placeholder='Input your phone:']")
        input1.send_keys("88005553535")

        input2 = browser.find_element(By.XPATH, "//input[@placeholder='Input your address:']")
        input2.send_keys("pushkina-kolotushkina")
        # Отправляем заполненную форму
        submit_button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
        submit_button.click()
        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(2)
        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text
        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        assert"Congratulations! You have successfully registered!" == welcome_text
        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(3)
        expected_welcome_text = "Congratulations! You have successfully registered!"
        self.assertEqual(welcome_text, expected_welcome_text, "Should be absolute value of a number")

    def test_registration2(self):
        link = "https://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        input1 = browser.find_element(By.NAME, "first_name")
        input1.send_keys("Ivan")
        input2 = browser.find_element(By.NAME, "last_name")
        input2.send_keys("Petrov")
        input3 = browser.find_element(By.CLASS_NAME, "city")
        input3.send_keys("Smolensk")
        input4 = browser.find_element(By.ID, "country")
        input4.send_keys("Russia")
        button = browser.find_element(By.XPATH, ('//button[@type="submit"]'))
        button.click()
        # успеваем скопировать код за 5 секунд
        time.sleep(5)
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h2")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text
        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        assert"Congratulations! You have successfully registered!" == welcome_text
        expected_welcome_text = "Congratulations! You have successfully registered!"
        self.assertEqual(welcome_text, expected_welcome_text, "NoSuchElementException")

if __name__ == "__main__":
    unittest.main()
