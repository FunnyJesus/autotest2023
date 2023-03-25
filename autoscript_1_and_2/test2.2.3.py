from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

def summa(x,y):
    return str(int(x)+int(y))

link = "http://suninjuly.github.io/selects1.html"

browser = webdriver.Chrome()
browser.get(link)

find_number1 = browser.find_element(By.ID, 'num1')
number1 = find_number1.text
print(number1)

find_number2 = browser.find_element(By.ID, 'num2')
number2 = find_number2.text
print(number2)

#find_dropdown = browser.find_element(By.ID, 'dropdown')
select = Select(browser.find_element(By.ID, 'dropdown'))
select.select_by_value(summa(number1, number2))

find_submit = browser.find_element(By.CSS_SELECTOR, 'button.btn')
find_submit.click()

time.sleep(10)
browser.quit()
