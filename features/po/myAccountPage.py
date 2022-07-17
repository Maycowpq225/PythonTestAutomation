from features.po.basePage import BasePage
from selenium.webdriver.common.by import By

class MyAccPE(object):
    # LABELS
    LBL_MY_ACCOUNT = (By.XPATH, '//h1[contains(.,"My account")]')


class MyAccountPage(BasePage):
    def validateMyAccountScreen(self):
        return self.is_element_visible(*MyAccPE.LBL_MY_ACCOUNT, timeout=15)
