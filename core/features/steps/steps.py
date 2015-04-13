from behave import given, when, then


@given('the user is at the Face Off application')
def step(context):
    context.browser.get('http://localhost:8000')


@given('the user has logged into the Face Off application')
def step(context):
    context.browser.get('http://localhost:8000')
    login(context, 'emmanuel.apau@excella.com', 'ForWork12')


@given('they are in practice mode')
def step(context):
    context.browser.find_element_by_id('easyGame').click()


@when('the user clicks the first card')
def step(context):
    click_card(context.browser, 0)


@when('they sign into the application through yammer')
def step(context):
    login(context, 'emmanuel.apau@excella.com', 'ForWork12')


@then('they should arrive at the begin game screen')
def step(context):
    assert 'Face Off' in context.browser.title


@then('all the cards should flip')
def step(context):
    for i in range(0, 4):
        assert "clickFlip" in get_card(context.browser, i).get_attribute("class")


# Helper Methods
def login(context, username, password):
    context.browser.find_element_by_name('signIn').click()
    context.browser.find_element_by_name('login').send_keys(username)
    context.browser.find_element_by_name('password').send_keys(password)
    context.browser.find_element_by_class_name('yj-btn').click()


def click_card(driver, index):
    driver.find_element_by_id('colleague' + str(index)).click()


def get_card(driver, index):
    return driver.find_element_by_id('colleague' + str(index))