from behave import *
from features.po.authenticationPage import AuthenticationPage
from nose.tools import assert_true

@then('validate the authentication page')
def validateAuthenticationScreen(context):
    context.auPage = AuthenticationPage()
    assert_true(context.auPage.validateAuthenticationPage())

@when('fill the field register email')
def fillFieldRegisterEmail(context):
    context.auPage.fillRegisterFieldEmail(context.person.EMAIL)

@when('fill the field email with {email}')
def fillFieldEmailWith(context, email):
    context.auPage.fillRegisterFieldEmail(email)

@when('click on create an account')
def clickCreateAccount(context):
    context.auPage.clickOnCreateAnAccount()

@when('fill the login fields email with {email} and password {password}')
def fillLoginFields(context, email, password):
    context.auPage.fillLoginFieldEmail(email)
    context.auPage.fillLoginFieldPassword(password)

@when('click on sign button')
def clickSignInBtn(context):
    context.auPage.clickOnSignIn()