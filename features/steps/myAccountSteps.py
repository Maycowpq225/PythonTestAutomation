from behave import *
from features.po.myAccountPage import MyAccountPage

@then('validate my account page')
def validateMyAccountPage(context):
    context.myAccountPage = MyAccountPage()
    context.myAccountPage.validateMyAccountScreen()