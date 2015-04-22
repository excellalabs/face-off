from behave import given, when, then
from helper import *

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
    for i in range(1, 4):
        assert "greyOut" in get_card(context.browser, i).get_attribute("class")

@then('all the cards should flip')
def step(context):
    for i in range(0, 4):
        assert "clickFlip" in get_card(context.browser, i).get_attribute("class")

@then('they logout')
def step(context):
    context.browser.find_element_by_id('logout').click()