from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

def num(y):
    return str(math.log(abs(12*math.sin(int(y)))))


browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/explicit_wait2.html')

WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, 'price'), '100'))
find_button_book = browser.find_element(By.ID, 'book')
find_button_book.click()

find_x = browser.find_element(By.ID, 'input_value')
x = int(find_x.text)

find_answer = browser.find_element(By.ID, 'answer')
find_answer.send_keys(num(x))

find_button_submit = browser.find_element(By.ID, 'solve')
find_button_submit.click()

time.sleep(20)
browser.quit()

