from features.environment import Browser
from selenium.webdriver.common.by import By

class LoggedOutHomePageElements(object):

    CONTAINER_HOME_UDEMY = (By.XPATH, '//body[@class="ud-app-loader logged-out-home-page udemy ud-app-loaded"]')
    BTN_LOGIN = '//a[@data-purpose="header-login"]'
    BTN_REGISTER = '//a[@data-purpose="header-signup"]'

class LoggedOutHomePage(Browser):

    def navigateToAutomationPratice(self):
        self.driver.get('http://automationpractice.com/index.php')
