from selenium import webdriver
from selenium.webdriver.support.ui import Select




link = "http://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()
browser.get(link)
    
x_element = browser.find_element_by_css_selector('#num1')
x = x_element.text

y_element = browser.find_element_by_css_selector('#num2')
y = y_element.text


z = str(str(int(x)+int(y)))

print(z)

select = Select(browser.find_element_by_tag_name("select"))
select.select_by_visible_text(z)

    
button = browser.find_element_by_css_selector('[type="submit"]')
button.click()

    
