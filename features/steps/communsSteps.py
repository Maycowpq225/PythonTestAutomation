from behave import *
from features.services.OneSecmailService import OneSecmailService

@given('a new user is created')
def step_impl(context):
    context.email = OneSecmailService().generateNewEmail()
    print(context.email)


@then('validate the error message {message}')
def step_impl(context, message):
    ...
