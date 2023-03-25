from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math


@pytest.fixture
def browser():
    print('\nstart browser for test..')
    browser = webdriver.Chrome()
    yield browser
    print('\nquit browser')
    browser.quit()


@pytest.mark.parametrize('links', ['236895/step/1','236896/step/1', '236897/step/1', '236898/step/1', '236899/step/1', '236903/step/1', '236904/step/1', '236905/step/1'])
class Test_Main():
    def test_lesson_364(browser, links):
        link = f"https://stepik.org/lesson/{links}/"
        browser.get(link)
        search_enter = WebDriverWait(browser, 5).until (EC.element_to_be_clickable((By.ID, "ember33")))
        search_enter.click()
        search_login = browser.find_element(By.ID, 'id_login_email')
        search_login.send_keys('rocknroll5757@gmail.com')
        search_password = browser.find_element(By.ID, 'id_login_password')
        search_password.send_keys('Additem1313')
        search_button = browser.find_element(By.CSS_SELECTOR, "#login_form>button")
        search_button.click()
    #search_ember87 = WebDriverWait(browser, 5).until (EC.element_to_be_clickable((By.ID, "ember87")))
        search_ember87 = browser.find_element(By.XPATH, "/html/body/main/div[1]/div[2]/div/div[2]/div[1]/div/article/div/div/div[2]/div/section/div/div[1]/div[2]/div/div/div/textarea")
        search_ember87.send_keys(math.log(int(time.time())))
        search_button = browser.find_element(By.CSS_SELECTOR, "button.submit-submission")
        search_button.click()
        search_correct = WebDriverWait(browser, 5).until (EC.visibility_of_element_located((By.XPATH, "/html/body/main/div[1]/div[2]/div/div[2]/div[1]/div/article/div/div/div[2]/div/div/div/div[2]/div/p")).text)
        assert search_correct != 'Correct!'
        search_correct_1 = ''
        search_correct_1 =+ search_correct
        print(search_correct_1)

if __name__ == '__main__':
    pytest.main()
