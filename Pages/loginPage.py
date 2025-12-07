from selenium.webdriver.common.by import By
from Library import get_locator, read_config
import time

class LoginPage:
    def __init__(self,browser):
        self.browser = browser
        self.username_locator = get_locator("Login","username")
        self.password_locator = get_locator("Login","password")
        self.login_button_locator = get_locator("Login","login_button")
        self.inventory_list_locator = get_locator("Login","inventory_list")
        self.burger_menu_locator = get_locator("Login","burger_menu")
        self.logout_button_locator = get_locator("Login","logout_button")
        
    def enter_username(self, username):
        self.browser.find_element(By.ID, self.username_locator).clear()
        self.browser.find_element(By.ID, self.username_locator).send_keys(username)
        
    def enter_password(self, password):
        self.browser.find_element(By.ID, self.password_locator).clear()
        self.browser.find_element(By.ID, self.password_locator).send_keys(password)
        
    def click_login(self):
        self.browser.find_element(By.ID, self.login_button_locator).click()
        
    def is_login_successfull(self):
        try:
            return self.driver.find_element(By.CLASS_NAME, self.inventory_list_locator).is_displayed()
        except Exception as e:
            print(f"Login failed: {e}")
        return False
    
    def logout(self):
        self.driver.find_element(By.ID, self.burger_menu_locator).click()
        time.sleep(1)
        self.driver.find_element(By.ID, self.logout_button_locator).click()
        time.sleep(2)
        