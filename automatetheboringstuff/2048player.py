#Excercise 3 Chapter 11 
#2048

import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys 


browser = webdriver.Firefox() 
browser.get('https://gabrielecirulli.github.io/2048/')
page = browser.find_element_by_tag_name('html')

for i in range(1000): 
    for key in [Keys.UP,Keys.DOWN,Keys.LEFT,Keys.RIGHT]:
        page.send_keys(key) 
        time.sleep(1)
    if browser.find_element_by_css_selector('.retry-button').is_displayed():
        browser.find_element_by_css_selector('.retry-button').click() 
    
