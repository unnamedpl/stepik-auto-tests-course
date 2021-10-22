from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

link = 'http://suninjuly.github.io/selects1.html'
browser = webdriver.Chrome()

try:
    browser.get(link)
    num1 = browser.find_element_by_id('num1')
    num2 = browser.find_element_by_id('num2')
    answer = int(num1.text) + int(num2.text)
    select = Select(browser.find_element_by_id('dropdown'))
    select.select_by_value(str(answer))
    button = browser.find_element_by_xpath('//button').click()


finally:
    time.sleep(10)
    browser.quit()