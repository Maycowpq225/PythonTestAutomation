from behave import *
from nose.tools import assert_true
from features.po.cadastralPage import CadastralPage

@then('validate the cadastral page')
def validateCadastralPage(context):
    context.cadastralPage = CadastralPage(context.driver)
    assert_true(context.cadastralPage.validateCadastralScreen())

@when('fill fields personal information')
def fillFieldsPersonalInformation(context):
    context.cadastralPage.fillFieldsPersonalInformation(context.person)

@when('fill fields your address')
def fillFieldsyouraddress(context):
    context.cadastralPage.fillFieldsyouraddress(context.person)

@when('click on register button')
def clickRegisterBtn(context):
    context.cadastralPage.clickRegisterBtn()

