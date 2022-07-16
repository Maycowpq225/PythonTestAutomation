from behave import *
from features.po.loggedOutHomePage import LoggedOutHomePage
from nose.tools import assert_true


@when('user is on the logged out home page')
def step_impl(context):
    context.loggedOutHomePage = LoggedOutHomePage()
    context.loggedOutHomePage.navigateToAutomationPratice()
    assert_true(context.loggedOutHomePage.validateLoggedOutHome())


@when('click on sign in button logged out home')
def step_impl(context):
    ...
