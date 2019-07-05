from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math
import pytest


@pytest.fixture()
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.mark.parametrize('get_link',
                         ["https://stepik.org/lesson/236895/step/1", "https://stepik.org/lesson/236896/step/1",
                          "https://stepik.org/lesson/236897/step/1", "https://stepik.org/lesson/236898/step/1",
                          "https://stepik.org/lesson/236899/step/1", "https://stepik.org/lesson/236903/step/1",
                          "https://stepik.org/lesson/236904/step/1", "https://stepik.org/lesson/236905/step/1"])
class TestAnswer(object):
    def test_send_answer_for_pages(self, browser, get_link):
        link = get_link
        browser.get(link)
        browser.implicitly_wait(5)
        input = browser.find_element_by_tag_name("textarea")
        answer = math.log(int(time.time()))
        input.send_keys(str(answer))

        # WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.TAG_NAME, "button")))
        button = browser.find_element_by_tag_name("button")
        button.click()

        message = browser.find_element_by_class_name("smart-hints__hint").text
        print("\n" + message)
        WebDriverWait(browser, 3).until(EC.text_to_be_present_in_element((By.CLASS_NAME, "smart-hints__hint"), "Correct!"))
