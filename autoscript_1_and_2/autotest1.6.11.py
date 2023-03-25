from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "http://suninjuly.github.io/registration2.html" # ссылка на второго сайта
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.XPATH, "//input[@class='form-control first']") # поиск поля ввода для имени через XPATH
    input1.send_keys("Alex")
    input2 = browser.find_element(By.XPATH, "//input[@class='form-control second']") # поиск поля ввода для фамилии
    input2.send_keys("Berlizov")
    input3 = browser.find_element(By.XPATH, "//input[@class='form-control third']") # поиск поля ввода для почты
    input3.send_keys("goose@mail.ru")
    # изначально были перепутаны поля для фамилиии и почты. что-то из них не вводилось вообще, потому что поля нет.
    button = browser.find_element(By.CSS_SELECTOR, "button.btn") #
    button.click()

    time.sleep(1) # пауза на подумать

    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1") # ищем нужное нам завершение
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text # сравниваем

finally:
    time.sleep(30) # ждем 30 секунд
    browser.quit() # потом все закрываем
