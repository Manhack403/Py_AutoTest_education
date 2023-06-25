from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "http://suninjuly.github.io/redirect_accept.html"

def calc(int_x):
    return str(math.log(abs(12 * math.sin(int_x))))
try:
    browser = webdriver.Chrome()
    browser.get(link)

    button_click = browser.find_element(By.XPATH, "//button[@type='submit']")
    button_click.click()

    new_window = browser.window_handles[1]
    switch_window_to_2 = browser.switch_to.window(new_window)

    time.sleep(1)

    value_x = browser.find_element(By.CSS_SELECTOR, "div .form-group label .nowrap#input_value")
    int_x = int(value_x.text)

    input_answer = browser.find_element(By.CSS_SELECTOR, "input#answer")
    input_answer.send_keys(calc(int_x))

    submit_button = browser.find_element(By.XPATH, "//button[@type='submit']")
    submit_button.click()

    time.sleep(2)

finally:
    time.sleep(3)