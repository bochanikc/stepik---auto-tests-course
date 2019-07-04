from selenium import webdriver
from selenium.webdriver.support.ui import Select

def calc(a, b):
  return int(a) + int(b)
  
link = "http://suninjuly.github.io/selects2.html"
browser = webdriver.Chrome()
browser.get(link)
  
num1_element = browser.find_element_by_id("num1")
a = num1_element.text
num2_element = browser.find_element_by_id("num2")
b = num2_element.text
y = calc(a, b)


select = Select(browser.find_element_by_tag_name("select"))
select.select_by_visible_text(str(y))

submit = browser.find_element_by_class_name("btn-default")
submit.click()
