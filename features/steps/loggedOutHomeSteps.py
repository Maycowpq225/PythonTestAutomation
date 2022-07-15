from behave import *
from features.po.loggedOutHomePage import LoggedOutHomePage

@when('user is on the logged out home page')
def step_impl(context):
    context.homePage = LoggedOutHomePage()
    context.homePage.navigateToAutomationPratice()

@when('click on sign in button logged out home')
def step_impl(context):
    ...