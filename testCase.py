import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#from selenium.webdriver.common.by import By
#from selenium.common.exceptions import TimeoutException

#from selenium.webdriver.support.select import Select

def test_open():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('http://localhost:8000/projects/')
    driver.quit()

#test_open()

def test_scrolling():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('http://localhost:8000/projects/')
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    #html = driver.find_element_by_tag_name('html')
    #html.send_keys(Keys.END)
    time.sleep(2)
    driver.quit()

#test_scrolling()

def test_blog():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('http://localhost:8000/projects/')
    elem = driver.find_element_by_link_text('Blog')
    elem.click()
    driver.quit()

#test_blog()

def test_blog_CCAactivities():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('http://localhost:8000/projects/')
    elem = driver.find_element_by_link_text('Blog')
    elem.click()
    time.sleep(2)
    elem = driver.find_element_by_link_text('CCA Activites - Ngee Ann Polytechnic')
    elem.click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'id_author')))
    yourName = driver.find_element_by_id('id_author')
    yourName.send_keys("Test")
    enterComment = driver.find_element_by_id('id_body')
    enterComment.send_keys("Good Job")
    button = driver.find_element_by_link_text("Submit")
    button.click()
    
test_blog_CCAactivities()
