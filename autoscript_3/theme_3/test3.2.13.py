from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
import time


class TestAbs(unittest.TestCase):
    def test_123(self):
        x = webdriver.Chrome()
        x.get('http://suninjuly.github.io/registration1.html')
        find_first_name = x.find_element(By.CLASS_NAME, 'form-control first')
        find_first_name.send_keys('Alex')
        find_last_name = x.find_element(By.CLASS_NAME, 'form-control second')
        find_last_name.send_keys('Berlizov')
        find_email = x.find_element(By.CLASS_NAME, 'form-control third')
        find_email.send_keys('goose@mail.com')
        find_button_submit = x.find_element(By.CSS_SELECTOR, 'button.btn')
        find_button_submit.click()
        time.sleep(2)
        welcome_text_elt = x.find_element(By.TAG_NAME, "h1")
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text_elt.text)

    def test_456(self):
        y = webdriver.Chrome()
        y.get('http://suninjuly.github.io/registration2.html')
        find_first_name = y.find_element(By.CLASS_NAME, 'form-control first')
        find_first_name.send_keys('Alex')
        find_last_name = y.find_element(By.CLASS_NAME, 'form-control second')
        find_last_name.send_keys('Berlizov')
        find_email = y.find_element(By.CLASS_NAME, 'form-control third')
        find_email.send_keys('goose@mail.com')
        find_button_submit = y.find_element(By.CSS_SELECTOR, 'button.btn')
        find_button_submit.click()
        time.sleep(2)
        welcome_text_elt = y.find_element(By.TAG_NAME, "h1")
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text_elt.text)

if __name__ == '__main__':
    unittest.main()
