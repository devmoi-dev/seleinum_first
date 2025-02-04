from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import time
import json

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

def is_page_loading(driver):
    while True:
        sleep(1.5)
        is_complete = driver.execute_script('return document.readyState')
        if is_complete == 'complete':  # If page is fully loaded
            break


with open("gcookies.txt", "r") as file:
    try:
        Cook = json.load(file)
    except json.JSONDecodeError:
        print("Error: The file content is not valid JSON.")


driver.get("https://google.com")

is_page_loading(driver)

for cookie in Cook:
    cookie.update({"sameSite": "Lax"})
    driver.add_cookie(dict(cookie))

driver.implicitly_wait(5)
input_element = driver.find_element(By.CLASS_NAME, "gLFyf")
input_element.clear()
input_element.send_keys("code with python" + Keys.ENTER)
time.sleep(10)

driver.quit()