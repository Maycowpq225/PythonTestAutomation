from behave import *
from features.po.loggedOutHomePage import LoggedOutHomePage
from nose.tools import assert_true

@given('user is on the logged out home page')
@when('user is on the logged out home page')
def step_impl(context):
    context.loggedOutHomePage = LoggedOutHomePage(context.driver)
    context.loggedOutHomePage.navigateToAutomationPratice()
    assert_true(context.loggedOutHomePage.validateLoggedOutHome())
    context.loggedOutHomePage.getScreenShotAndSave(context.scenarioFolder, 'mainScreen')


@given('click on sign in button on logged out home')
@when('click on sign in button on logged out home')
def step_impl(context):
    context.loggedOutHomePage.clickOnSignIn()
