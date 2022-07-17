from features.po.basePage import BasePage
from selenium.webdriver.common.by import By
import random


class CadastralPE(object):
    # LABELS
    LBL_CREATE_AN_ACCOUNT = (By.XPATH, '//h1[contains(.,"Create an account")]')

    # BUTTONS
    BTN_REGISTER = (By.CSS_SELECTOR, 'button#submitAccount')

    # FIELDS
    FIELD_FIRST_NAME = (By.CSS_SELECTOR, 'input#customer_firstname')
    FIELD_LAST_NAME = (By.CSS_SELECTOR, 'input#customer_lastname')
    FIELD_PASSWORD = (By.CSS_SELECTOR, 'input#passwd')
    FIELD_ADDRESS = (By.CSS_SELECTOR, 'input#address1')
    FIELD_CITY = (By.CSS_SELECTOR, 'input#city')
    FIELD_ZIP_CODE = (By.CSS_SELECTOR, 'input#postcode')
    FIELD_MOBILE_PHONE = (By.CSS_SELECTOR, 'input#phone_mobile')
    FIELD_SECOND_EMAIL = (By.CSS_SELECTOR, 'input#alias')

    # CBX/SELECT BUTTON
    CBX_MR = (By.XPATH, '//label[@for="id_gender1"]')
    CBX_MRS = (By.XPATH, '//label[@for="id_gender2"]')
    SELECT_DAY = (By.CSS_SELECTOR, 'select#days')
    SELECT_MONTH = (By.CSS_SELECTOR, 'select#months')
    SELECT_YEAR = (By.CSS_SELECTOR, 'select#years')
    SELECT_STATE = (By.CSS_SELECTOR, 'select#id_state')


class CadastralPage(BasePage):

    def validateCadastralScreen(self):
        return self.is_element_visible(*CadastralPE.LBL_CREATE_AN_ACCOUNT, timeout=15)

    def fillFieldsPersonalInformation(self, person):
        self.click_element(*CadastralPE.CBX_MR) if person.TITLE == 'Mr' else self.click_element(*CadastralPE.CBX_MRS)
        self.fill(person.FIRST_NAME, *CadastralPE.FIELD_FIRST_NAME)
        self.fill(person.LAST_NAME, *CadastralPE.FIELD_LAST_NAME)
        self.fill(person.PASSWORD, *CadastralPE.FIELD_PASSWORD)
        self.click_element(*CadastralPE.SELECT_DAY)
        self.click_element(*(By.XPATH, '//select[@id="days"]/option[@value="' + person.BIRTH_DATE[8:10].lstrip('0') + '"]'))
        self.click_element(*CadastralPE.SELECT_MONTH)
        self.click_element(*(By.XPATH, '//select[@id="months"]/option[@value="' + person.BIRTH_DATE[5:7].lstrip('0') + '"]'))
        self.click_element(*CadastralPE.SELECT_YEAR)
        self.click_element(*(By.XPATH, '//select[@id="years"]/option[@value="' + person.BIRTH_DATE[0:4].lstrip('0') + '"]'))

    def fillFieldsyouraddress(self, person):
        self.fill(person.ADDRESS, *CadastralPE.FIELD_ADDRESS)
        self.fill(person.CITY, *CadastralPE.FIELD_CITY)
        self.click_element(*CadastralPE.SELECT_STATE)
        self.click_element(*(By.XPATH, '//select[@id="id_state"]/option[@value="' + str(random.randint(1, 50)) + '"]'))
        self.fill(person.ZIP_CODE, *CadastralPE.FIELD_ZIP_CODE)
        self.fill(person.MOBILE_PHONE, *CadastralPE.FIELD_MOBILE_PHONE)
        self.fill(person.SECOND_EMAIL, *CadastralPE.FIELD_SECOND_EMAIL)

    def clickRegisterBtn(self):
        self.click_element(*CadastralPE.BTN_REGISTER)
