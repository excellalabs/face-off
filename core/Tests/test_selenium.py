from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Firefox()
driver.get("http://localhost:8111")

print driver.title
assert "Sign In" in driver.title
loginButton = driver.find_element_by_name('signIn')

loginButton.click()

usernameElement = driver.find_element_by_name('login').send_keys('sean.lewis@excella.com')
passwordElement = driver.find_element_by_name('password').send_keys('Excella2014')

yammerButton = driver.find_element_by_class_name('yj-btn')
yammerButton.click()

print driver.title

assert 'Face It' in driver.title

driver.close()