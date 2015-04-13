from helper import login

@given('the user is at the Face Off application')
def step(context):
    context.browser.get('http://localhost:8111')

@when('they sign into the application through yammer')
def step(context):
    # Helper method Login
    login(context, 'sean.lewis@excella.com', 'Excella2014')


@then('they should arrive at the begin game screen')
def step(context):
    assert 'Face Off' in context.browser.title