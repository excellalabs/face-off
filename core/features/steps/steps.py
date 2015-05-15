from behave import given, when, then
from helper import *
import random
import time

# Given statements
# -----------------
@given('the user is at the Face Off application')
def step(context):
    context.browser.get('http://localhost:8111')


@given('the user has logged into the Face Off application')
def step(context):
    context.browser.get('http://localhost:8111')
    login(context, 'testuser@excella.com', 'Mufa0772')


@given('they are in practice mode')
def step(context):
    context.browser.find_element_by_id('easyGame').click()

@given('they are in competitive mode')
def step(context):
    context.browser.find_element_by_id('hardGame').click()

# When statements
# ---------------
@when('they select play again')
def step(context):
    context.browser.find_element_by_id('endGame').click()

@when('they play through the competitive mode')
def step(context):
    context.browser.find_element_by_id('hardGame').click()
    play_through_competitive_mode(context.browser)

@when('the user clicks a card')
def step(context):
    random_card = random.randint(0, 3)
    click_card(context.browser, random_card)
    time.sleep(3)

@when('they hover over a card')
def step(context):
    get_hover(context.browser, 0)

@when('the user clicks the first card')
def step(context):
    click_card(context.browser, 0)

@when('they sign into the application through yammer with a picture')
def step(context):
    login(context, 'testuser@excella.com', 'Mufa0772')

@when('they sign into the application through yammer with no picture')
def step(context):
    login(context, 'testuser2@excella.com', 'Mufa0773')

@when('they are in practice mode')
def step(context):
    context.browser.find_element_by_id('easyGame').click()

@when('they are in competitive mode')
def step(context):
    context.browser.find_element_by_id('hardGame').click()

@when('they play through the Educational Mode')
def step(context):
    play_through_education_mode(context.browser)




# Then statements
# ----------------
@then('they should arrive at the results page')
def step(context):
    assert 'Results' in context.browser.title


@then('they should arrive at the metrics page')
def step(context):
    assert 'Metrics' in context.browser.title

@then('they should be able to select metrics')
def step(context):
    context.browser.find_element_by_id('metrics').click()

@then('they should arrive at the no photo game screen')
def step(context):
    context.browser.find_element_by_id('noPicButton').click()

@then('they should be at the home screen')
def step(context):
    assert 'Sign In' in context.browser.title

@then('they should arrive at the begin game screen')
def step(context):
    assert 'Face Off' in context.browser.title

@then('they should have the option to add a photo')
def step(context):
    user = get_user()
    context.browser.find_element_by_id('noPicLink').click()
    assert user in context.browser.getCurrentUrl()

@then('all the cards should not flip')
def step(context):
    for i in range(1, 3):
        assert "greyOut" in get_card(context.browser, i).get_attribute("class")

@then('all the cards should flip')
def step(context):
    for i in range(0, 4):
        assert "clickFlip" in get_card(context.browser, i).get_attribute("class")

@then('they logout')
def step(context):
    context.browser.find_element_by_id('logout').click()

@then('the share icon is visible')
def step(context):
    for i in range(0, 3):
        assert "block" in context.browser.find_element_by_class_name('fa-share').value_of_css_property('display')

@then('the share icon is not visible')
def step(context):
    for i in range(0, 3):
        assert "none" in context.browser.find_element_by_class_name('fa-share').value_of_css_property('display')

@then('the card rumbles')
def step(context):
    assert not "0" in context.browser.find_element_by_id('colleague0').value_of_css_property('left')

@then('the cards are disabled')
def step(context):
    for i in range(0, 3):
        context.browser.find_elements_by_xpath('//colleague'+str(i)+'[contains(@class, "disabled")]')
