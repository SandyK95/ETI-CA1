import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

def test():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('http://localhost:8000/projects/')

test()

def test():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('http://localhost:8000/projects/')


    
