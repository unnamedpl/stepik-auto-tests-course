# import lib
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from math import log, sin

# comment
def calc(x):
    return str(log(abs(12 * sin(int(x)))))


# action
browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/explicit_wait2.html')

buy = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, 'price'), '100')
)
browser.find_element_by_id('book').click()
x = browser.find_element(By.ID, 'input_value').text
browser.find_element(By.ID, 'answer').send_keys(calc(x))
browser.find_element(By.ID, 'solve').click()
alert = browser.switch_to.alert
alert_text = alert.text
print(alert_text.split(' ')[-1])
alert.accept()
browser.quit()
