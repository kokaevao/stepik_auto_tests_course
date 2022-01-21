import os
import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome()
browser.get(link)

button = browser.find_element_by_css_selector('[type="submit"]')
button.click()

browser.switch_to.window(browser.window_handles[1])

time.sleep(1)

x_element = browser.find_element_by_css_selector('#input_value')
x = x_element.text
y = calc(x)

input0 = browser.find_element_by_css_selector('#answer')
input0.send_keys(y)

button = browser.find_element_by_css_selector('[type="submit"]')
button.click()

    
