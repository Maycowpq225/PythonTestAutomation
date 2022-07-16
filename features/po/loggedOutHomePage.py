from features.po.basePage import BasePage
from selenium.webdriver.common.by import By


class LoggedOutHomePageElements(object):
    BTN_WOMEN = (By.XPATH, '//a[contains(.,"Women")]')
    BTN_LOGIN = '//a[@data-purpose="header-login"]'
    BTN_REGISTER = '//a[@data-purpose="header-signup"]'


class LoggedOutHomePage(BasePage):

    def navigateToAutomationPratice(self):
        self.navigate('http://automationpractice.com/index.php')

    def validateLoggedOutHome(self):
        return self.is_element_visible(*LoggedOutHomePageElements.BTN_WOMEN, timeout=15)
