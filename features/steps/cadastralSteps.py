from behave import *

@then('validate the cadastral page')
def validateCadastralScreen(context):
    ...

@when('fill all fields to register')
def fillFieldsRegister(context):
    ...

@when('fill all fields except the {exceptField} field')
def fillFieldsRegisterExcept(context, exceptField):
    ...

@when('click on register button')
def clickRegisterBtn(context):
    ...

@then('validate that the account has not been created')
def validateAccountNotCreated(context):
    ...


