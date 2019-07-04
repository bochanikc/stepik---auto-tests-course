from selenium import webdriver
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
  
link = " http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()
browser.get(link)
  
#x_element = browser.find_element_by_id("input_value")
#x = x_element.text
x_element = browser.find_element_by_id("treasure")
x = x_element.get_attribute("valuex")
y = calc(x)

input_answer = browser.find_element_by_id("answer")
input_answer.send_keys(y)

checkbox = browser.find_element_by_id("robotCheckbox")
checkbox.click()

radio = browser.find_element_by_id("robotsRule")
radio.click()

submit = browser.find_element_by_class_name("btn-default")
submit.click()
