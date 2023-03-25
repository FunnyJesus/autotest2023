from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(f):
    return str(math.log(abs(12*math.sin(int(f)))))


link = "https://suninjuly.github.io/math.html"

browser = webdriver.Chrome()
browser.get(link)

x_element = browser.find_element(By.CSS_SELECTOR, 'span[id=input_value]')
x = x_element.text
y = calc(x)
input1 = browser.find_element(By.CSS_SELECTOR, "input[id=answer]")
input1.send_keys(calc(x))
    
check_box1 = browser.find_element(By.CSS_SELECTOR, "input[id=robotCheckbox]")
check_box1.click()

robot_rule = browser.find_element(By.ID, "robotsRule")
robot_rule.click()

submit_click = browser.find_element(By.CSS_SELECTOR, "button.btn")
submit_click.click()


time.sleep(10)
browser.quit()
