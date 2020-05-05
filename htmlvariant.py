# -*- coding: utf-8 -*-
"""
Created on Tue May  5 22:38:01 2020

@author: emilm
"""

import time
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

CHROME = r'.\chromedriver.exe'


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")
driver = webdriver.Chrome(executable_path=CHROME,
                           chrome_options=chrome_options)

def wait_click_by_class(class_):
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME,class_))
        )
        driver.find_elements_by_class_name(class_)[0].click()
    except Exception as e:
        print(e)
        driver.quit()



driver.get('https://www.keybr.com/')
time.sleep(2)

wait_click_by_class("Tour-close")
wait_click_by_class("TextInput-fragment")

inputElement = driver.find_element_by_class_name('TextInput-fragment')

for i in range(10):
    letters = [let.text
               for let in driver.find_elements_by_class_name('TextInput-item')]
    letters = ''.join([i if i != '␣' else ' ' for i in letters])
    pyautogui.write(letters, interval=0.005)
