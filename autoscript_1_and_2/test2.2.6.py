from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

def num(y):
    return str(math.log(abs(12*math.sin(int(x)))))

link = 'http://suninjuly.github.io/execute_script.html'
browser = webdriver.Chrome()
browser.get(link)

find_x = browser.find_element(By.ID, 'input_value')
x = int(find_x.text)

find_answer = browser.find_element(By.ID, 'answer')
find_answer.send_keys(num(x))

find_robocheck = browser.find_element(By.ID, 'robotCheckbox')
find_robocheck.click()
time.sleep(2)
find_roborule = browser.find_element(By.ID, 'robotsRule')
browser.execute_script("return arguments[0].scrollIntoView(true);", find_roborule)
find_roborule.click()

find_submit = browser.find_element(By.CSS_SELECTOR, 'button.btn')
find_submit.click()

time.sleep(15)
browser.quit()


