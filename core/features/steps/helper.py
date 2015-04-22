from selenium.webdriver.support.wait import WebDriverWait
import random
import time


# Helper methods to consolidate steps.py
def login(context, username, password):
    context.browser.find_element_by_name('signIn').click()
    context.browser.find_element_by_name('login').send_keys(username)
    context.browser.find_element_by_name('password').send_keys(password)
    context.browser.find_element_by_class_name('yj-btn').click()


def click_card(driver, index):
    driver.find_element_by_id('colleague' + str(index)).click()


def get_card(driver, index):
    return driver.find_element_by_id('colleague' + str(index))


def get_user(driver):
    return driver.find_element_by_id('userName')


def click_next_round(driver):
    driver.find_element_by_id('nextRound').click()


def play_through_education_mode(driver):
    driver.find_element_by_id('easyGame').click()
    click_card(driver, 0)
    click_next_round(driver)
    click_card(driver, 2)
    click_next_round(driver)
    click_card(driver, 3)
    click_next_round(driver)
    click_card(driver, 1)
    click_next_round(driver)
    click_card(driver, 0)
    driver.find_element_by_id('resultsSubmit').click()

def play_through_competitive_mode(driver):
    # First round
    random_card = random.randint(1, 3)
    print(random_card)
    click_card(driver, random_card)
    time.sleep(5)
    # Second round
    random_card = random.randint(1, 3)
    print(random_card)
    click_card(driver, random_card)
    time.sleep(5)
    # Third round
    random_card = random.randint(1, 3)
    print(random_card)
    click_card(driver, random_card)
    time.sleep(5)
    # Fourth round
    random_card = random.randint(1, 3)
    print(random_card)
    click_card(driver, random_card)
    time.sleep(5)
    # Fifth round
    random_card = random.randint(1, 3)
    print(random_card)
    click_card(driver, random_card)
    time.sleep(5)
