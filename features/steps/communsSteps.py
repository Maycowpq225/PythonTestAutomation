from behave import *
from utils.personUtil import PersonUtil

@given('a new user is created')
def step_impl(context):
    context.person = PersonUtil()


@then('validate the error message {message}')
def step_impl(context, message):
    ...
