from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/explicit_wait2.html")

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    wait = WebDriverWait(browser, 12)
    wait_until_100 = wait.until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    button = browser.find_element(By.CSS_SELECTOR, "#book")
    button.click()

    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y = calc(x)

    input_answer = browser.find_element(By.CSS_SELECTOR, "#answer")
    input_answer.send_keys(y)

    submit_button = browser.find_element(By.XPATH, '//button[contains(text(),"Submit")]')
    submit_button.click()

finally:
    time.sleep(3)