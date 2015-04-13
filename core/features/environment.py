from selenium import webdriver

BEHAVE_DEBUG_ON_ERROR = True


def setup_debug_on_error(userdata):
    global BEHAVE_DEBUG_ON_ERROR
    BEHAVE_DEBUG_ON_ERROR = userdata.getbool("BEHAVE_DEBUG_ON_ERROR")


def before_all(context):

    setup_debug_on_error(context.config.userdata)

    context.browser = webdriver.Firefox()

    # desired_capabilities = webdriver.DesiredCapabilities.FIREFOX
    # desired_capabilities['version'] = '12'
    # desired_capabilities['platform'] = 'WINDOWS'
    # desired_capabilities['name'] = 'Testing Col-League App'
    # desired_capabilities['client_key'] = '44fa53ac66807797ca8ec3f1e9f9a9d9'
    # desired_capabilities['client_secret'] = '5cc0cce8a93b22b347ffd72204d007bb'
    # webdriver.Remote(desired_capabilities=desired_capabilities, command_executor="http://hub.testingbot.com:4444/wd/hub")



def after_step(context, step):
    if BEHAVE_DEBUG_ON_ERROR and step.status == "failed":
        # -- ENTER DEBUGGER: Zoom in on failure location.
        # NOTE: Use IPython debugger, same for pdb (basic python debugger).
        import ipdb
        ipdb.post_mortem(step.exc_traceback)


def after_all(context):
    context.browser.quit()