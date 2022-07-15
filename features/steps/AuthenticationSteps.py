from behave import *

@then('validate the authentication page')
def validateAuthenticationScreen(context):
    ...

@when('fill the field email')
def fillFieldEmail(context):
    ...

@when('fill the field email with {email}')
def fillFieldEmailWith(context, email):
    ...

@when('click on create an account')
def clickLoginBtn(context):
    ...

@when('fill the fields email with {email} and password {password}')
def fillLoginFields(context, email, password):
    ...

@when('click on sign button')
def clickLoginBtn(context):
    ...