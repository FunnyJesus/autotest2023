from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest
link = 'http://suninjuly.github.io/registration1.html'

@pytest.fixture
def browser():
    print('\nstart browser for test..')
    browser = webdriver.Chrome()
    yield browser
    print('\nquit browser')
    browser.quit()

class TestAbs():
    def test_1(self, browser):
        browser.get(link)
        find_first_name = browser.find_element(By.CSS_SELECTOR, "body > div > form > div.first_block > div.form-group.first_class > input")
        find_first_name.send_keys('Alex')
    
        find_last_name = browser.find_element(By.CSS_SELECTOR, "body > div > form > div.first_block > div.form-group.second_class > input")
        find_last_name.send_keys('Berlizov')

        find_email = browser.find_element(By.CSS_SELECTOR, "body > div > form > div.first_block > div.form-group.third_class > input")
        find_email.send_keys('goose@mail.com')

        find_button_submit = browser.find_element(By.CSS_SELECTOR, 'button.btn')
        find_button_submit.click()
        time.sleep(2)
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        assert "Congratulations! You have successfully registered!" == welcome_text_elt.text

    #def test_2(self, browser):
        #browser.get(link)
        #find_first_name = browser.find_element(By.CSS_SELECTOR, "body > div > form > div.first_block > div.form-group.first_class > input")
        #find_first_name.send_keys('Alex')
        #find_last_name = browser.find_element(By.CSS_SELECTOR, "body > div > form > div.first_block > div.form-group.second_class > input")
        #find_last_name.send_keys('Berlizov')
        #find_email = browser.find_element(By.CSS_SELECTOR, "body > div > form > div.first_block > div.form-group.third_class > input")
        #find_email.send_keys('goose@mail.com')
        #find_button_submit = browser.find_element(By.CSS_SELECTOR, 'button.btn')
        #find_button_submit.click()
        #time.sleep(2)
        #welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        #assert "Congratulations! You have successfully registered!" == welcome_text_elt.text


if __name__ == '__main__':
    pytest.main()
