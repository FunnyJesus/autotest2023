from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = 'https://litgorod.ru/'

@pytest.fixture
def browser():
    print('\nStart browser for test...')
    browser = webdriver.Chrome()
    yield browser
    print('\nBrowser quit.')
    browser.quit()

@pytest.mark.parametrize('search', ['время','бремя','стремя'])
def test_1(browser, search):
    browser.get(link)
    browser.fullscreen_window()
    wait = WebDriverWait(browser, 5)
    add_search = wait.until (EC.element_to_be_clickable((By.ID, 'fieldq')))
    add_search.click()
    add_search.send_keys(search)
    add_search.send_keys(Keys.RETURN)
    total = wait.until (EC.visibility_of_element_located((By.CSS_SELECTOR, '#app > main > div > div > div > div.col-12.col-lg-9.flex-grow-1 > div:nth-child(2) > p > b')))
    total_text = total.text
    assert total_text != '0'

if __name__ == '__main__':
    pytest.main()

