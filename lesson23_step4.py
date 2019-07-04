from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/alert_accept.html"
browser.get(link)

button = browser.find_element_by_tag_name("button")
button.click()

confirm = browser.switch_to.alert
confirm.accept()

time.sleep(1)

x = browser.find_element_by_id("input_value").text
answer = calc(x)

browser.find_element_by_id("answer").send_keys(answer)

button = browser.find_element_by_tag_name("button")
button.click()
