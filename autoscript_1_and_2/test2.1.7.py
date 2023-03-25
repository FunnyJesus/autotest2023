from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time


def calc(f):
    return str(math.log(abs(12*math.sin(int(f)))))


link = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()
browser.get(link)

print_box = browser.find_element(By.ID, 'treasure')
number = print_box.get_attribute('valuex')


input1 = browser.find_element(By.ID, 'answer')
input1.send_keys(calc(number))

not_robot = browser.find_element(By.ID, 'robotCheckbox')
not_robot.click()

robots_rule = browser.find_element(By.ID, 'robotsRule')
robots_rule.click()

submit_click = browser.find_element(By.CSS_SELECTOR, 'button.btn' )
submit_click.click()

time.sleep(15)
browser.quit()
