from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time

link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)

find_name = browser.find_element(By.NAME, 'firstname')
find_name.send_keys('Alex')

find_second_name = browser.find_element(By.NAME, 'lastname')
find_second_name.send_keys('Berlizov')

find_mail = browser.find_element(By.NAME, 'email')
find_mail.send_keys('rock@gmail.com')

current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'file.txt')
find_file = browser.find_element(By.ID, 'file')
find_file.send_keys(file_path)

find_submit = browser.find_element(By.CSS_SELECTOR, 'button.btn')
find_submit.click()

time.sleep(10)
browser.quit()