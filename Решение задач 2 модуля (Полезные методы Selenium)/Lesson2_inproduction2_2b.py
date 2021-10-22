from selenium import webdriver
import time
from math import sin, log

link = 'http://SunInJuly.github.io/execute_script.html'
browser = webdriver.Chrome()

try:
    browser.get(link)
    x = browser.find_element_by_id('input_value').text
    x = log(abs(12 * sin(int(x))))
    input1 = browser.find_element_by_id('answer').send_keys(str(x))
    check1 = browser.find_element_by_id('robotCheckbox').click()
    check2 = browser.find_element_by_id('robotsRule')
    browser.execute_script("return arguments[0].scrollIntoView(true);", check2)
    check2.click()
    button = browser.find_element_by_tag_name('button')
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

finally:
    time.sleep(10)
    browser.quit()

