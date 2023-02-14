from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

options=Options()
options.add_argument('--headless')

driver = webdriver.Firefox(options=options)

driver.get("https://stepik.org/lesson/25969/step/8")
print(driver.title)
driver.quit()
