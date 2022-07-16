from features.po.basePage import BasePage
from selenium.webdriver.common.by import By


class LoggedOutHomePageElements(object):
    BTN_WOMEN = (By.XPATH, '//a[contains(.,"Women")]')
    BTN_SIGN_IN = (By.XPATH, '//a[@title="Log in to your customer account"]')


class LoggedOutHomePage(BasePage):

    def navigateToAutomationPratice(self):
        self.navigate('http://automationpractice.com/index.php')

    def validateLoggedOutHome(self):
        return self.is_element_visible(*LoggedOutHomePageElements.BTN_WOMEN, timeout=15)

    def clickOnSignIn(self):
        self.click_element(*LoggedOutHomePageElements.BTN_SIGN_IN)
