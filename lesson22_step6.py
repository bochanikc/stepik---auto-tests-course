from selenium import webdriver
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
link = "https://suninjuly.github.io/execute_script.html"
browser.get(link)
x = browser.find_element_by_id("input_value").text
answer = calc(x)

browser.execute_script("window.scrollBy(0, 100);")

browser.find_element_by_id("answer").send_keys(answer)

checkbox = browser.find_element_by_id("robotCheckbox")
checkbox.click()

radio = browser.find_element_by_id("robotsRule")
radio.click()

button = browser.find_element_by_tag_name("button")
button.click()
