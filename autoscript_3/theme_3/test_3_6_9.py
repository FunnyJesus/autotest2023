from selenium.webdriver.common.by import By
import pytest

link = "http://selenium1py.pythonanywhere.com/"

def test_guest_should_see_login_link_pass(browser):
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "#login_link")

def test_guest_should_see_login_link_fail(browser):
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "#magic_link")

if __name__ == '__main__':
    pytest.main()

    #pytest -v --tb=line --reruns 1 --browser_name=chrome test_3_6_9.py команда запуска в терминале
