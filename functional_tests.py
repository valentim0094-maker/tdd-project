from selenium import webdriver 

browser = webdriver.Firefox() 
browser.get('http://127.0.0.1:8080') 

assert 'install' in browser.title