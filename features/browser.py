from selenium import webdriver
from selenium.webdriver.firefox.options import Options


class Browser(object):
    def __init__(self, nameBrowser):
        if nameBrowser == "Firefox":
            options = Options()  # firefox
            options.set_preference('dom.webnotifications.enabled', False)
            options.set_preference('dom.push.enabled', False)
            options.set_preference('geo.enabled', False)
            self.driver = webdriver.Firefox('drivers\geckodriver.exe')
            self.driver.maximize_window()
        else:
            options = webdriver.ChromeOptions()
            # block permission webnotif
            prefs = {"profile.default_content_setting_values.notifications": 2}
            # options.add_experimental_option("prefs",prefs)
            options.add_argument('--headless')
            options.add_argument('--no-sandbox')
            options.add_argument('--disable-dev-shm-usage')
            self.driver = webdriver.Chrome('drivers\chromedriver.exe')
            self.driver.set_window_size(1280, 800)
        self.driver.implicitly_wait(15)
        self.driver.set_page_load_timeout(60)

    def getDriver(self):
        return self.driver

    def close(self):
        self.driver.close()

    def quit(self):
        self.driver.quit()
