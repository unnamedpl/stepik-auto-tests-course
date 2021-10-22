from selenium import webdriver
import time
import math

link = 'http://suninjuly.github.io/math.html'
browser = webdriver.Chrome()


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser.get(link)
    x_element = browser.find_element_by_css_selector('label > #input_value')
    x = x_element.text
    y = calc(x)
    input1 = browser.find_element_by_css_selector('.form-control')
    input1.send_keys(y)
    option1 = browser.find_element_by_css_selector('.form-check.form-check-custom > .form-check-input')
    option1.click()
    option2 = browser.find_element_by_css_selector("[for='robotsRule']")
    option2.click()
    button1 = browser.find_element_by_xpath('//button')
    button1.click()


finally:
    time.sleep(15)
    browser.quit()



