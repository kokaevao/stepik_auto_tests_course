from selenium import webdriver
import math
from selenium.webdriver.common.keys import Keys

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


link = "http://SunInJuly.github.io/execute_script.html"
browser = webdriver.Chrome()
browser.get(link)
    
x_element = browser.find_element_by_css_selector('#input_value')
x = x_element.text
y = calc(x)

browser.find_element_by_tag_name('body').send_keys(Keys.END)

input0 = browser.find_element_by_css_selector('#answer')
input0.send_keys(y)

    
input1 = browser.find_element_by_css_selector('#robotCheckbox')
input1.click()
input2 = browser.find_element_by_css_selector('#robotsRule')
input2.click()
    

button = browser.find_element_by_css_selector('[type="submit"]')
button.click()
    
