from behave import *
from utils.personUtil import PersonUtil
from nose.tools import assert_true
from features.po.basePage import BasePage

@given('a new user is created')
def step_impl(context):
    context.person = PersonUtil()


@then('validate the error message {message}')
def step_impl(context, message):
    context.basePage = BasePage()
    assert_true(context.basePage.is_element_visible_by_text(message, timeout=15))
