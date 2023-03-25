from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def num(y):
    return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/alert_accept.html')

find_button_journey = browser.find_element(By.CSS_SELECTOR, 'button.btn')
find_button_journey.click()

time.sleep(2)

alert = browser.switch_to.alert
alert.accept()

find_x = browser.find_element(By.ID, 'input_value')
x = int(find_x.text)

find_answer = browser.find_element(By.ID, 'answer')
find_answer.send_keys(num(x))

find_button_submit = browser.find_element(By.CSS_SELECTOR, 'button.btn')
find_button_submit.click()

time.sleep(20)
browser.quit()

