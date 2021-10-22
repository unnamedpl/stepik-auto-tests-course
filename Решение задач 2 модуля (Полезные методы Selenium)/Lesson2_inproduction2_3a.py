from selenium import webdriver
from math import log, sin
import time

link = 'http://suninjuly.github.io/alert_accept.html'
browser = webdriver.Chrome()


def num(x):
    return log(abs(12 * sin(int(x))))


try:
    browser.get(link)
    browser.find_element_by_tag_name('button').click()
    alert = browser.switch_to.alert
    alert.accept()
    x = browser.find_element_by_id('input_value').text
    y = num(x)
    input1 = browser.find_element_by_tag_name('input').send_keys(str(y))
    button1 = browser.find_element_by_tag_name('button').click()
    alert2 = browser.switch_to.alert
    alert_text = alert2.text
    print(alert_text.split(':')[-1])

finally:
    time.sleep(5)
    browser.quit()
