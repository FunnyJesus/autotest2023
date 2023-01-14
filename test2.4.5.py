from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser =  webdriver.Chrome()
browser.get('http://suninjuly.github.io/cats.html')

find_button = browser.find_element(By.ID, "button")


time.sleep(10)
browser.quit()

