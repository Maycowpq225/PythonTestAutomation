from behave import *
from utils.personUtil import PersonUtil
from nose.tools import assert_true
from features.po.basePage import BasePage

@given('a new user is created')
def step_impl(context):
    context.person = PersonUtil()


@then('validate the error message {message}')
def step_impl(context, message):
    context.basePage = BasePage(context.driver)
    assert_true(context.basePage.is_element_visible_by_text(message, timeout=15))
    context.basePage.getScreenShotAndSave(context.scenarioFolder, message.replace('"', '') + 'ErrorScreen')
