from selenium import webdriver
from math import log, sin
import time

link = 'http://suninjuly.github.io/redirect_accept.html'
browser = webdriver.Chrome()


def calc(x):
    return str(log(abs(12 * sin(int(x)))))


try:
    browser.get(link)
    browser.find_element_by_tag_name('button').click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    x = browser.find_element_by_id('input_value').text
    browser.find_element_by_id("answer").send_keys(calc(x))
    browser.find_element_by_tag_name('button').click()
    alert = browser.switch_to.alert
    alert_text = alert.text
    print(alert_text.split(' ')[-1])


finally:
    time.sleep(5)
    browser.quit()