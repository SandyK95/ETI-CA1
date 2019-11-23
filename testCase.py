import os
import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


#----------------No Need--------------------------------
#from selenium.common.exceptions import TimeoutException
#from selenium.webdriver.support.select import Select
#from rp-portfolio.manage import *

def test_open():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('http://localhost:8000/projects/')
    assert "Welcome!" in driver.page_source
    driver.quit()
    #add title

test_open()

def test_scrolling():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('http://localhost:8000/projects/')
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    elem = driver.find_element(By.XPATH, '//h4[text()="Education"]')
    assert "Education" in elem.text
    time.sleep(3)
    driver.quit()

test_scrolling()

def test_blog():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('http://localhost:8000/projects/')
    elem = driver.find_element_by_link_text('Blog')
    elem.click()
    assert "Blog Index" in driver.page_source
    driver.quit()

test_blog()

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
    putComment = "Good Job" 
    enterComment.send_keys(putComment)
    button = driver.find_element_by_class_name("btn.btn-primary")
    button.click()
    driver.implicitly_wait(10)
    assert driver.find_element_by_xpath("//p[text()='"+ putComment +"']") 
    driver.quit()
    
test_blog_CCAactivities()
    
def test_blog_Photography():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('http://localhost:8000/projects/')
    elem = driver.find_element_by_link_text('Blog')
    elem.click()
    time.sleep(2)
    elem = driver.find_element_by_link_text('Photography')
    elem.click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'id_author')))
    yourName = driver.find_element_by_id('id_author')
    yourName.send_keys("Test")
    enterComment = driver.find_element_by_id('id_body')
    putComment = "Good Job" 
    enterComment.send_keys(putComment)
    button = driver.find_element_by_class_name("btn.btn-primary")
    button.click()
    driver.implicitly_wait(10)
    assert driver.find_element_by_xpath("//p[text()='"+ putComment +"']") 
    driver.quit()
    
test_blog_Photography()

def test_blog_Project():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('http://localhost:8000/projects/')
    elem = driver.find_element_by_link_text('Blog')
    elem.click()
    time.sleep(2)
    elem = driver.find_element_by_link_text('Purple Project')
    elem.click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'id_author')))
    yourName = driver.find_element_by_id('id_author')
    yourName.send_keys("Test")
    enterComment = driver.find_element_by_id('id_body')
    putComment = "Good Job" 
    enterComment.send_keys(putComment)
    button = driver.find_element_by_class_name("btn.btn-primary")
    button.click()
    driver.implicitly_wait(10)
    assert driver.find_element_by_xpath("//p[text()='"+ putComment +"']")
    driver.quit()
    
test_blog_Project()

def test_withoutbody():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('http://localhost:8000/projects/')
    elem = driver.find_element_by_link_text('Blog')
    elem.click()
    time.sleep(2)
    elem = driver.find_element_by_link_text('Purple Project')
    elem.click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'id_author')))
    yourName = driver.find_element_by_id('id_author')
    yourName.send_keys("Test")
    button = driver.find_element_by_class_name("btn.btn-primary")
    button.click()
    driver.implicitly_wait(10)
    assert driver.find_element_by_css_selector("textarea:invalid")
    driver.quit()
    
test_withoutbody()

def test_withoutauthor():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('http://localhost:8000/projects/')
    elem = driver.find_element_by_link_text('Blog')
    elem.click()
    time.sleep(2)
    elem = driver.find_element_by_link_text('Purple Project')
    elem.click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'id_body')))
    enterComment = driver.find_element_by_id('id_body')
    enterComment.send_keys("Good Job")
    button = driver.find_element_by_class_name("btn.btn-primary")
    button.click()
    driver.implicitly_wait(10)
    assert driver.find_element_by_css_selector("input:invalid")
    driver.quit()
    
test_withoutauthor()

def test_maxlength60():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('http://localhost:8000/projects/')
    elem = driver.find_element_by_link_text('Blog')
    elem.click()
    time.sleep(2)
    elem = driver.find_element_by_link_text('Purple Project')
    elem.click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'id_author')))
    yourName = driver.find_element_by_id('id_author')
    yourName.send_keys("AGNLSDNGDFMBASLNGASLNGALSNGLSDNGASLNGASLGNASLGNAGNLSDNGDFMBASLNGASLNGALSNGLSDNGASLNGASLGNASLGNASLNGSALGNGNLSDNGDFMBASLNGASLNGALSNGLSDNGASLNGASLGNASLGNASLNGSALGGNLSDNGD;FMBASLNGASLNGALSNGLSDNGASLNGASLGNASLGNASLNGSALGGNLSDNGD;FMBASLNGASLNGALSNGLSDNGASLNGASLGNASLGNASLNGSALGGNLSDNGD;FMBASLNGASLNGALSNGLSDNGASLNGASLGNASLGNASLNGSALGGNLSDNGD;FMBASLNGASLNGALSNGLSDNGASLNGASLGNASLGNASLNGSALGGNLSDNGD;FMBASLNGASLNGALSNGLSDNGASLNGASLGNASLGNASLNGSALGGNLSDNGD;FMBASLNGASLNGALSNGLSDNGASLNGASLGNASLGNASLNGSALGGNLSDNGD;FMBASLNGASLNGALSNGLSDNGASLNGASLGNASLGNASLNGSALGGNLSDNGD;FMBASLNGASLNGALSNGLSDNGASLNGASLGNASLGNASLNGSALGGNLSDNGD;FMBASLNGASLNGALSNGLSDNGASLNGASLGNASLGNASLNGSALGGNLSDNGD;FMBASLNGASLNGALSNGLSDNGASLNGASLGNASLGNASLNGSALGGNLSDNGD;FMBASLNGASLNGALSNGLSDNGASLNGASLGNASLGNASLNGSALGGNLSDNGD;FMBASLNGASLNGALSNGLSDNGASLNGASLGNASLGNASLNGSALGGNLSDNGD;FMBASLNGASLNGALSNGLSDNGASLNGASLGNASLGNASLNGSALGGNLSDNGD;FMBASLNGASLNGALSNGLSDNGASLNGASLGNASLGNASLNGSALGGNLSDNGD;FMBASLNGASLNGALSNGLSDNGASLNGASLGNASLGNASLNGSALGGNLSDNGD;FMBASLNGASLNGALSNGLSDNGASLNGASLGNASLGNASLNGSALGGNLSDNGD;FMBASLNGASLNGALSNGLSDNGASLNGASLGNASLGNASLNGSALGGNLSDNGD;FMBASLNGASLNGALSNGLSDNGASLNGASLGNASLGNASLNGSALGGNLSDNGD;FMBASLNGASLNGALSNGLSDNGASLNGASLGNASLGNASLNGSALGGNLSDNGD;FMBASLNGASLNGALSNGLSDNGASLNGASLGNASLGNASLNGSALGGNLSDNGD;FMBASLNGASLNGALSNGLSDNGASLNGASLGNASLGNASLNGSALGGNLSDNGD;FMBASLNGASLNGALSNGLSDNGASLNGASLGNASLGNASLNGSALGGNLSDNGD;FMBASLNGASLNGALSNGLSDNGASLNGASLGNASLGNASLNGSALGGNLSDNGD;FMBASLNGASLNGALSNGLSDNGASLNGASLGNASLGNASLNGSALGGNLSDNGD;FMBASLNGASLNGALSNGLSDNGASLNGASLGNASLGNASLNGSALGGNLSDNGD;FMBASLNGASLNGALSNGLSDNGASLNGASLGNASLGNASLNGSALGGNLSDNGD;FMBASLNGASLNGALSNGLSDNGASLNGASLGNASLGNASLNGSALGGNLSDNGD;FMBASLNGASLNGALSNGLSDNGASLNGASLGNASLGNASLNGSALGGNLSDNGD;FMBASLNGASLNGALSNGLSDNGASLNGASLGNASLGNASLNGSALGGNLSDNGD;FMBASLNGASLNGALSNGLSDNGASLNGASLGNASLGNASLNGSALGGNLSDNGD;FMBASLNGASLNGALSNGLSDNGASLNGASLGNASLGNASLNGSALGGNLSDNGD;FMBASLNGASLNGALSNGLSDNGASLNGASLGNASLGNASLNGSALGGNLSDNGD;FMBASLNGASLNGALSNGLSDNGASLNGASLGNASLGNASLNGSALGGNLSDNGD;FMBASLNGASLNGALSNGLSDNGASLNGASLGNASLGNASLNGSALGGNLSDNGD;FMBASLNGASLNGALSNGLSDNGASLNGASLGNASLGNASLNGSALGGNLSDNGD;FMBASLNGASLNGALSNGLSDNGASLNGASLGNASLGNASLNGSALGGNLSDNGD;FMBASLNGASLNGALSNGLSDNGASLNGASLGNASLGNASLNGSALGGNLSDNGD;FMBASLNGASLNGALSNGLSDNGASLNGASLGNASLGNASLNGSALGASLGNSALGNLNGLSNAGNLSDNGD;FMBASLNGASLNGALSNGLSDNGASLNGASLGNASLGNASLNGSALGNASLGNSALGNLNGLSNAGNLSDNGD;FMBASLNGASLNGALSNGLSDNGASLNGASLGNASLGNASLNGSALGNASLGNSALGNLNGLSNAGNLSDNGD;FMBASLNGASLNGALSNGLSDNGASLNGASLGNASLGNASLNGSALGNASLGNSALGNLNGLSNAGNLSDNGD;FMBASLNGASLNGALSNGLSDNGASLNGASLGNASLGNASLNGSALGNASLGNSALGNLNGLSNAGNLSDNGD;FMBASLNGASLNGALSNGLSDNGASLNGASLGNASLGNASLNGSALGNASLGNSALGNLNGLSNAGNLSDNGD;FMBASLNGASLNGALSNGLSDNGASLNGASLGNASLGNASLNGSALGNASLGNSALGNLNGLSNAGNLSDNGD;FMBASLNGASLNGALSNGLSDNGASLNGASLGNASLGNASLNGSALGNASLGNSALGNLNGLSNAGNLSDNGD;FMBASLNGASLNGALSNGLSDNGASLNGASLGNASLGNASLNGSALGNASLGNSALGNLNGLSNAGNLSDNGD;FMBASLNGASLNGALSNGLSDNGASLNGASLGNASLGNASLNGSALGNASLGNSALGNLNGLSNAGNLSDNGD;FMBASLNGASLNGALSNGLSDNGASLNGASLGNASLGNASLNGSALGNASLGNSALGNLNGLSNAGNLSDNGD;FMBASLNGASLNGALSNGLSDNGASLNGASLGNASLGNASLNGSALGNASLGNSALGNLNGLSNAGNLSDNGD;FMBASLNGASLNGALSNGLSDNGASLNGASLGNASLGNASLNGSALGNASLGNSALGNLNGLSNAGNLSDNGD;FMBASLNGASLNGALSNGLSDNGASLNGASLGNASLGNASLNGSALGNASLGNSALGNLNGLSNASLNGSALGNASLGNSALGNLNGLSN")

    assert yourName.get_attribute('maxlength')
    
    enterComment = driver.find_element_by_id('id_body')
    enterComment.send_keys("Good Job")
    button = driver.find_element_by_class_name("btn.btn-primary")
    button.click()
    driver.implicitly_wait(10)
    driver.quit()

test_maxlength60()

def test_without():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('http://localhost:8000/projects/')
    elem = driver.find_element_by_link_text('Blog')
    elem.click()
    time.sleep(2)
    elem = driver.find_element_by_link_text('Purple Project')
    elem.click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'btn.btn-primary')))
    button = driver.find_element_by_class_name("btn.btn-primary")
    button.click()

    assert driver.find_element_by_css_selector("input:invalid")
    assert driver.find_element_by_css_selector("textarea:invalid")
    driver.implicitly_wait(10)
    time.sleep(2)
    driver.quit()
    
test_without()

def test_authorwRandom():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('http://localhost:8000/projects/')
    elem = driver.find_element_by_link_text('Blog')
    elem.click()
    time.sleep(2)
    elem = driver.find_element_by_link_text('Purple Project')
    elem.click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'id_author')))
    yourName = driver.find_element_by_id('id_author')
    text = "?/$^&@$*3252"
    yourName.send_keys(text)
    assert yourName.get_attribute('value') == text
    
    enterComment = driver.find_element_by_id('id_body')
    enterComment.send_keys("Good Job")
    button = driver.find_element_by_class_name("btn.btn-primary")
    button.click()
    driver.implicitly_wait(10)

    driver.quit()

test_authorwRandom()

def test_loginwithadmin():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('http://localhost:8000/admin/')
    Username = driver.find_element_by_id('id_username')
    Username.send_keys("sandy")
    Password = driver.find_element_by_id('id_password')
    Password.send_keys("18U48c95")
    driver.find_element_by_xpath("//input[@type='submit' and @value='Log in']").click()
    time.sleep(2)
    assert "Site administration | Django site admin" in driver.title
    driver.quit()
    
test_loginwithadmin()

def test_loginwithadminFalseUser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('http://localhost:8000/admin/')
    Username = driver.find_element_by_id('id_username')
    Username.send_keys("kee")
    Password = driver.find_element_by_id('id_password')
    Password.send_keys("18U48c95")
    driver.find_element_by_xpath("//input[@type='submit' and @value='Log in']").click()
    time.sleep(2)
    assert "Please enter the correct username and password for a staff account. Note that both fields may be case-sensitive." in driver.find_element_by_class_name("errornote").text
    driver.quit()
    
test_loginwithadminFalseUser()

def test_loginwithadminFalsePassword():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('http://localhost:8000/admin/')
    Username = driver.find_element_by_id('id_username')
    Username.send_keys("sandy")
    Password = driver.find_element_by_id('id_password')
    Password.send_keys("12345678")
    driver.find_element_by_xpath("//input[@type='submit' and @value='Log in']").click()
    time.sleep(2)
    assert "Please enter the correct username and password for a staff account. Note that both fields may be case-sensitive." in driver.find_element_by_class_name("errornote").text
    driver.quit()
    
test_loginwithadminFalsePassword()

def test_loginwithadminWithout():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('http://localhost:8000/admin/')
    driver.find_element_by_xpath("//input[@type='submit' and @value='Log in']").click()
    time.sleep(2)
    assert driver.find_element_by_css_selector("input:invalid")
    driver.quit()
    
test_loginwithadminWithout()

def test_loginwithadminWithoutName():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('http://localhost:8000/admin/')
    Password = driver.find_element_by_id('id_password')
    Password.send_keys("12345678")
    driver.find_element_by_xpath("//input[@type='submit' and @value='Log in']").click()
    time.sleep(2)
    assert driver.find_element_by_css_selector("input:invalid")
    driver.quit()
    
test_loginwithadminWithoutName()

def test_loginwithadminWithoutPassword():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('http://localhost:8000/admin/')
    Username = driver.find_element_by_id('id_username')
    Username.send_keys("sandy")
    driver.find_element_by_xpath("//input[@type='submit' and @value='Log in']").click()
    time.sleep(2)
    assert driver.find_element_by_css_selector("input:invalid")
    driver.quit()
    
test_loginwithadminWithoutPassword()

