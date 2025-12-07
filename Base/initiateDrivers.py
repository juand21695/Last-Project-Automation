from selenium import webdriver
from Library import read_config


class InitiateDriver:
    browser = None  # Global driver variable

    @classmethod
    def startBrowser(self):
        browser_name = read_config("Details","browser")
        app_url = read_config("Details", "app_url")
        
        if browser_name.lower() == "chrome":
            self.browser = webdriver.Chrome()
        elif browser_name.lower() == "firefox":
            self.browser = webdriver.Firefox()
        elif browser_name.lower() == "brave":
            self.browser = webdriver.Firefox()
        else:
            raise Exception("Unsupport Browser")
        
        #InitiateDriver.browser = webdriver.Firefox()
        self.browser.implicitly_wait(1)
        self.browser.get(app_url)
        self.browser.maximize_window()        
        return self.browser

    @classmethod
    def closeBrowser(self):
        if self.browser is not None:
            self.browser.quit()
            self.browser = None  # Reset browser to None
