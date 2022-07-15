import time
from features.browser import Browser

class BasePage(Browser):

    def fill(self, text, *locator):
        self.driver.find_element(*locator).send_keys(text)

    def click_element(self, *locator):
        self.driver.find_element(*locator).click()

    def get_element(self, *locator):
        return self.driver.find_element(*locator)

    def get_text_element(self, *locator):
        return self.driver.find_element(*locator).text

    def scroll_element(self, *locator):
        for i in range(8):
            try:
                if self.get_element(*locator).is_displayed():
                    break
            except: pass
            self.driver.execute_script("window.scrollTo(0, window.scrollY + 200)")
            time.sleep(1)

    def navigate(self, address):
        return self.driver.get(address)

    def get_page_title(self):
        return self.driver.title