from features.po.basePage import BasePage
from selenium.webdriver.common.by import By


class AuthenticationPageElements(object):
    # LABELS
    LBL_AUTHENTICATION = (By.XPATH, '//h1[contains(.,"Authentication")]')

    # BUTTONS
    BTN_SIGN_IN = (By.CSS_SELECTOR, 'p.submit')
    BTN_CREATE_AN_ACCOUNT = (By.CSS_SELECTOR, 'button#SubmitCreate')

    # FIELDS
    FIELD_REGISTER_EMAIL = (By.CSS_SELECTOR, 'input#email_create')
    FIELD_LOGIN_EMAIL = (By.CSS_SELECTOR, 'input#email')
    FIELD_LOGIN_PASSWORD = (By.CSS_SELECTOR, 'input#passwd')


class AuthenticationPage(BasePage):
    def __init__(self, driver):
        self.driver = driver

    def validateAuthenticationPage(self):
        return self.is_element_visible(*AuthenticationPageElements.LBL_AUTHENTICATION, timeout=15)

    def fillRegisterFieldEmail(self, email):
        self.fill(email, *AuthenticationPageElements.FIELD_REGISTER_EMAIL)

    def clickOnCreateAnAccount(self):
        self.click_element(*AuthenticationPageElements.BTN_CREATE_AN_ACCOUNT)

    def fillLoginFieldEmail(self, email):
        self.fill(email, *AuthenticationPageElements.FIELD_LOGIN_EMAIL)

    def fillLoginFieldPassword(self, password):
        self.fill(password, *AuthenticationPageElements.FIELD_LOGIN_PASSWORD)

    def clickOnSignIn(self):
        self.click_element(*AuthenticationPageElements.BTN_SIGN_IN)
