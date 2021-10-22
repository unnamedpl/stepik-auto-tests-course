from selenium import webdriver
import time
import math

link = 'http://suninjuly.github.io/get_attribute.html'
browser = webdriver.Chrome()


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser.get(link)
    element = browser.find_element_by_id('treasure')
    val = element.get_attribute('valuex')
    y = calc(val)
    input1 = browser.find_element_by_id('answer').send_keys(y)
    option1 = browser.find_element_by_id('robotCheckbox').click()
    option2 = browser.find_element_by_id('robotsRule').click()
    button = browser.find_element_by_xpath('//button').click()


    print(y)
finally:
    time.sleep(10)
    browser.quit()