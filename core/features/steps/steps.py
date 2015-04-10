@when('we visit col-league')
def step(context):
    context.browser.get('http://cole-league.herokuapp.com')

@then('it should have the title "Sign In"')
def step(context):
    assert context.browser.title == "Sign In"