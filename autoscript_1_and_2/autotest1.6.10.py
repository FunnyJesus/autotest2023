from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.XPATH, "//input[@placeholder='Input your name']")
    input1.send_keys("Alex")
    input2 = browser.find_element(By.XPATH, "//input[@class='form-control second']")
    input2.send_keys("Berlizov")
    input3 = browser.find_element(By.XPATH, "//input[@class='form-control third']")
    input3.send_keys("goose@mail.ru")

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    time.sleep(1)

    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(30)
    browser.quit()
